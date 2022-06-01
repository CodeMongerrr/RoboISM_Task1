data = input()
arr = []
for i in range(len(data)):
    arr.append(data[i])
for i in range(len(arr)):
    arr[i] = ord(arr[i])
arr.sort()
for i in range(len(arr)):
    print(chr(arr[i]), end = "")
