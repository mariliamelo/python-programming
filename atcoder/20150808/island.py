islands = int(raw_input());
A = map(int, raw_input().split())

if sum(A) == 0:
    print 0
elif sum(A) % islands != 0:
    print -1
else:
    ideal = sum(A) / islands
    total = num = bridge = 0
    for a in A:
        total += a
        num += 1
        if total != ideal*num:
            bridge += 1
    print bridge

