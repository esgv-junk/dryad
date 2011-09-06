import collections
from dryad import doctree

__all__ = []

def _emit(text):
    raise NotImplementedError('Writer must set its own emit up')

def _emitRaw(text):
    raise NotImplementedError('Writer must set its own emit up')

emit = _emit
emitRaw = _emitRaw
writer = None

def reset():
    global emit, emitRaw, writer
    emit = _emit
    emitRaw = _emitRaw
    writer = None

nodeWriters = collections.defaultdict(lambda:
    lambda node: None)

def nodeEnter(node):
    writers = nodeWriters[type(node), writer]
    if isinstance(writers, tuple):
        writers[0](node)
    else:
        writers(node)

def nodeExit(node):
    writers = nodeWriters[type(node), writer]
    if isinstance(writers, tuple):
        writers[1](node)

def walk(*nodes):
    for n in nodes:
        doctree.walkDoctree(n, nodeEnter, nodeExit)