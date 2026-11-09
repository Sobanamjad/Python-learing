def cal_sum(a ,b):
    sum = a + b
    print(sum)
    return sum

cal_sum(5, 10)
cal_sum(10, 56)

# Lenght of a list in function
list = [1,2,3,4,5,6,7,8,9,10]
def print_len(li):
    print(len(li))
print_len(list)

#use function to print in single line 
def single_line(list):
    for item in list:
        print(item, end=" ")

single_line(list)

#convert dollar to ruppes
def converter(usd_val):
    PKR = usd_val * 280
    print(usd_val, "USD = " ,PKR , "PKR")

converter(12)