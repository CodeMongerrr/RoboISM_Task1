data = input()
arr = []
s = 0
for i in range(len(data)):
    arr.append(data[i])
for i in range(len(arr)):
    if arr[i].isdigit():
        s += int(arr[i])
print(s)