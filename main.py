import answer as ans
import about as abt
from termcolor import colored
import os

aux = "_"

opt0 = colored('(0)READ ABOUT.', 'yellow')
opt1 = colored('(1)READ THE QUESTIONS.', 'yellow')
opt2 = colored('(2)VIEW ANSWERS.', 'yellow')

print(f"{aux*50} \n\n WELCOME TO OBESITY CLEANED. \n\n {aux*50} \n\n WHAT DO YOU WANT TO ACCOMPLISH TODAY? \n TYPE ON YOUR KEYBOARD AN OPTION IN THE MENU BELOW, WHICH IS IN PARENTHESES AT THE BEGINNING OF THE OPTION. \n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")

answer = int(input('ENTER YOUR ANSWER: '))
while answer < 0 | answer > 2:
    print(f"Oooooops, you must enter a valid option between 0 and 3. \n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")
    answer = int(input('ENTER YOUR ANSWER: '))
else:
    while True:
        if answer == 0:
            abt.about()
        elif answer == 1:
            print(abt.b)
        elif answer == 2:
            while True:
                print('Select one question, typing on your keyboard. \n\n(0)for question 0. \n(1)for question 1. \n(2)for question 2. \n(3)for questio 3.')
                question = int(input('ENTER YOUR ANSWER: '))
                while question < 0 | question > 7:
                    print('Oooooops, you must enter a valid option between 0 and 3.')
                    question = int(input('ENTER YOUR ANSWER: '))
                else:
                    if question == 0: 
                        q0 = ans.obesityforsex()
                        print(q0)
                    elif question == 1: 
                        q1 = ans.maxandmintaxobesity()
                        print(q1)
                    elif question == 2: 
                        q2 = ans.maxmintaxobesityin2015()
                        print(q2)
                    elif question == 3: 
                        q3 = ans.worldandbrazil()
                        print(q3)
                    if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        
        if input('Do you wish to continue? Y for yes and N for NO:-') == "Y":
            os.system('cls')
            print(f"\n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")
            answer = int(input('ENTER YOUR ANSWER: '))
            if answer == 0:
                abt.about()
            elif answer == 1:
                print(abt.b)
            elif answer == 2:
                while True:
                    print('Select one question, typing on your keyboard. \n\n(0)for question 0. \n(1)for question 1. \n(2)for question 2. \n(3)for questio 3.')
                    question = int(input('ENTER YOUR ANSWER: '))
                    while question < 0 | question > 7:
                        print('Oooooops, you must enter a valid option between 0 and 3.')
                        question = int(input('ENTER YOUR ANSWER: '))
                    else:
                        if question == 0: 
                            q0 = ans.obesityforsex()
                            print(q0)
                        if question == 1: 
                            q1 = ans.maxandmintaxobesity()
                            print(q1)
                        if question == 2: 
                            q2 = ans.maxmintaxobesityin2015()
                            print(q2)
                        if question == 3: 
                            q3 = ans.worldandbrazil()
                            print(q3)
                        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        else: break