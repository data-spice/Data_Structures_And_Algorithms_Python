def linear(arr,element):
    n=len(arr)
    found=[]
    for index,x in enumerate(arr):
        if x == element:
            found.append(index)
            status=1
    if status==1:
        return f"{element} found at the following indexes {found}"
    else:
        return f"{element} was not found."


arr=list(map(int,input("Enter the array values seperated by a comma: ").strip().split(",")))
element=int(input("Enter the value you want to look for: "))
    
print(linear(arr,element))