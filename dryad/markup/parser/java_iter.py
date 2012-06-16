class JavaIter:
    def __init__(self, seq, padding=None):
        self._padding = padding
        self._seq = list(seq)
        self._index = 0

    def _index_valid(self, index):
        return 0 <= index < len(self._seq)

    def next(self):
        if not self._index_valid(self._index):
            raise StopIteration

        result = self._seq[self._index]
        self._index += 1
        return result

    def __getitem__(self, index):
        real_index = self._index + index
        if self._index_valid(real_index):
            return self._seq[real_index]
        else:
            return self._padding

    def __iter__(self):
        return self

    def position(self):
        return self._index

    def is_done(self):
        return self._index >= len(self._seq)
