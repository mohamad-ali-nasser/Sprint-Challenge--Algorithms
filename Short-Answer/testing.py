a = 0
n = 10000
c = 0
while (a < n * n * n):
    a = a + n * n
    c += 1

print(c, a)

sum = 0
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        sum += 1

print(sum)