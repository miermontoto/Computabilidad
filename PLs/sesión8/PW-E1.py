def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E1: Construir un PW equivalente a este sin macros
begin
X2:=2;
X5:=0;
while X3!=X5 do
begin
  X2:=X2+X4;
  X3:=pred(X3);
end
X1:=X2;
end
"""

""" SOLUCIÓN:


"""

# Programa original en Python
def original(X1,X2,X3,X4,X5):
 # begin
 X2=2	# X2:=2;
 X5=0	# X5:=0;
 while X3 != X5:	#while X3!=X5 do
  # begin
  X2 = X2 + X4	# X2:=X2+X4;
  X3 = pred(X3)	# X3:=pred(X3);
  # end
  X1 = X2	# X1:=X2;
 # end
 return X1

# Añadir tantas variables extra como sean necesarias
def sinMacros(X1,X2,X3,X4,X5,...):
 # begin



 # end
 return X1


# Para probar el programa, invocar el original y el nuevo con 
# el mismo input y comprobar que sale lo mismo
print(original(1,2,3,4,5))
print(sinMacros(1,2,3,4,5,...))
