def reverse(x: int) -> int:
    inputnumber = x.__str__()
    reversedStr = inputnumber[::-1]
    strOriLen = len(reversedStr)
    result = list()
    flag = 1
    for i in range(0, strOriLen):
        if i == (strOriLen -1) and reversedStr[i] == '-' :
            flag = -1
        else:
            result.append(reversedStr[i])
    outputs = ''.join(result)
    outputInt = int(outputs)        
     
    outputInt = outputInt * flag
        
    if outputInt > pow(2,31)-1  or outputInt < -1 * pow(2,31):
        outputInt = 0
        
    return outputInt

print(reverse(134))