count = 1 
while count <= 5: 
    print("Hello World...")
    count += 1
print(count)
# use list to display variables
heroes = [ "Superman", "Spiderman", "Batman", "Ironman" ]
idx = 0
while idx < len(heroes) :
    print(heroes[idx])
    idx +=1

# Tuple use brake statment
nums = [ 12, 22, 33, 41,55, 52 ,63 ,75 ,80]
x = 55
i = 0
while  i<len(nums):
    if(nums[i] == x):
        print("Element Found at index", i)
        break
    else: 
        print("Finding...")
    i += 1
print("Element to find:", x)

# Tuple use continue statment
numbers = [1,2,3,4,5]
i = 0
while i<= 5 :
    if( i == 3):
        i +=1
        continue #act as skip
    print(i)
    i +=1