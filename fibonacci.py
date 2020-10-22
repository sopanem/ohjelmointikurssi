n = int(input("How many Fibonacci numbers do you want? "))

f1 = 0
f2 = 1
for i in range(1, n + 1):
    f3 = f2
    f2 = f1 + f2
    f1 = f3
    print("{}. {}".format(i, f1))
