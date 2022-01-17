def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
 
""" Sesion 8-E2a: Constrúyanse Programa Whiles sin macro-tests equivalentes a los siguientes
begin
X3:=succ(X1);
while (X1 ≠ X2) ˄ (X3 > X4) do
  begin
      X1:=succ(X1);
      X3:=pred(X3);
  end
end
"""

""" SOLUCIÓN
Expresión aritmética para el test: 


begin


end
"""


# Programa original en Python
def original(X1,X2,X3,X4):
 # begin
 X3 = succ(X1)	# X3:=succ(X1);
 while X1 != X2 and X3 > X4:	# while (X1 ≠ X2) ˄ (X3 > X4) do
  #begin
  X1 = succ(X1)	# X1:=succ(X1);
  X3 = pred(X3)	# X3:=pred(X3);
  # end
 # end
 return X1
  

# Añadir tantas variables extra como sean necesarias
def sinMacroTest(X1,X2,X3,X4,...):
    X3 = succ(X1)
    while(X3 ∸ X4 * (X1 != X2)) != 0):


# Para probar el programa, invocar el original y el nuevo con 
# el mismo input y comprobar que sale lo mismo
print(original(3,5,7,3))
print(sinMacroTest(3,5,7,3,...))

