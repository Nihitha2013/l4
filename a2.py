a=int(input("Enter amount:"))

n1=a//100

n2=(a % 100) //50

n3=((a % 100) % 50) //10

n4=(((a % 100) % 50) % 10 )//1
print("100Rs notes:",n1)
print("50 Rs notes:",n2)
print("10 Rs notes:",n3)
print("1 Rs notes:",n4)