"""
Integration project final for COP 1500
"""

# Ashley Battaglia
# This will be a quiz to test your knowledge
# 2/6/21
# https://www.python-ds.com/
__author__ = "Ashley Battaglia"


def main():
    """
This function acts as the point of execution for this program
    """
    print("Hello!", end=' ')
    # end adds space instead of a new line
    print("Welcome to your computer quiz")
    print()
    print("Please enter the following before getting started:")
    print()

    # add name
    name = input("Your Name: ")
    print(name)
    print()

    # add course
    course = input("Your Class: ")
    print(course)
    print()

    # add ID
    i_d = input("Your ID: ")
    print(i_d)
    print()

    # add date
    date = input("Date: ")
    print(date)
    print()
    score_ = 0

    # Q1
    # Used POGIL 03 as reference for Q1-BONUS
    print("Question 1")
    print("What is the difference between 2**3 and 2*3?")
    print()
    print("A. 2**3 is subtracting 2 and 3")
    print("B. 2*3 is dividing 2 by 3")
    print("C. 2*3 is adding 2 and 3")
    print("D. 2**3 is raising 2 to the 3rd power")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'D'
    if answer == correct_answer:
        print("Correct!")
        score_ += 1
        # score_ = score_+1
    print()
    # explanation
    print("2**3 raises 2 to the 3rd power\n2*3 is basic multiplication.")
    print()
    print("2-3=", 2 - 3)
    print("2/3=", 2 / 3)
    print("2+3=", 2 + 3)
    print("2**3=", 2 ** 3)
    print()

    # Q2
    print("Question 2")
    print("What is the difference between 2/5 and 2//5?")
    print()

    print("A. 2/5 subtracts 2 from 5")
    print("B. 2/5 adds 2 and 5")
    print("C. 2//5 multiplies 2 by 5")
    print("D. 2//5 divides and dumps the value after the decimal")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'D'
    if answer == correct_answer:
        print("Good job!")
        score_ += 1
    print()
    # explanation
    print(
        "2/5 is simple division\n2//5 divides and dumps the numbers after "
        "the decimal.")
    print()
    print("2-5=", 2 - 5)
    print("2/5=", 2 / 5)
    print("2*5=", 2 * 5)
    print("2//5=", 2 // 5)
    print()

    # Q3
    print("Question 3")
    print("What is the difference between 2+7 and 2-7?")
    print()

    print("A. 2+7 is adding 2 and 7 together")
    print("B. 2-7 is raising 2 to the 7th power")
    print("C. 2-7 is multiplying 2 by 7")
    print("D. 2+7 is dividing 2 by 7")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'A'
    if answer == correct_answer:
        print("Fantastic!")
        score_ += 1
    print()
    # explanation
    print("2+7 is adding 2 and 7\n2-7 is subtracting 2 from 7.")
    print()
    print("2+7=", 2 + 7)
    print("2-7=", 2 - 7)
    print("2*7=", 2 * 7)
    print("2/7=", 2 / 7)
    print()

    # Q4
    print("Question 4")
    print("What does the int() function do?")
    print()

    print("A. Multiplies two numbers")
    print("B. Adds two numbers")
    print("C. Turns a decimal into a whole number")
    print("D. Subtracts two numbers")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'C'
    if answer == correct_answer:
        print("Amazing!")
        score_ += 1
    print()
    # example
    print("4.5 would turn into 4 if put into the int() function.")
    print()
    print("4*5=", 4 * 5)
    print("4+5=", 4 + 5)
    print("int(4.5)=", int(4.5))
    print("4-5=", 4 - 5)
    print()

    # Q5
    print("Question 5")
    print("What does the float() function do?")
    print()

    print("A. Adds two numbers")
    print("B. Multiplies two numbers")
    print("C. Subtracts two numbers")
    print("D. Adds a decimal to the end of a number")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'D'
    if answer == correct_answer:
        print("Correct!")
        score_ += 1
    print()
    # example
    print("4 would turn into 4.0 if put into the float() function.")
    print()
    print("4+0=", 4 + 0)
    print("4*0=", 4 * 0)
    print("4-0=", 4 - 0)
    print("float(4)=", float(4))
    print()

    # bonus
    print("*BONUS QUESTION*")
    print("What does % do when used in programming?")
    print()

    print("A. Multiplies two numbers")
    print("B. Adds two numbers")
    print("C. Divides and returns the value of the remainder")
    print("D. Divides two numbers")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'C'
    if answer == correct_answer:
        print("Great job!")
        score_ += 2
    print()
    print("5*4=", 5 * 4)
    print("5+4=", 5 + 4)
    print("5%4=", 5 % 4)
    print("5/4=", 5 / 4)
    print()
    x = "Yes! " * 3
    # * 3 repeats the phrase 3 times
    print(x)
    y = "You " + "are " + "very " + "smart!"
    print(y)
    print()
    print()
    print("Here are some example to help you understand more")
    print()
    # extra examples
    examples = ["4**3 = 64", "4*3 = 12", "6//4 = 1", "6/4 = 1.5", "8-3 = 5",
                "6%9 = 6", "int(10.5) = 10", "float(10) "
                                             "= 10.0"]
    print(*examples, sep='\n')
    # sep formats strings that need printed
    # sep also adds separator between strings
    # https://www.studytonight.com/post/the-sep-and-end-parameters-in-python
    # -print-statement
    print()
    print()
    print()
    # sprint 2
    print("Welcome back to your next quiz. Let's begin!")
    print()
    # Q1
    print("Question 1")
    print()

    print("Which statement is true?")
    print()
    # prints the equations
    # Use POGIL 05 as reference for Q1 and Q2
    print("A. 5<4")
    print("B. 5 == 4")
    print("C. 4>=5")
    print("D. 4!=5")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'D'
    if answer == correct_answer:
        print("Great job!")
        score_ += 1
    # prints the answers to the equations
    print()
    print("A", 5 < 4)
    print("B", 5 == 4)
    print("C", 4 >= 5)
    print("D", 4 != 5)
    print()
    # Q2
    print("Question 2")
    print()

    print("Assume you are given a value of 100. Which is true?")
    print()
    # prints the equations

    print("A. 100 > 50 and 100 < 75")
    print("B. 100 < 200 or 100 > 30")
    print("C. 100 * 5 is not 500")
    print()

    answer = input("Choose your answer: ")
    correct_answer = 'B'
    if answer == correct_answer:
        print("Correct")
        score_ += 1
    else:
        print("Incorrect")
    # prints the answers to the equations
    print()

    print("A", (100 > 50) and (100 < 75))
    print("B", (100 < 200) or (100 > 30))
    print("C", not (100 * 5 == 500))
    print()

    # Q3
    # Used POGIL 08 as reference
    print("Question 3")
    print()

    print("Look at the following code. How many numbers are printed?")
    print()

    # prints the code
    print("num=0")
    print("while num != 10: ")
    print("num = num + 1")
    # same as num += 1
    print("print(num)")
    print()

    answer = input("Choose your answer: ")
    correct_answer1 = '10'
    correct_answer2 = 'ten'
    if answer == correct_answer1:
        print("Correct")
    elif answer == correct_answer2:
        print("Correct")
        score_ += 1
    # prints the answer to the code
    print()

    num = 0
    while num != 10:
        num += 1
        print(num)
    print()

    # Q4
    # Used POGIL 09 as reference for Q4-Q5
    print("Question 4")
    print()

    print("Look at the following code. Is the output vertical or horizontal?")
    print()

    # prints the code
    print("soda = ['Pepsi', 'Mountain Dew', 'Coke', 'Sprite']")
    print("for x in soda: ")
    print("print(x)")
    print()

    answer = input("Choose your answer: ")
    correct_answer1 = 'vertical'
    correct_answer2 = 'up and down'
    if answer == correct_answer1:
        print("Correct")
    elif answer == correct_answer2:
        print("Specify the term")
        score_ += 1
    else:
        print("Incorrect")
    # prints the answer to the code
    print()

    soda = ['Pepsi', 'Mountain Dew', 'Coke', 'Sprite']
    for x in soda:
        print(x)
    print()

    # Q5
    print("Question 5")
    print()

    print(
        "Assume you are given range(6, 12, 4). Look at the code and "
        "determine the output")
    print()

    # prints the code
    print("for x in range(6, 12, 4): ")
    print("print(x)")
    print()

    answer = input("Choose your answer: ")
    correct_answer = '6, 10'
    if answer == correct_answer:
        print("Correct")
        score_ += 1
    else:
        print("Incorrect")
    # prints the answer to the code
    print()
    for x in range(6, 12, 4):
        print(x)
    print()
    # Q6
    # https://www.guru99.com/functions-in-python.html
    print("Question 6")
    print()

    print("Look at the code below. What is the output?")
    print()
    # prints the code
    print("def add(t,h):")
    print("print(t + h)")
    print("add(12, 3)")
    print()
    answer = input("Choose your answer: ")
    correct_answer = '15'
    if answer == correct_answer:
        print("Awesome!")
        score_ += 1
    else:
        print("Incorrect")
        print()
        print("You have earned", score_, "points")


def add(t, h):
    # prints the answer to the code in Q6
    """
    This function adds the two numbers given
        :param t: A number to be added to second
        :param h: A number to be added to the first
    """
    print(t + h)

    add(12, 3)
    print()


# return to main
main()
