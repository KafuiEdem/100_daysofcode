
final_array = []

num = 0

while  num <=9:
    user_input = input('Enter a number: ')
    if int(user_input) <0:
        print('Negative numbers are not allowed')
    else:
        final_array.append(int(user_input))
    num +=1

#inserting -20 after element 3
final_array[2] = -20
#inserting -15 at position 9
final_array[9] = -15
#removing the element at position 2
final_array.remove(2)
#inserting -30 after the first item/element
final_array[1] = -30

print(final_array)