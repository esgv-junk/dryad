from pyforge.iter_utils import group_k_forward

class k_iter:
    
    def __init__ (self, seq, lookahead=1, end_padding='', do_rstrip=True):
        if do_rstrip:
            seq = map(str.rstrip, seq)
        self._k_iter = group_k_forward(iter(seq), end_padding, lookahead)
        self.context_ = None
        self.is_done = False

    def __next__(self):
        try:
            self.context_ = next(self._k_iter)
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
