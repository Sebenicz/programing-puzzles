def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
        lines[i] = int(lines[i])

    return lines


def jumping():
    steps = get_table("day5_file.txt")
    i = 0
    jumps = 0
    while True:
        try:
            steps[i] += 1
            i = i + steps[i] 
            i -= 1
            jumps += 1
            if i < 0:
                raise IndexError
        except IndexError:
            print("out of loop in " + str(jumps) + " jumps.")
            break
            

jumping()