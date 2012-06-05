from itertools import ifilter
from pyforge.all import *

#
#                                SELECTORS
#
def true_selector(node):
    return True

def false_selector(node):
    return False

def type_selector(*node_types):
    return lambda node: isinstance(node, node_types)

#
#                       STOP PROPAGATION EXCEPTIONS
#
class StopPropagation(Exception):
    def __init__(self, levels=1):
        Exception.__init__(
            self, 'Stopped propagation on {0} levels.'.format(levels))
        self.levels = levels

class StopWalk(Exception):
    pass


#
#                                 WALKERS
#
def do_nothing(node):
    pass

def iter_walk(node,
              on_enter       =do_nothing,
              on_exit        =do_nothing,
              selector       =true_selector,
              _top_level_call=True):
    """
    If on_enter throws StopPropagation(n) on some node N, then:

    - N won't be yielded;
    - on_exit(N) won't be called;
    - If n=1, walk will continue on N's immediate sibling, else walk will go
      further up, calling on_exit on the nodes on the way up, since on_enter
      finished successfully (without throwing an exception) on them.

      The general rules are the following:

      - The walk will then continue on N's (n-1)'th parent immediate sibling.
      - on_exit will be called on any node K iff on_enter was called on that
        node, and that call finished successfully without throwing
        StopPropagation exception.

    on_exit shouldn't throw anything. You might try, but I'm not sure how it'll
    work.

    """

    selector_matches = selector(node)
    on_enter_ok = False

    try:
        # on enter
        if selector_matches:
            on_enter(node)
            on_enter_ok = True
            yield node

        # node has no children, just return
        if not hasattr(node, 'doctree'):
            return

        # propagate
        for children_group_name in node.doctree:
            # get child node(s) as list
            children_group = getattr(node, children_group_name)
            if not isinstance(children_group, list):
                children_group = [children_group]

            # walk into each child node
            for child in children_group:
                for _ in iter_walk(child, on_enter, on_exit, selector, False):
                    yield _

    # process stoppers
    except StopPropagation as stop_propagation:
        if stop_propagation.levels > 1 and not _top_level_call:
            raise StopPropagation(stop_propagation.levels - 1)
    except StopWalk:
        if not _top_level_call:
            raise

    # on exit
    finally:
        if selector_matches and on_enter_ok:
            on_exit(node)

def walk(*args, **kwargs):
    eat(iter_walk(*args, **kwargs))

def iter_find(node,
              selector        =true_selector,
              stop_propagation=false_selector,
              stop_siblings   =false_selector,
              stop_walk       =false_selector):
    """
    If stop_propagation triggers on some node N, N and its children will not
    be included into the walk; walk continues on N's immediate sibling.

    If stop_walk triggers on some node N, walk immediately stops, and no more
    nodes will be yielded.

    If stop_siblings triggers on some node N, N and its children will not be
    included into the walk; neither will N's siblings be. Walk continues on a
    N's parent immediate sibling.
    """

    def on_enter(node):
        if stop_propagation(node):
            raise StopPropagation(1)
        elif stop_siblings(node):
            raise StopPropagation(2)
        elif stop_walk(node):
            raise StopWalk()

    return ifilter(selector, iter_walk(node, on_enter))

def find_first(*args, **kwargs):
    return next(iter_find(*args, **kwargs))
