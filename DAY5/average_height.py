# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
num_item = 0
sum_item = 0
for l in student_heights:
    if l in student_heights:
        num_item +=1
        sum_item +=l

#finding for the average height
average_height = sum_item / num_item

if sum_item % num_item < 5:
    print(round(average_height))

else:
    average_height + 1

    print(round(average_height))

print(num_item)
print(sum_item)