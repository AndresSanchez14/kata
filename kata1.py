#https://www.md5hashgenerator.com/

def Challenge1(array,S):
    resultado = []
    for num in array:
        string=""
        if(num >= 10):
            carga= num
            while carga>0:
                #print("Carga " + str(carga))
                digito = carga%10
                carga= carga // 10
                if(digito<S):
                    string =string + str(digito)
                    #print(string)
            resultado.append((string[::-1]))       
        elif(num<S):
            resultado.append(num)
    #print("Resultado sin orden: " + str(resultado))
    sizeR= len(resultado)
    contador= sizeR-1
    resultadoOr=[]
    for i in range(0,sizeR):
        resultadoOr.append(resultado[contador])
        contador-= 1
    #print("Resultado con orden: " + str(resultadoOr))    
    #print("Resultado: " + str(list(reversed(resultado))))
    return resultado

#19df669cf9bc136b8e5ec0b7f7c983f5 ---> Andres Sanchez
# mi numero es 1 
S = 1
array = [60, 6, 5, 4, 3, 2, 7, 7, 29, 1]
#array = [1,2,3,4,10707982388,6,7,8]
#array=[10, 20, 30, 40]
#array = [1, 2, 3, 4, 5, 6]
#array= [6, 2, 1]
#array= [66]
#array= [65]
print(Challenge1(array, S))