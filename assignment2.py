#task1
a = int(input("enter a number:"))
if a%2 == 0:
    print(f"{a} is an even number.")
elif a%2 ==1:
    print(f"{a} is a odd number.")
else:
    print("input invalid.")

#task2

sum = 0
for i in range(1,51):
    sum+=i
print(f"the sum of numbers from 1 to 50 is: {sum}")