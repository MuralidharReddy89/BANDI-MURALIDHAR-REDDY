
a = int(input())

count = a if a % 2 != 0 else a - 1

odd_numbers = []
for i in range(1, count + 1):
    odd_numbers.append(2 * i - 1)

print(", ".join(map(str, odd_numbers)))
