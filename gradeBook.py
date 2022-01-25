
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ['Physics', 'Calculus', 'Poetry', 'History']
grades = [98, 97, 85, 88]
gradebook = []

subjects.append('Computer Science')
grades.append(100)

no_subjects = len(subjects)

for x in range(0, no_subjects):
    gradebook.append([subjects[x], grades[x]])

gradebook.append(['Visual arts', 93])
gradebook[5][-1] += 5

gradebook[2].remove(gradebook[2][1])
gradebook[2].append('Pass')

print(no_subjects)
print(subjects)
print(grades)
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)

#/Users/calvinjohnson/PycharmProjects/pythonProject1