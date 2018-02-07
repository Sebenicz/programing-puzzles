def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        lines[i] = list(map(int, lines[i]))
    
    return lines

print(get_table("day2_table.txt"))