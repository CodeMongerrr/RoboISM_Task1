hoe = input()
hoe = hoe.split()
shi = input()
def sorting( hoe, shi):
    if shi == 'asc':
        hoe.sort()
    if shi == 'desc':
        hoe.sort(reverse = True)
    if shi == 'None':
        pass
    return hoe


sorting(hoe, shi)
print(hoe)