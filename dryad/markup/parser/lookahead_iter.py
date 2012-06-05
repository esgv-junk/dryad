from itertools import islice, repeat, chain

class LookaheadIter:
    def __init__(self, seq, padding=None):
        self._real_seq = iter(seq)
        self.padding = padding

        self._cached = []
        self._cache_updated()
        self._position = 0

    def _ensure_in_cache(self, index):
        """
        Load at least ``index`` elements from sequence into cache. If sequence
        has less than ``index`` elements left, return ``False``, otherwise
        return ``True``.

        """
        items_needed = index + 1 - len(self._cached)
        if items_needed > 0:
            new_items = list(islice(self._real_seq, items_needed))
            if new_items:
                self._cached.extend(new_items)
                self._cache_updated()
            if len(new_items) < items_needed:
                return False
        return True

    def _cache_updated(self):
        self._iter_seq = \
            self._real_seq if not self._cached else iter(self._cached)

    def next(self):
        result = next(self._iter_seq)
        if self._cached:
            result = self._cached.pop(0)
            self._cache_updated()
        self._position += 1
        return result

    def __iter__(self):
        return self

    def __getitem__(self, index):
        if index < 0:
            raise NotImplementedError("Negative indices not supported.")

        if self._ensure_in_cache(index):
            return self._cached[index]
        else:
            return self.padding

    def position(self):
        return self._position

    def is_done(self):
        return not self._ensure_in_cache(0)
