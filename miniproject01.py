import random as r
l=int(input("How many character you want in your password:"))
n=int(input("How many numbers you want in your password:"))
s=int(input("How many symbols you want in your password:"))
characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols=["!","@","#","$","%","^","&","*",":","~","_","+"]

password=""
for i in range(l):
    password += r.choice(characters[:30])
for i in range(n):
    password += str(r.choice(numbers[:30]))
for i in range(s):
    password += r.choice(symbols[:30])

print(f"Password is {password}")