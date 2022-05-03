import random
f = open("integer.txt", 'w')
i = int(input("Please enter how many random numbers you want to see: "))
for count in range(i):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
    print(number)
f.close()