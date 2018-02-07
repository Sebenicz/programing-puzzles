def check_square(pos):
    square = 1
    power = 1

    while power < pos:
        power = square**2
        square +=2

    square= square // 2
    return square
        
