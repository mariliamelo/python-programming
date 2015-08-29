a = int(raw_input())

def results(a):
    if a < 60:
        print "Bad"
    elif a >= 60 and a < 90:
        print "Good"
    elif a >= 90 and a < 100:
        print "Great"
    else:
        print "Perfect"

results(a)

print "Learnings: there is no switch/case in python and no && - you need to use 'and'. It is better to not use method and directly compare the numbers"
