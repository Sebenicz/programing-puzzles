def check_square(pos):
    square = 1
    power = 1

    while power < pos:

        power = square**2
        square +=2

    square = (square // 2) - 1

    return square
        

def get_list_of_steps_in_square(square):
    steps = square * 2 
    steps_list = []
    half_steps = square
    step = steps

    for i in range(steps):

        steps_list.append(step)
        
        if i < half_steps: 
            step -= 1

        elif i >= half_steps:
            step += 1  

    return steps_list


def get_steps(pos):
    sqr = check_square(pos)
    step_list = get_list_of_steps_in_square(sqr)
    highest_pos_from_lower_square = ((sqr*2) -1) ** 2
    step = pos - highest_pos_from_lower_square
    step = step % (sqr*2)

    return step_list[step]


def spiral_until_at_least(n):
    NEIGHBORS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)] 
    spiral = {}               
    spiral[(0,0)] = 1
    x,y = 0,0
    steps_in_row = 1         
    second_direction = False  
    nstep = 0                 
    step_direction = 0        
    
    while True:
        dx, dy = DIRECTION[step_direction]
        x, y = x + dx, y + dy
        total = 0

        for neighbor in NEIGHBORS:
            nx, ny = neighbor

            if (x+nx, y+ny) in spiral:
                total += spiral[(x+nx, y+ny)]
        
        if total > n:
            return total

        spiral[(x,y)] = total
        nstep += 1

        if nstep == steps_in_row:

            nstep = 0
            step_direction = (step_direction + 1)% 4

            if second_direction:

                second_direction = False
                steps_in_row += 1

            else:
                second_direction = True

def main():
    inp = int(input("Enter the position: "))
    print(get_steps(inp))
    print(spiral_until_at_least(inp))

if __name__ == '__main__':
    main()

