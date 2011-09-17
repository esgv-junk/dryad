import collections
from dryad import doctree

__all__ = []

def _emit(text):
    raise NotImplementedError('Writer must set its own emit up')

def _emitRaw(text):
    raise NotImplementedError('Writer must set its own emit up')

emit = _emit
emitRaw = _emitRaw
runningWriterName = None

def reset():
    global emit, emitRaw, writer
    emit = _emit
    emitRaw = _emitRaw
    writer = None

def _nodeEnter(node):
    global runningWriterName
    
    writer = node.writers[runningWriterName]
    writer
    
def _nodeExit(node):

def walk(*nodes):
    for n in nodes:
        doctree.walkDoctree(n, nodeEnter, nodeExit)
        