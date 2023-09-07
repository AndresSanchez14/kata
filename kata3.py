
def minCambio(arraym):
  arraym.sort()
  minicambio = 1
  for moneda in arraym:
      #print("moneda: " + str(moneda))
      if(moneda > minicambio + 1): 
          
          #print("Cambio minimo :" + str(minicambio))
          break
      minicambio+=moneda   
      #print("El cambio minimo es de momento es : " + str(minicambio))

  return "El cambio minimo que no puedo dar es: " + str(minicambio +1) 



#arraym= [1,2,4]
#arraym = [5, 7, 1, 1, 2, 3, 22]
#arraym = [1, 1, 1, 1, 1]
arraym = [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(minCambio(arraym))
