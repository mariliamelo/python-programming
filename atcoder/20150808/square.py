
l1, l2, l3 = map(int, raw_input().split())
sides = [l1, l2, l3]

if (l1 != l2) or (l2 != l3):
    for x in sides:
        if sides.count(x) == 1:
            print x
else:
    print l1
