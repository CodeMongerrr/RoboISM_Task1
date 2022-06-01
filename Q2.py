data = input()
arr = []
for i in range(len(data)):
    arr.append(data[i])
for i in range(len(arr) - 4):
    if arr[i].isdigit():
        arr[i] = "*"
for i in range(len(arr)):
    print(arr[i], end ="")