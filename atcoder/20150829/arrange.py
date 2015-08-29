import itertools
number = map(int, raw_input().split())

results = set()

for result in itertools.combinations(number,3):
    results.add(sum(result))

answers = sorted(results)
print answers[-3]

print "Learnings: itertools and combinations are very useful. Set/Lists are clear in my mind"
