file_path = "day8/input.txt"
result = 0

map = []
antennas = []
antinodes = set()


with open(file_path, "r") as file:
    content = file.read().strip()
    lines = content.split("\n")
    for i, line in enumerate(lines):
        line_map = []
        for j, c in enumerate(line):
            line_map.append(c)
            if c != ".":
                antennas.append(((c, i, j)))
        map.append(line_map)
        
for a in antennas:
    antenna_frequency = a[0]
    antenna_pos = (a[1], a[2])
    
    for ant in antennas:
        if a != ant and ant[0] == antenna_frequency:
            ant_pos = (ant[1], ant[2])
            antinode_pos = (2 * antenna_pos[0] - ant_pos[0], 2 * antenna_pos[1] - ant_pos[1])
            antinodes.add(antinode_pos)

for antinode in antinodes:
    if antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(map) or antinode[1] >= len(map[0]):
        continue
    
    result += 1   
            
for i, line in enumerate(lines):
    for j, c in enumerate(line):    
        if (i, j) in antinodes and c == ".":
            print("#", end="")
        else:
            print(c, end="")
    print()


print(result)