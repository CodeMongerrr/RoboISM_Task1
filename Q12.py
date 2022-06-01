data = input()
arr = data.split()
arr1 = []
a = 0
for i in range(10):
    arr1.append(i+1)
arr.sort()
for i in range(11):
    if int(arr[i]) != arr1[i]:
        a = i
        break
if a != 0:
    print(arr[i]+ " Is the Repeated character")
else:
    print("No character is being repeated")
