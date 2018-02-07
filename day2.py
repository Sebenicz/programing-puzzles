def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        lines[i] = list(map(int, lines[i]))
    
    return lines


def count_solution_1(filename):

    table = get_table(filename)

    solution_1 = 0

    for line in table:
        solution_1 += max(line) - min(line)

    return solution_1


def count_solution_2(filename):

    table = get_table(filename)
    
    solution_2 = 0
    i = 0 
    while i < len(table):
        j=0
        
        while j < len(table[i]):
            k = 0

            while k < len(table[i]):
                
                if table[i][j] % table[i][k] == 0 and j != k:
                    solution_2 += table[i][j] / table[i][k]

                k += 1

            j += 1

        i += 1

    solution_2 = int(solution_2)

    return solution_2

    
print(count_solution_1("day2_table.txt"))
print(count_solution_2("day2_table.txt"))