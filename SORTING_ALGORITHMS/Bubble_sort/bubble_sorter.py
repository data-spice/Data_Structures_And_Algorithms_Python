#User Input
values=input("Enter the values seperated by a comma: ").strip().split(",")
arr=list(map(int,values))

#Code
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(f"The sorted array is \n {arr}")