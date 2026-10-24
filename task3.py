def unique_in_order(values):
    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


def word_frequencies(text):
    freq = {}
    for word in text.split():
        word = word.lower().strip(".,;:!?")
        if word == "":
            continue
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_k(frequencies, k):
    ordered = sorted(frequencies.items(), key=lambda pair: (-pair[1], pair[0]))
    return ordered[:k]


def transpose(matrix):
    if not matrix:
        return []
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]


def invert(mapping):
    result = {}
    for key, value in mapping.items():
        result.setdefault(value, []).append(key)
    for keys in result.values():
        keys.sort()
    return result


def common_elements(first, second):
    return sorted(set(first) & set(second))


def group_by_length(words):
    groups = {}
    for w in words:
        groups.setdefault(len(w), []).append(w)
    return groups


class Bag:
    def __init__(self, items=()):
        self._counts = {}
        self._size = 0
        for item in items:
            self.add(item)

    def add(self, item):
        self._counts[item] = self._counts.get(item, 0) + 1
        self._size += 1

    def remove(self, item):
        if self._counts.get(item, 0) == 0:
            raise KeyError(item)
        self._counts[item] -= 1
        self._size -= 1
        if self._counts[item] == 0:
            del self._counts[item]

    def count(self, item):
        return self._counts.get(item, 0)

    def distinct(self):
        return len(self._counts)

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return item in self._counts

    def __iter__(self):
        for item, n in self._counts.items():
            for _ in range(n):
                yield item

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self._counts == other._counts

    def __repr__(self):
        return f"Bag({sorted(self)!r})"



def countdown(n):
    while n >= 1:
        yield n
        n -= 1


def chunks(values, size):
    if size < 1:
        raise ValueError("size must be at least 1")
    return _chunks(values, size)


def _chunks(values, size):
    for start in range(0, len(values), size):
        yield values[start:start + size]