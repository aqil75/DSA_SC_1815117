def movea(cups):
    temp = cups[1]
    cups[1]=cups[0]
    cups[0]=temp
    return cups

def moveb(cups):
    temp = cups[2]
    cups[2]=cups[1]
    cups[1]=temp
    return cups

def movec(cups):
    temp = cups[0]
    cups[0]=cups[2]
    cups[2]=temp
    return cups

cups = ['A','B','C']
order = input()

for i in order:
    if i == 'A':
        cups = movea(cups)
    elif i == 'B':
        cups = moveb(cups)
    elif i == 'C':
        cups = movec(cups)

print(cups.index('B')+1)
