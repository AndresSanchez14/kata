
def minCambio(arraym):
  arraym.sort()
  minicambio = 0
  for moneda in arraym:
      
      if(moneda > minicambio + 1): # si es mayor 
          #print("moneda: " + str(moneda))
          #print("Cambio minimo :" + str(minicambio))
          break
      minicambio+=moneda  #sumando el cambio que puedo ir dando   
      #print("El cambio minimo es de momento es : " + str(minicambio))

  return "El cambio minimo que no puedo dar es: " + str(minicambio +1) 



#arraym= [1,2,4]
#arraym = [5, 7, 1, 1, 2, 3, 22]
#arraym = [1, 1, 1, 1, 1]
arraym = [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(minCambio(arraym))
