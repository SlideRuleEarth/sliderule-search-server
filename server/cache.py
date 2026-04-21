"""Small thread-safe LRU cache for ranking results.

We don't use functools.lru_cache because its hashing machinery gets in
the way (ranking results contain nested dicts, categories arrive as
lists, and we want a single clear() to wipe everything on corpus
reload in dev). An OrderedDict-backed LRU is 30 lines and does exactly
what we need.
"""

from __future__ import annotations

from collections import OrderedDict
from threading import Lock
from typing import Any, Hashable


class LRUCache:
    def __init__(self, maxsize: int = 1024) -> None:
        self._data: OrderedDict[Hashable, Any] = OrderedDict()
        self._max = maxsize
        self._lock = Lock()
        self.hits = 0
        self.misses = 0

    def get(self, key: Hashable) -> Any | None:
        with self._lock:
            if key in self._data:
                self._data.move_to_end(key)
                self.hits += 1
                return self._data[key]
            self.misses += 1
            return None

    def set(self, key: Hashable, value: Any) -> None:
        with self._lock:
            self._data[key] = value
            self._data.move_to_end(key)
            if len(self._data) > self._max:
                self._data.popitem(last=False)

    def clear(self) -> None:
        with self._lock:
            self._data.clear()

    def stats(self) -> dict:
        with self._lock:
            total = self.hits + self.misses
            return {
                "hits": self.hits,
                "misses": self.misses,
                "hit_rate": self.hits / total if total else 0.0,
                "size": len(self._data),
                "maxsize": self._max,
            }
