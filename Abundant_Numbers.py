def is_abundant(n):  
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])  
    return fctr_sum > n  
a = int(input())  
if is_abundant(a):  
    print("True")  
else:  
    print("False")