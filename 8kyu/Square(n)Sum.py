a = [0, 3, 4, 5]
numbers = 0
for i in a:
    numbers += i * i
print(numbers)

numbers = 0
numbers = sum(i ** 2 for i in a)
print(numbers)