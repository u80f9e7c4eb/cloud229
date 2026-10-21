"""Odds and ends."""

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(clamp(3, 0, 25))
