#For Loop with Range

for number in range(0, 101): #Print Numbers 0-100
    print(number)

for number in range(0, 100, 10): #Print Numbers 1-100 multiples of 10
    print(number)

total = 0
for number in range(0, 101):
    total += number
print(total)