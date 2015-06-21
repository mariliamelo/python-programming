line = [0,0,4,4]

print line

def merge(line):
    line2 = [x for x in line if x]
    print line2
    for i in range(1, len(line2)):
        if line2[i] == line2[i-1]:
            line2[i-1] = 2*line2[i]
            line2[i] = 0
    print line2
    line2 = [x for x in line2 if x]
    print line2
    return line2 + [0]*(len(line)-len(line2))
                                   
newline = merge(line)
print newline
