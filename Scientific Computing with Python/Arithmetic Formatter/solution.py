def arithmetic_arranger(problems, show_answers=False):
    
    # Initial Setup
    first_nums = [item.split(' ')[0] for item in problems]
    operands = [item.split(' ')[1] for item in problems]
    sec_nums = [item.split(' ')[2] for item in problems]

    # Error Checks
    valid_operands = ['+', '-']
    for item in operands:
        if item not in valid_operands:
            answer = "Error: Operator must be '+' or '-'."
            return answer
            
    if len(problems) > 5:
        answer = 'Error: Too many problems.'
        return answer
        
    maybe_nums = ''.join(first_nums+sec_nums)
    num_check = "0123456789"
    for item in maybe_nums:
        if item not in num_check:
            answer = 'Error: Numbers must only contain digits.'
            return answer
    
    for item in (sec_nums + first_nums):
        if len(item) > 4:
            answer = 'Error: Numbers cannot be more than four digits.'
            return answer
    
    # Base Logic
    prob_count = len(problems)
    first_section = f""
    second_section = f""
    dividers = f""
    problem_answers = f""
    
    # First Row
    for count in range(prob_count):
        length = len(str(max([int(first_nums[count]), int(sec_nums[count])])))
        first_section += "  " + (" " * (length - len(first_nums[count]))) + first_nums[count]
        if sec_nums[count] != sec_nums[-1]:
            first_section += " " * 4
    # Second Row
    for count in range(prob_count):
        length = len(str(max([int(first_nums[count]), int(sec_nums[count])])))
        second_section += operands[count] + (" ") + (" " * (length - len(sec_nums[count]))) + sec_nums[count]
        if sec_nums[count] != sec_nums[-1]:
            second_section += " " * 4
    
    # Dividers
    for count in range(prob_count):
        length = len(str(max([int(first_nums[count]), int(sec_nums[count])])))+2
        dividers += "-" * (length)
        if sec_nums[count] != sec_nums[-1]:
            dividers += " " * 4
    
    # Answers
    answers = []
    if show_answers:
        for count in range(prob_count): answers.append(str(eval(f"{first_nums[count]}{operands[count]}{sec_nums[count]}")))
        print(answers)
        for count in range(prob_count):
            length = len(str(max([int(first_nums[count]), int(sec_nums[count])])))+2
            problem_answers += (" " * (length - len(answers[count]))) + answers[count]
            if answers[count] != answers[-1]:
                problem_answers += " " * 4
        answer = f"{first_section}\n{second_section}\n{dividers}\n{problem_answers}"
    else:
        answer = f"{first_section}\n{second_section}\n{dividers}"
    
    print(answer)
    return answer
