#19df669cf9bc136b8e5ec0b7f7c983f5 ---> Andres Sanchez
# mi numero es 1 

def Chll2_POW_Sorted(array,S):
    
    if(len(array)==0):
         #print("El array esta vacio mi amigo")
         return "El array esta vacio mi amigo"
    else:
        limitsup= str(S) + str(S)
        print("Limite sup: " + limitsup)
        Result =[]
        for num in array:
            #print("Numero al cuadrado: " + str(num**2))
            if (num**2<=int(limitsup)):
                  #print("Voy a agregar este numero a mi array: "+ str(num**2))
                  Result.append(num**2)  
                  #print("Mi array va asi: " + str(Result))
        sizeR=len(Result)
        #print("Tamaño Result: " + str(sizeR))
        for i in range(sizeR):
            #print("Ciclo Externo: " +  str(i))
            for j in range (0, sizeR-i-1):
                #print("Ciclo interno: " +  str(j))
                if(Result[j] >Result[j+1]):
                      #print("Voy a intercarmbiar posiciones de estos valores : " + str(Result[j]) +" Y este " + str(Result[j+1]) )
                      #print(Result)
                      Result[j],Result[j+1] = Result[j+1],Result[j]
                      #print(Result)
        #Result.sort()
        #print("Result :"+ str(Result))
        return Result

S = 5
#array = [1, 2, 3, 5, 6, 8, 9] # 1 , 4 , 9 ,16 
#array= [-2, -1]
#array = [-10, 10]
#array= []
array=[-6, -5, 0, 5, 6]
print(Chll2_POW_Sorted(array,S))
