
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


# Situations that will return an error:
# If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
# The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
# Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
# Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
