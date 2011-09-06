import itertools
import collections

# eater

def eat(seq, n = None):
    if n is None:
        collections.deque(seq, maxlen = 0)
    else:
        next(itertools.islice(seq, n, n), None)

# LL iterator

def k_forward(seq, end=None, k = 1):
    safe = itertools.chain(seq, itertools.repeat(end, k))
    context = itertools.tee(safe, k+1)
    [eat(context[i], i) for i in range(k+1)]
    return zip(*context)

class k_iter:
    def __init__ (self, seq, end = None, k = 1):
        self.seq = iter(seq)
        self.end = end
        self.k = k
        self.itr = k_forward(seq, end, k)
        self.context = None
        self.done = False

    def __next__(self):
        try:
            self.context = next(self.itr)
        except StopIteration:
            self.done = True
            raise
        return self.context[0]

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if not self.done:
            return self.context[item]
        else:
            raise StopIteration()

    def __repr__(self):

        return repr(self.context)

    def takewhile(self, pred):
        if not self.context:
            next(self)

        while pred(self):
            yield self.context[0]
            if next(self, None) is None:
                break