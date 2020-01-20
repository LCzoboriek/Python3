#This program averages test scores input from a teacher

#First im going to aquire the number of students
num_students = int(input('How many students do you have? '))

#Next im going to get the number of test scores to acquire
num_test_scores = int(input('How many different test scores do you have per student? '))

#Determine the average
for students in range(num_students):
    #Start of by initialising the accumulator
    total = 0.0
    print('Student number', students + 1)
    print('------------------')
    for test_num in range(num_test_scores):
        print('Test number', test_num + 1, end='')
        score = float(input(': '))
        total += score

        average = total / num_test_scores

        print('The average for student number', students + 1, 'is: ', average)

        print()
