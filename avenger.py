print("Take the test to find which avenger you are")
print("Which suerpower qualities do you think you posses?")
print("1. intelligence 2.leadership 3.mightly 4.smart 5.strength 6.magical")
x=int(input("enter the value"))
print("Which weapon do you like ")
print("1. hi-tech 2. shield 3. hammer 4.webs 5.bare hands 6.cloak")
y=int(input("enter the input"))
print("Which colour do you like")
print("1.yellow 2.silver 3.red 4.violet 5.green 6.blue")
z=int(input("enter the value"))
avg=int((x+y+z)/3)
if x==y:
    avg=x
elif y==x:
    avg=y
elif z==x:
    avg=z
d=[["IRON MAN",1],["CAPTAIN AMERICA",2],["THOR",3],["SPIDER MAN",4],["HULK",5],["DR STRANGE",6]]
for i in d:
    for j in i:
        if avg==j:
            print("CONGRATULATIOONS!! YOU ARE")
            print(i[0])
        