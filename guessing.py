import random
num=random.randrange(1,10)
print(num)
n=int(input("enter your guess"))


for i in range(5):
     if num==n:
        print("CONGRATULATIONS")
        break
     else:
         print("not right guess take another chance ")
         n=int(input("enter your guess"))
