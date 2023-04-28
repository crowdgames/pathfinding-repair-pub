import argparse, math, pprint, random, sys



parser = argparse.ArgumentParser(description='Simple n-grams.')
parser.add_argument('filenames', type=str, nargs='+', help='Input level files.')
parser.add_argument('--gramsize', type=int, help='N-gram size.', required=True)
parser.add_argument('--levelsize', type=int, help='Output level size.', required=True)
parser.add_argument('--transpose', action='store_true', help='Transpose level to use rows instead of columns.')
parser.add_argument('--solid', type=str, help='Solid tiles.')
args = parser.parse_args()



grams = {}
cols_all = {}

for infilename in args.filenames:
    with open(infilename) as infile:
        lines = [_.strip() for _ in infile.readlines()]

    if args.transpose:
        cols = list(reversed(lines))
    else:
        cols = [''.join(_)[::-1] for _ in [*zip(*lines)]]

    for col in cols:
        if col not in cols_all:
            cols_all[col] = set()
        cols_all[col].add(infilename)

    for igram in range(args.gramsize - 1, len(cols)):
        left = tuple(cols[igram - (args.gramsize - 1):igram])
        right = cols[igram]

        if left not in grams:
            grams[left] = []
        grams[left].append(right)



grams_ok = {}
for left, right_options in grams.items():
    right_options_ok = []

    for right_option in right_options:
        next_key = left[1:] + (right_option,)
        if next_key in grams:
            right_options_ok.append(right_option)

    grams_ok[left] = right_options_ok

grams = grams_ok



cols_out = list(random.sample(list(grams.keys()), 1)[0])

while len(cols_out) < args.levelsize:
    left = tuple(cols_out[-(args.gramsize - 1):])
    right_options = grams[left]

    right = random.sample(right_options, 1)[0]
    cols_out.append(right)



if args.transpose:
    level = list(reversed(cols_out))
else:
    level = [''.join(_) for _ in [*zip(*cols_out)]][::-1]

level = [[c for c in r] for r in level]



def isSolid(c):
    if args.solid:
        return c in args.solid
    else:
        return c != '-'

maxX = len(level[0]) - 1
maxY = len(level) - 1

if args.transpose:
    startX = None
    startY = maxY
    while startX == None:
        startY -= 1
        for x in range(1, maxX):
            if not isSolid(level[startY][x]) and isSolid(level[startY + 1][x]):
                startX = x
                break

    goalX = None
    goalY = 0
    while goalX == None:
        goalY += 1
        for x in range(1, maxX):
            if not isSolid(level[goalY][x]) and isSolid(level[goalY + 1][x]):
                goalX = x
                break

else:
    startX = 0
    startY = None
    while startY == None:
        startX += 1
        for y in range(maxY-1, 0, -1):
            if not isSolid(level[y][startX]) and isSolid(level[y + 1][startX]):
                startY = y
                break

    goalX = maxX
    goalY = None
    while goalY == None:
        goalX -= 1
        for y in range(maxY-1, 0, -1):
            if not isSolid(level[y][goalX]) and isSolid(level[y + 1][goalX]):
                goalY = y
                break

level[startY][startX] = '{'
level[goalY][goalX] = '}'



for row in level:
    out = ''
    for col in row:
        out += col
    print(out)
