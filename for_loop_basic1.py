for i in range(151):
    print(i)

for i in range(5, 1000, 5):
    print(i)

for i in range(101):
    if i % 10 == 0:
        print("coding dojo")
        continue
    if i % 5 == 0:
        print("coding")
        continue
    print(i)

sum = 0
for i in range( 1, 500000, 2):
    sum = sum + i
print(f"sum is {sum}")

for i in range (2018,0,-4):
    print(i)

low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)

