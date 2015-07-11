# Your task is to process some data.
# You are given 3 integers a , b , c and a string s. Output result of a+b+c and string s with a half-width break.
# get an integer
a = int(raw_input())

# get two integers separated with half-widt break
b, c = map(int, raw_input().split())

# get a string
s = raw_input()

# output
print str(a+b+c) + " " + s
