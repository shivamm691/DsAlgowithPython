# Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)

def pow (a, b):
    if b== 0:
        return 1
    elif b==1 :
        return a
    else:
        result = a*pow(a,b-1)
        return result

a, b = input().split()
a = int(a)
b = int(b)
print(pow(a,b))