def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
		
""" Sesion 8-E2b: Constrúyanse Programas While sin macro-tests equivalentes a los siguientes
begin
X1:=succ(X1);
while (X1 ≤ X2) v (X3 < X1) do
  begin
      X1:=pred(X1);
      X2:=pred(X2);
  end
end
"""

""" SOLUCIÓN
Expresión aritmética para el test: 

begin


end
"""


# Programa original en Python
def original(X1,X2,X3):
 X1 = succ(X1)	# X1:=succ(X1);
 while X1 <= X2 or X3 < X1:	# while (X1 ≤ X2) v (X3 < X1) do
  # begin
  X1 = pred(X1)	# X1:=pred(X1);
  X2 = pred(X2)	# X2:=pred(X2);
  # end
 # end
 return X1
  

# Añadir tantas variables extra como sean necesarias
def sinMacroTest(X1,X2,X3,...):
 # begin
 
 # end
 return X1

# Para probar el programa, invocar el original y el nuevo con 
# el mismo input y comprobar que sale lo mismo
print(original(5,4,3))
print(sinMacroTest(5,4,3,...))

