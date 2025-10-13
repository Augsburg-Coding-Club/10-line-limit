k = 60
bounces = int(input("Enter number of bounces: "))

for _ in range(bounces):
    # Move right
    for i in range(k):
        print(" " * i + "*")
    # Move left
    for i in range(k - 2, -1, -1):
        print(" " * i + "*")
