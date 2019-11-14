#this is the first gradebook which will be added later on
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#First its time to create a list of the subjects
subjects = ["physics", "calculus", "poetry", "history"]

#Next is to add the grades to a seperate new list
grades = [98, 97, 85, 88]

#Adding a new subject to the subjects list
subjects.append("computer science")

#Adding the new grade
grades.append(100)

#Combining the two using zip
gradebook = list(zip(subjects, grades))

#Adding another subject to the gradebook, rather then the list
gradebook.append(("visual arts", 93))

#printing the final outcome
print(gradebook)

#combining the new grades with last semesters grades
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
