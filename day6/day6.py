file_path = "day6/input.txt"
result = 0
map = []
pos = (0, 0)

def get_following_pos(pos, map, direction):
    if direction == "up":
        return (pos[0], pos[1] - 1)
    elif direction == "right":
        return (pos[0] + 1, pos[1])
    elif direction == "down":
        return (pos[0], pos[1] + 1)
    elif direction == "left":
        return (pos[0] - 1, pos[1])

with open(file_path, "r") as file:
    content = file.read()
    splitted_content = content.split("\n")
    for line in splitted_content:
        map.append(line)
        
    for i, line in enumerate(map):
        if '^' in line:
            pos = (line.index('^'), i)
            break
        
    print(pos)
    direction = "up"
    map[pos[1]] = map[pos[1]][:pos[0]] + "X" + map[pos[1]][pos[0] + 1:]
    while pos[1] < len(map) and pos[1] >= 0 and pos[0] < len(map[0]) and pos[0] >= 0:
        next_pos = get_following_pos(pos, map, direction)
        if next_pos[1] >= len(map) or next_pos[1] < 0 or next_pos[0] >= len(map[0]) or next_pos[0] < 0:
            break
        if map[next_pos[1]][next_pos[0]] == "#":
            if direction == "up":
                direction = "right"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
        else:
            map[next_pos[1]] = map[next_pos[1]][:next_pos[0]] + "X" + map[next_pos[1]][next_pos[0] + 1:]
            pos = next_pos
            
    for line in map:
        for c in line:
            print(c, end="")
            if c == 'X':
                result += 1
        print()
            
    print(result)