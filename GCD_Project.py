num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

gcd = 0

def GCD (num1, num2):
    while num1:
        if num1 % num2 == 0 :
            gcd = num2
            break
        else:
            num3 = num1 % num2
            num1 = num2
            num2 = num3
    return gcd

print()

print(f"GCD({num1},{num2}): ", GCD(num1, num2))
            
            
            
        
