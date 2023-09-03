list1 = [1,4,3,4,5]
for i in range(len(list1)-1):
    if list1[i]>list1[i+1]:
        list1[i], list1[i+1] = list1[i+1], list1[i]

print(list1)