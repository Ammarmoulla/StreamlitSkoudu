from random import sample

base  = 3
side  = base * base

def pattern(r,c): 
    return (base * (r % base) + r // base + c) % side

def shuffle(s): 
    return sample(s, len(s))

Range = range(base)
rows  = [ g*base + r for g in shuffle(Range) for r in shuffle(Range) ] 
cols  = [ g*base + c for g in shuffle(Range) for c in shuffle(Range) ]

nums  = shuffle(range(1, base * base + 1))

board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

for line in board: 
    print(line)