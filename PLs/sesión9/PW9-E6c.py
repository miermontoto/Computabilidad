def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
		
""" PW-E6-c): Construir un PW que compute f(X,Y)=Y div (X mod Y). 
Utilizar el resultado del ejercicio 4c por composición y un programa que calcule x div y. Se permiten macros. """

"""
Programa While para el módulo
begin
 X1 := succ(X1) 
 while X1 != X4 do
 begin
  X3 := succ(X1)
  X3 := pred(X3)
  X5 := 0
  while X5 != X2 do
  begin
   X1 := pred(X1);
   X5 := succ(X5)
  end
 end
 X1 := pred(X3)
 end
"""

# Pasar a f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(...):


    return X1

def div_mod(X,Y):
  return print(pw(X,Y,....))


# Para probar el programa, invocar div_mod
# Probar que sucede para varios valores de X e Y: 0, 1, 2, ...
# Probar que cuando Y==0 --> Indeterminacion
div_mod(....)	


