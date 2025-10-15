# PROJECT COMPLETED

##### Below is a link to the original project challenge from freeCodeCamp for which the accompanying python file "solution.py" is the solution for. Below that is the task list following my logic for completing the challenge.

#### https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project

****

### Task List 

##### Lines 4-6, Initial Setup
###### Because this project wants us to return the problems formatted into multiple lines, I decided to pull them into different variables using a combination of pythons list comprehension, split, and indexing. The first line would be populated by items from the "first_nums", and the second

##### Lines 9-29, Error Checks
###### This length of code simply contains the logic for ending the program when the errors, outlined in the project guidelines, are caught.

##### Lines 32-56, Base Logic, First Row, Second Row, Dividers
###### Base Logic section is used to do two thing. Detect and store how many problems we are working with, and create a variable for each line that will go into our final answer. Each row is built using its own slightly different logic but it all follows the same pattern. In short, string concactenation is used to part the math problems together but by bit. The length of the longest number in each problem is checked for to ensure each one is as long as it needs to be so they align top to bottom.

##### Lines 59-70, Answers
###### This portion of the code does the same as the others, but it calculates the actual answers of the problems, IF the "show_answers" variable in the initial function is true, before formatting them appropriately into a fourth line.

##### Lines 72-73, Problem solved!
###### I always leave this print statement in, and the finalized formatted answer is returned. Problem solved!
