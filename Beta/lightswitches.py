def lightswitch(n):
    lights = [0] * n
    for a in xrange(n):
        for b in xrange(a, n, a + 1):
            lights[b] = int(not lights[b])
    return sum(lights)


assert lightswitch(3) == 1
assert lightswitch(4) == 2
