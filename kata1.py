#https://www.md5hashgenerator.com/

def Challenge1(array,S):
    Result = []
    for num in array:
        string=""
        if(num >= 10):
            carry= num
            while carry>0:
                #print("Carga " + str(carry))
                digit = carry%10
                #print("Digito :" + str(digit))
                carry= carry // 10
                if(digit<S):
                    string =string + str(digit)
                    #print(string)
            Result.append((string[::-1]))       
        elif(num<S):
            Result.append(num)
    #print("Result sin orden: " + str(Result))
    sizeR= len(Result)
    iterator= sizeR-1
    resultSort=[]
    for i in range(0,sizeR):
        resultSort.append(Result[iterator])
        iterator-= 1
    #print("Result con orden: " + str(resultSort))    
    #print("Result: " + str(list(reversed(resultSort))))
    return resultSort

#19df669cf9bc136b8e5ec0b7f7c983f5 ---> Andres Sanchez
# mi numero es 1 
S = 5
array = [60, 6, 5, 4, 3, 2, 7, 7, 29, 1]
#array = [1,2,3,4,10707982388,6,7,8]
#array=[10, 20, 30, 40]
#array = [1, 2, 3, 4, 5, 6]
#array= [6, 2, 1]
#array= [66]
#array= [65]
print(Challenge1(array, S))