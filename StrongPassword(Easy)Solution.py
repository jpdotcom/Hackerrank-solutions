def condition_satisfier(condition,password):
    x=0
    for letter in password:
        for conditions in condition:
            if letter!=conditions:
                x+=1
    if x==len(condition)*len(password):
        return False
    return True
def minimumNumber(n, password):
    addition=0   
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    con_1=condition_satisfier(numbers,password)
    con_2=condition_satisfier(lower_case,password)
    con_3=condition_satisfier(upper_case,password)
    con_4=condition_satisfier(special_characters,password)
    if not con_1:
        addition+=1
    if not con_2:
        addition+=1
    if not con_3:
        addition+=1
    if not con_4:
        addition+=1

    if n+addition<6:
        addition+=6-(n+addition)
    return addition


password="Ab1"
n=len(password)
print(minimumNumber(n,password))
    
