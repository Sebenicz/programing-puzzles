def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
    
    return lines


