num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

GCD = 0

def GCD (num1, num2):
    while num1:
        if num1 % num2 == 0 :
            GCD = num2
            break
        else:
            num3 = num1 % num2
            num1 = num2
            num2 = num3
    return GCD

print()

print(f"GCD({num1},{num2}): ", GCD(num1, num2))
            
            
            
        
