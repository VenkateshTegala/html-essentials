rows = int(input())
cols = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))
top = 0
bottom = rows - 1
left = 0
right = cols - 1
mylist = []
while top <= bottom and left <= right:
    if top <= bottom:
        for i in range(left, right + 1):
            mylist.append(matrix[top][i])
        top += 1
    if left <= right:
        for i in range(top, bottom + 1):
            mylist.append(matrix[i][right])
        right -= 1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            mylist.append(matrix[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            mylist.append(matrix[i][left])
        left += 1
for number in mylist:
    print(number, end=" ")
        