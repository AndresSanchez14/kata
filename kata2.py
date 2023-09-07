#19df669cf9bc136b8e5ec0b7f7c983f5 ---> Andres Sanchez
# mi numero es 1 

def Chll2_POW_Sorted(array,S):
    
    if(len(array)==0):
         #print("El array esta vacio mi amigo")
         return "El array esta vacio mi amigo"
    else:
        limitesup= str(S) + str(S)
        print("Limite sup: " + limitesup)
        resultado =[]
        for num in array:
            #print("Numero al cuadrado: " + str(num**2))
            if (num**2<=int(limitesup)):
                  #print("Voy a agregar este numero a mi array: "+ str(num**2))
                  resultado.append(num**2)  
                  #print("Mi array va asi: " + str(resultado))
        sizeR=len(resultado)
        #print("Tamaño resultado: " + str(sizeR))
        for i in range(sizeR):
            #print("Ciclo Externo: " +  str(i))
            for j in range (0, sizeR-i-1):
                #print("Ciclo interno: " +  str(j))
                if(resultado[j] >resultado[j+1]):
                      #print("Voy a intercarmbiar posiciones de estos valores : " + str(resultado[j]) +" Y este " + str(resultado[j+1]) )
                      #print(resultado)
                      resultado[j],resultado[j+1] = resultado[j+1],resultado[j]
                      #print(resultado)
        #resultado.sort()
        #print("Resultado :"+ str(resultado))
        return resultado

S = 5
#array = [1, 2, 3, 5, 6, 8, 9] # 1 , 4 , 9 ,16 
#array= [-2, -1]
#array = [-10, 10]
#array= []
array=[-6, -5, 0, 5, 6]
print(Chll2_POW_Sorted(array,S))
