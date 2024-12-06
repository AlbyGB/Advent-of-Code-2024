import time

start_time = time.time()

file_path = "day6/input.txt"
result = 0
map = []
pos = (0, 0)

def get_following_pos(pos, direction):
    if direction == "up":
        return (pos[0], pos[1] - 1)
    elif direction == "right":
        return (pos[0] + 1, pos[1])
    elif direction == "down":
        return (pos[0], pos[1] + 1)
    elif direction == "left":
        return (pos[0] - 1, pos[1])

with open(file_path, "r") as file:
    content = file.read().strip()
    map = content.split("\n")
    
    for i, line in enumerate(map):
        if '^' in line:
            pos = (line.index('^'), i)
            break
    for z in range(0, len(map) * len(map[0])):
        direction = "up"
        visited_positions = set()
        moving_pos = pos

        pos_possible_obstacle = (z % len(map[0]), z // len(map[0]))
    
        if map[pos_possible_obstacle[1]][pos_possible_obstacle[0]] in "#^":
            continue
            
        while (moving_pos, direction) not in visited_positions:
            visited_positions.add((moving_pos, direction))
            next_pos = get_following_pos(moving_pos, direction)
            
            if next_pos[1] < 0 or next_pos[1] >= len(map) or next_pos[0] < 0 or next_pos[0] >= len(map[0]):
                break
            
            if map[next_pos[1]][next_pos[0]] == "#" or next_pos == pos_possible_obstacle:
                if direction == "up":
                    direction = "right"
                elif direction == "right":
                    direction = "down"
                elif direction == "down":
                    direction = "left"
                elif direction == "left":
                    direction = "up"
            else:
                moving_pos = next_pos

        if not(next_pos[1] < 0 or next_pos[1] >= len(map) or next_pos[0] < 0 or next_pos[0] >= len(map[0])):
            result += 1
            
    print("Execution time: %s seconds" % (time.time() - start_time))
    print(result)
