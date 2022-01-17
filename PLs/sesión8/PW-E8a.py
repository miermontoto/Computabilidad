def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

"""
Programa While para el factorial:
------------------
begin
 X2 := 1;
 X3 := 1;
 while X3 != X1 do
 begin
  X3 = succ(X3);
  X2 = X2 * X3;
 end
 X1 := X2;
end
"""
		
""" PW-E8-a): Construir un PW que compute f(X)=sum_i=0..X(i!). 
Utilizar el resultado del ejercicio 4c por composición. Se permiten macros. """
# Pasar a f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(...):


    return X1

def sum_fact(X):
  return print(pw(X,...))


# Para probar el programa, invocar a sum_fact	
# Probar que sucede para varios valores de X: 0, 1, 2, ...
sum_fact(...)	



