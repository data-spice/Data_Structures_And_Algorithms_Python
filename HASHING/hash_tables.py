def hash_function(value):
    sum_of_chars=0
    for char in value:
        sum_of_chars  += ord(char)
    
    return sum_of_chars % 10



def add(value):
    index =hash_function[index]
    bucket= hash_set[index]
    if value not in bucket:
        bucket.append(value)
        
def contains(value):
    index=hash_function(value)
    bucket=hash_set[index]
    return value in bucket
    
    

hash_set=[None]*10

arr=list(input("Enter the items separated by a comma: ").split(","))
search=input("Enter the item you want to search for: ")


for names in arr:
    index=hash_function(names)
    hash_set[index]=names
    
print("It is",contains(search),f"that {search} is in the list.")

