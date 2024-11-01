
student_names = ['Sandra','Partricia','Phiona','Anitah']
student_marks = [80,56,78,90]
data = ['Sandra',90,'Kamwokya']

# Print excluding the first and the last students
print(student_names[1:3])

# add Masha at the fourth position
student_names.insert(4,'Masha')
print(student_names)

#Update the name Phiona Aladinah
student_names.append('Phiona Aladinah')
print(student_names)

#display the length of the list
list_length = len(student_names)
print(list_length)

#Print all the students  names using a for loop
for name in student_names:
    print(name)

#calculate the total marks for the students marks304
total_marks = sum(student_marks)
print(f'The total marks of the students is {total_marks}')