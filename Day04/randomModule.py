import random
import exportedModule

# random_number = random.randint(1, 50)
random_float = random.random() * 5 #Number between 0 - 1 and times'd by 5
print(random_float)
# print(random_number)

lottery_a = random.randint(1, 50)
lottery_b = random.randint(1, 50)
lottery_c = random.randint(1, 50)
lottery_d = random.randint(1, 50)
lottery_e = random.randint(1, 50)

print(lottery_a, lottery_b, lottery_c, lottery_d, lottery_e)

print(exportedModule.pi) #Imported the Variable from another file.

love_score = random.randint(1, 100)
print(f"Your Love Score Is.. {love_score}")