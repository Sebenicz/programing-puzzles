def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        lines[i] = list(map(int, lines[i]))
    
    return lines

def count_solution(filename):

    table = get_table(filename)

    solution = 0

    for line in table:
        solution += max(line) - min(line)

    return solution

print(count_solution("day2_table.txt"))