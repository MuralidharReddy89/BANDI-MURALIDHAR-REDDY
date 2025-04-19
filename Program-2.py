
a = int(input())

odd_numbers = []
for i in range(1, a + 1):
    odd_numbers.append(2 * i - 1)

print(", ".join(map(str, odd_numbers)))
