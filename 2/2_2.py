def max_per_color_on_line(line):
    _, grabs = line.rstrip().split(':')
    grabs = [grab.split(',') for grab in grabs.split(';')]
    flat_grabs = [x for y in grabs for x in y]
    return max_per_color(flat_grabs)

def max_per_color(flat_grabs):
    max_per_color = {'red': 0, 'green': 0, 'blue': 0}
    for grab_color in flat_grabs:
        for color in max_per_color:
            if color in grab_color:
                num = int(grab_color.replace(color, '').strip())
                max_per_color[color] = max(max_per_color[color], num)
    return max_per_color 

with open('input', 'r') as f:
    maxes = [max_per_color_on_line(line) for line in f.readlines()]
    powers = [r*g*b for (r, g, b) in [m.values() for m in maxes]]
    print(sum(powers))