from time import perf_counter

start = perf_counter()

result = []
rows_a = int(input("Rows number of matrix A: "))
cols_a = int(input("columns number of matrix A: "))

a = []
print("numbers of matrix A: ")
for i in range(rows_a):
    row = list(map(int, input().split()))
    a.append(row)


rows_b = int(input("Rows number of matrix B: "))
cols_b = int(input("columns number of matrix B:  "))

b = []
print("numbers of matrix B: ")
for i in range(rows_b):
    row = list(map(int, input().split()))
    b.append(row)


if cols_a != rows_b:
    print("Error: Number of columns of matrix A should be equal to number of rows of matrix B")
else:
    result = [[0 for j in range(cols_b)] for i in range(rows_a)]

for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j] += a[i][k] * b[k][j]
for row in result:
    print(row)

end = perf_counter()
print(f"Program execution time: {end - start:.2f}")