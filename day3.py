def check_square(pos):
    square = 1
    power = 1

    while power < pos:
        power = square**2
        square +=2

    square= square // 2
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


