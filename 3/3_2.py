def num_coords(line, y):
    nums_with_coords = []
    num = ''
    in_num = False
    line = line + '.' # fix numbers at line ends
    for i, c in enumerate(line):
        if c.isdigit():
            in_num = True
            num += c
        else:
            if not in_num: continue
            coords = [(x, y) for x in range(i - len(num), i)]
            nums_with_coords.append((int(num), coords))
            in_num = False
            num = ''
    return nums_with_coords

def sym_coords(line, y):
    syms_with_coords = []
    for x, c in enumerate(line):
        if c != '.' and not c.isdigit():
            syms_with_coords.append((c, (x, y)))
    return syms_with_coords

def is_adjacent(a, b):
    return abs(a[0] - b[0]) < 2 and abs(a[1] - b[1]) < 2

def is_sym_adjacent_to_two_nums(sym, nums):
    adjacent_nums = []
    for num in nums:
        for num_coord in num[1]:
            if is_adjacent(num_coord, sym[1]):
                #print(f'{num[0]} adjacent to {sym[0]}')
                adjacent_nums.append(num[0])
                break

    return adjacent_nums if len(adjacent_nums) == 2 else None

def plot(nums, syms, lines):
    import matplotlib.pyplot as plt
    from matplotlib.collections import PatchCollection
    from matplotlib.patches import Rectangle

    rows = len(lines)
    cols = len(lines[0].strip())

    px = 1 / plt.rcParams['figure.dpi']
    _, ax = plt.subplots(figsize=(1000*px, 1000*px))

    ax.set_xlim(-1, rows+1)
    ax.set_ylim(-1, cols+1)
    
    num_boxes = [[Rectangle((coord[0], rows - coord[1] - 1), 1, 1) \
                  for coord in num[1]] for num in nums]
    num_boxes = [i for j in num_boxes for i in j] # flatten
    sym_boxes = [Rectangle((sym[1][0], rows - sym[1][1] - 1), 1, 1) \
                  for sym in syms]
    
    num_pc = PatchCollection(num_boxes, facecolor='skyblue')
    sym_pc = PatchCollection(sym_boxes, facecolor='gold')

    ax.add_collection(num_pc)
    ax.add_collection(sym_pc)

    for y in range(rows):
        for x in range(cols):
            _x = x
            _y = rows - y
            _text = lines[y][x]
            ax.text(_x, _y, _text,
                    fontsize=6, ha='left', va='top')
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()

with open('input', 'r') as f:
    lines = f.readlines()

    nums = []
    syms = []
    for i, line in enumerate(lines):
        line = line.strip()
        nums.append(num_coords(line, i))
        syms.append(sym_coords(line, i))

    # flatten and remove empty
    nums = [num for line in nums for num in line if not len(line) == 0]
    syms = [sym for line in syms for sym in line if not len(line) == 0]

    syms_adjacent_to_two_nums = [(sym, is_sym_adjacent_to_two_nums(sym, nums)) \
                                 for sym in syms]
    syms_adjacent_to_two_nums = [sym for sym in syms_adjacent_to_two_nums \
                                 if not sym[1] is None]
    
    plot(nums, [sym[0] for sym in syms_adjacent_to_two_nums], lines)

    ratios = [sym[1][0]*sym[1][1] for sym in syms_adjacent_to_two_nums]
    
    print(sum(ratios))
