
def minCambio(arraym):
  arraym.sort()
  minchange = 0
  for coin in arraym:
      #print("moneda: " + str(moneda))
      if(coin > minchange + 1): 
          
          #print("Cambio minimo :" + str(minchange))
          break
      minchange+=coin   
      #print("El cambio minimo es de momento es : " + str(minchange))

  return "El cambio minimo que no puedo dar es: " + str(minchange +1) 



#arraym= [1,2,4]
#arraym = [5, 7, 1, 1, 2, 3, 22]
#arraym = [1, 1, 1, 1, 1]
#arraym = [1, 5, 1, 1, 1, 10, 15, 20, 100]
arraym = [2,3,4,5]
print(minCambio(arraym))
