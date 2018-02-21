Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>##Calculate average grade for Student
>>>##Program to compute average grade in class (will include syllabus, mid and final exam that are equally weighted
>>>
>>>print ('This program will calculate the average grade for a student')
>>>print ("Please input necessary data as requested. ")


>>>name_first = input("What is student's first name? ")
What is student's first name?
>>>name_last = input("What is the student's last name? ")
What is student's last name?
>>>## Entering the values for the exam scores
>>>print ('Now enter the exam scores as requested: ')
>>>print ("Then press 'ENTER' ")

>>>score_syllabusexam = int(input('Enter syllabus exam score: '))
Enter syllabus exam score:

>>>score_midtermexam = int(input('Enter mid term exam score: '))
Enter mid term exam score:

>>> score_finalexam = int(input('Enter final exam score: '))
Enter final exam score:


>>> ##Will Calculate Average Score for all 3 examinations
>>> ## Average Score = sum of 3 exams divided by three

>>>Print ('The program will now calculate average grade for ', first_name, last_name )
>>>## Calculate average grade for student
>>>## Program will compute average for syllabus, mid term and final exams
>>>
>>>score_average = float((score_syllabusexam + score_midtermexam + score_finalexam)/(3))
>>> ## Show Output calculation for Average Score for three exams
>>>
>>>print('The average score is: ', score_average)
>>>print('Hello' , name_first, name_last, 'your average score is' , score_average )
>>>#Score average will also be presented as percentage of total test scores
>>>#Score average percent equals score_average divided by perfect score (150) for each test
score_percent_average_score = score_average / 150
>>>print('Your average percentage grade is', float(format(score_average.1F)))


