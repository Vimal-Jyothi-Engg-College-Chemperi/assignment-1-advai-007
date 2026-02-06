n=int(input("Enter number of elements: "))
ls=[]
for i in range(n):
    ele=int(input("Enter element: "))
    ls.append(ele)
key=int(input("Enter element to search: "))
for ind,num in enumerate(ls):
    if num==key:
        print("Element found at index", ind)
        break
else:
    print("Element not found")