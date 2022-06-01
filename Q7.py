data = input()
arr = data.split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()
max = 0
num = arr[0]
for i in arr:
    freq = arr.count(i)
    if freq > max:
        max = freq
        num = i
print("Highest Frequency :" + str(num))