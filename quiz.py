print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. How many legs does a spider have? ').lower()
    if ques == '8':
        score +=1
        print('correct! you got 1 point')       
    else:
        print('Incorrect!')
        print(f'current answer is --> 8')
# ------1
    question_no += 1
    ques = input(f'\n{question_no}. How many seconds make one hour? ').lower()   
    if ques == '3600':
        score +=1
        print('correct! you got 1 point')       
    else:
        print('Incorrect!')
        print(f'current answer is --> 3600')
# -----2
    question_no += 1
    ques = input(f'\n{question_no}. Which animal is known as the ship of the desert? ').lower()   
    if ques == 'camel':
        score +=1
        print('correct! you got 1 point')       
    else:
        print('Incorrect!')
        print(f'current answer is --> camel')
# -----3
    question_no += 1
    ques = input(f'\n{question_no}. How many legs do insects have? ').lower() 
    if ques == '6':
        score +=1
        print('correct! you got 1 point')      
    else:
        print('Incorrect!')
        print(f'current answer is --> 6')
# -----4
    question_no += 1
    ques = input(f'\n{question_no}. How many days are there in a year? ').lower()  
    if ques == '365':
        score +=1
        print('correct! you got 1 point')       
    else:
        print('Incorrect!')
        print(f'current answer is --> 365')
# ------5 
else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')
print(f'{percentage}% questions are correct.')