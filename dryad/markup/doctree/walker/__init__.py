from dryad.markup.doctree.walker.selectors import \
    true_selector, false_selector, type_selector

class StopPropagation(Exception):
    def __init__(self, levels = 1, message=''):
        Exception.__init__(self, message)
        self.levels = levels

class StopWalk(Exception):
    pass

def do_nothing(node):
    pass

def walk(node,
         on_enter=do_nothing,
         on_exit=do_nothing,
         selector=true_selector,
         raise_stop_exceptions=False):

    selector_matches = selector(node)

    try:
        if selector_matches:
            on_enter(node)
            yield node

        if not hasattr(node, 'doctree'):
            return

        for child_name in node.doctree:
            child_nodes = getattr(node, child_name)
            if not isinstance(child_nodes, list):
                child_nodes = [child_nodes]

            for child_node in child_nodes:
                grandchild_nodes = walk(
                    child_node,
                    on_enter,
                    on_exit,
                    selector,
                    True,
                )

                for grandchild_node in grandchild_nodes:
                    yield grandchild_node

    except StopPropagation as stop_propagation:
        if stop_propagation.levels > 1 and raise_stop_exceptions:
            raise StopPropagation(stop_propagation.levels - 1)

    except StopWalk:
        if raise_stop_exceptions:
            raise

    finally:
        if selector_matches:
            on_exit(node)

def find(node,
         selector=true_selector,
         stop_propagation=false_selector,
         stop_siblings=false_selector,
         stop_walk=false_selector):

    def on_enter(node):
        if stop_propagation(node):
            raise StopPropagation()
        if stop_siblings(node):
            raise StopPropagation(2)
        if stop_walk(node):
            raise StopWalk()

    return filter(selector, walk(node, on_enter))

def find_first(node,
               selector=true_selector,
               stop_propagation=false_selector,
               stop_siblings=false_selector,
               stop_walk=false_selector):
    return next(
        find(node, selector, stop_propagation, stop_siblings, stop_walk),
        None
    )
