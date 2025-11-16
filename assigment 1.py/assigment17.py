#Q=1.
for i in range(1,6):
    print("*"*i)
#Q=2.
for i in range(5, 0, -1):
    print("* " * i)
#Q=3.
for i in range(5):
    print("  " * i + "* " * (5 - i))
#Q=4.
for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)
#Q=5.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()