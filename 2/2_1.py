def is_game_valid(line):
    id, grabs = line.rstrip().split(':')
    id = int(id.split(' ')[1])
    grabs = [grab.split(',') for grab in grabs.split(';')]
    valids = [is_grab_valid(g) for g in grabs]
    return id, all(valids)

def is_grab_valid(grab):
    for grab_color in grab:
        for color, limit in {'red': 12, 'green': 13, 'blue': 14}.items():
            if color in grab_color:
                num = int(grab_color.replace(color, '').strip())
                if num > limit: return False
    return True

with open('input', 'r') as f:
    valids = [is_game_valid(line) for line in f.readlines()]
    print(sum([id for (id, valid) in valids if valid]))
