print("             Multiplication Table")
print("  |", end='')

for j in range(1, 10):
    print("  ", j, end='')

print()
print("------------------------------------------")

for row in range(1, 10):
    print(row, "|", end='')
    for col in range(1, 10):
        print(format(row * col, "4d"), end='')
    print()


