def arithmetic_arranger(problems, show_answers=False):
    if not show_answers:
        pass
    first_nums = [item.split(' ')[0] for item in problems]
    operands = [item.split(' ')[1] for item in problems]
    sec_nums = [item.split(' ')[2] for item in problems]

    answer = 'Pie'
    valid_operands = ['+', '-']
    answers = []
    
    for item in operands:
        if item not in valid_operands:
            answer = "Error: Operator must be '+' or '-'."
            break
    
    
    
    print(answer)


arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)

arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
