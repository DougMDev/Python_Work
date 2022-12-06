# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowered1 = name1.lower()
lowered2 = name2.lower()
t1 = lowered1.count('t')
t2 = lowered2.count('t')
r1 = lowered1.count('r')
r2 = lowered2.count('r')
u1 = lowered1.count('u')
u2 = lowered2.count('u')
e1 = lowered1.count('e')
e2 = lowered2.count('e')

l1 = lowered1.count('l')
l2 = lowered2.count('l')
o1 = lowered1.count('o')
o2 = lowered2.count('o')
v1 = lowered1.count('v')
v2 = lowered2.count('v')
e3 = lowered1.count('e')
e4 = lowered2.count('e')

total1 = t1 + t2 + r1 + r2 + u1 + u2 + e1 + e2
total2 = l1 + l2 + o1 + o2 + v1 + v2 + e3 + e4
lovescore = str(total1) + str(total2)
formatted_score = int(lovescore)

if formatted_score < 10 or formatted_score > 90:
    print(f"Your score is {formatted_score}, you go together like coke and mentos.")
elif formatted_score >= 40 and formatted_score <= 50:
    print(f"Your score is {formatted_score}, you are alright together.")
else:
    print(f"Your score is {formatted_score}")