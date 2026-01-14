fruits=["apple","mango","banana","grapes","bluebery"]
print("list of fruits=",fruits)

fruits.append("orange")
print("after adding orange =",fruits)

fruits.remove("orange")
print("after removing orange =",fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)




def second_largest(num):
    # Initialize first and second with the first two numbers in the list
    if num[0] > num[1]:
        first, second = num[0], num[1]
    else:
        first, second = num[1], num[0]
    
    # Iterate through the rest of the numbers
    for n in num[2:]:
        if n > first:
            first, second = n, first
        elif n > second and n != first:
            second = n
    
    return second

num = []

# Taking runtime input
print('Enter any 10 positive numbers:')
count = 0
while count < 10:
    try:
        item = int(input(f'num{count + 1} = '))
        if item > 0:
            num.append(item)
            count += 1
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Find and print the second largest number
sl = second_largest(num)
print('Second Largest Number =', sl)
