import itertools
import collections


def eat(seq, n=None):
    if n is None:
        collections.deque(seq, maxlen=0)
    else:
        next(itertools.islice(seq, n, n), None)
        
def group_k_forward(seq, end_padding=None, lookahead=1):
    safe_seq = itertools.chain(seq, itertools.repeat(end_padding, lookahead))
    context = itertools.tee(safe_seq, lookahead + 1)
    [eat(context[i], i) for i in range(lookahead + 1)]
    return zip(*context)


class k_iter:
        
    def __init__ (self, seq, lookahead=1, end_padding='', do_rstrip=True):
        if do_rstrip:
            seq = map(str.rstrip, seq)
        self.k_iter_ = group_k_forward(iter(seq), end_padding, lookahead)
        self.context_ = None
        self.is_done = False

    def __next__(self):
        try:
            self.context_ = next(self.k_iter_)
        except StopIteration:
            self.is_done = True
            raise
        return self.context_[0]

    def __iter__(self):
        return self

    def __getitem__(self, item):
        if not self.is_done:
            return self.context_[item]
        else:
            raise StopIteration()

    def takewhile(self, pred):
        if not self.context_:
            next(self)

        while pred(self):
            yield self.context_[0]
            if next(self, None) is None:
                break

    def __repr__(self):
        return repr(self.context_)
