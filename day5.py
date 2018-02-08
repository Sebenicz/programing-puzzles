def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        lines[i] = int(lines[i])

    return lines

#get_table("day5_file.txt")