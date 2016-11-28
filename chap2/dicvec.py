
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def print(self):
        for key in sorted(self.f, key=hash):
            print("%s:%s" % (key, str(self.f[key])))


def setitem(v, d, val):
    v.f[d] = val


def getitem(v, d):
    if d in v.f:
        return v.f[d]
    else:
        return 0


def scalar_mul(v, alf):
    return Vec(v.D, {d:alf*val for d, val in v.f.items()})


def add(u, v):
    return Vec(u.D, {d:getitem(u, d)+getitem(v, d) for d in u.D})


def neg(v):
    return scalar_mul(v, -1)


def list2vec(L):
    return Vec(set(range(Len(L))), {k:x for k, x in enumerate(L)})

def main():
    v = Vec({'A', 'B', 'C'}, {'A':1})
    for d in v.D:
        if d in v.f:
            print(v.f[d])

    setitem(v, 'B', 2)
    print(getitem(v, 'A'))
    print(getitem(v, 'B'))
    scalar_mul(v, 2).print()

    u = Vec(v.D, {'A':5, 'C':10})
    add(u, v).print()
    neg(v).print()

if __name__ =="__main__":
    main()