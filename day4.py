def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "").split(" ")
    
    return lines

def count_solution_1():
    table = get_table("day4_file.txt")
    
    solution=0

    for line in table:

        if chceck_repets(line):
            solution += 1

    return solution

def chceck_repets(pasw):

    for word in pasw:
    
        if pasw.count(word) != 1:
            return False
    
    return True

def main():
    print("solution to part 1: " + str(count_solution_1()))

if __name__=='__main__':
    main()