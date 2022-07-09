def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0
		
 
""" Sesion 8-E3: Constrúyase un programa while sin macros (ni macro-test), equivalente al siguiente
begin
  X3 := 2;
  while X3 < X2 do
    begin
      X3 := succ(X3);
    end
  X1:=pred(X3)
end
"""

""" SOLUCIÓN
begin
  
  
  
end
"""


# Programa original en Python
def original(X1,X2,X3):
 # begin
 X3 = 2	# X3 := 2;
 while X3 < X2:	# while X3 < X2 do
  # begin
  X3 = succ(X3)	# X3 := succ(X3);
  # end
 X1 = pred(X3)	# X1:=pred(X3)
 # end
 return X1
  

# Añadir tantas variables extra como sean necesarias
def sinMacroTest(X1,X2,X3,...):
 # begin
 
 
 # end
 return X1


# Para probar el programa, invocar el original y el nuevo con 
# el mismo input y comprobar que sale lo mismo
print(original(5,4,7))
print(sinMacroTest(5,4,7,...))

