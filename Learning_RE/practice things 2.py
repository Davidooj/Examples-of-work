n = int(input(""))
A = []

for x in range(n):
    A.append(x)
    sort = A.sort(reverse=True)

print(A[1])
print(A)