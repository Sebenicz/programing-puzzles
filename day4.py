def get_table(filename):

    with open(filename) as f:
        lines = f.readlines()  

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    
    return lines


def count_solution():
    table = get_table("day4_file.txt")
    
    solution1 = 0
    solution2 = 0

    for line in table:

        if chceck_repets(line):
            solution1 += 1

        if check_anagrams(line):
            solution2 += 1

    return solution1, solution2


def chceck_repets(pasw):

    for word in pasw:
    
        if pasw.count(word) != 1:
            return False
    
    return True


def check_anagrams(pasw):
    
    for i in range(len(pasw)):

        pasw[i] = sorted(pasw[i])
    
    return chceck_repets(pasw)
    


def main():
    sol1, sol2 = count_solution()
    print("solution to part 1: " + str(sol1))
    print("solution to part 2: " + str(sol2))

if __name__=='__main__':
    main()