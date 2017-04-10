equation = "y= 2+6+45"

def bite(equation):
    text = equation[2:].replace(" ","")
    split = text.split("+")

    result = 0
    for i in split:
        result = result + int(i)

    return result

print(equation)        
print(bite(equation))
    
