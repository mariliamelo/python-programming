letters = raw_input()

# print list_letter.count('A'), list_letter.count('B'), list_letter.count('C'), list_letter.count('D'), list_letter.count('E'), list_letter.count('F')

print " ".join(str(letters.count(a)) for a in "ABCDEF")

# print "Learnings: I don't like this answer. There must be a way to create list from first line and better approach for calling the same method 6 times"
