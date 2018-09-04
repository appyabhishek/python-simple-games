import random
import time

print("********** WELCOME TO THE BOLLYWOOD QUIZ **********")
time.sleep(2)
user = 'Start'
count = 1
score = 0
k = 0
questions = ['jaipur','dubey','aishwarya','dhoni','sachin']
clues = {
    0:['Pink city of India','It is in Rajasthan'],
    1:['he is gaandu','he is lodu'],
    2:['daughter in law of amitabh bachhan','wife of abhishek bachhan'],
    3:['he wears the number7 jearsy','sakshi is his wife'],
    4:['most centuries','most runs']

    }
list=[]
for i in range(5):
    r = random.randint(0,4)
    if r not in list: list.append(r)
          
          
while(user != 'x' or user != 'X'):
    if(count > len(list)):
        break
    user = input("PRESS ANY KEY TO PLAY AND 'X' TO QUIT ")
    if(user == 'x' or user == 'X'):
        break

    
    rand_question_number = list[k]
    #jumbled = ""
    
    duplicate_question = questions[rand_question_number]
    clues_to_question = duplicate_question
    str_length = len(duplicate_question)
    jumbled = ''.join(random.sample(duplicate_question,str_length))

    print(" Your Question ", count , "is")
    print(jumbled)
    display_options = input(" press 'D' to display the clues ")
    if(display_options == 'D' or display_options == 'd'):
        flag = clues[rand_question_number]
        for i in range(2):
            print(i+1, ". ", flag[i])

    answer = input("Enter the answer ")
    if(answer == duplicate_question):
        print("Your answer is correct")
        score = score + 5
        print("Your score is ", score)
    else:
        print("Your answer is wrong")
        score = score - 5
        print("Your score is ", score)

    count = count+1
    k = k+1
    
            

print("Your final score is ",count)
        
            
        

    
