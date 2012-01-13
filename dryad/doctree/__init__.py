from pyforge.all import *

id_dispatcher = IdDispatcher()


def get_parent(element):
    pass

def get_siblings(element):
    pass

def get_siblings_index(element):
    pass


def reset_id_dispatcher():
    global id_dispatcher
    id_dispatcher.clear()

def create_doctree_structure(root):
    pass

before_parse_document = [reset_id_dispatcher]
after_parse_document  = [create_doctree_structure]