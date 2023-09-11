for i in range(151):
    print(i)

for i in range (201) :
    a=i*5
    print(a)

for i in range(101):
    if i % 5 ==0 :
        print(f"coding {i}")
    elif i % 10 ==0 :
        print(f"coding dojo{i}")
    else :
        print(i)


for i in range (500000):
    if i % 2 == 1 :
        a+=i

print(a)
num = 2018
decrement = 4
while num >= 0:
    print(num)
    num -= decrement


lowNum = int(input("enter a lownum :"))
highNum = int(input("enter a highnum :"))
mult = int(input("enter a mult :"))

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)