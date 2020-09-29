print("Enter Rows:")
n = int(input().strip()) #rows
print("Enter Columns:")
m = int(input().strip()) #columns
a = [[0]*n for _ in range(m)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]
print(a)

R=len(a)
C = len(a)
rows, cols = set(), set()

for i in range(R):
    for j in range(C):
        if a[i][j] == 0:
            rows.add(i)
            cols.add(j)

        
for i in range(R):
    for j in range(C):
        if i in rows or j in cols:
            a[i][j] = 0
print(a)