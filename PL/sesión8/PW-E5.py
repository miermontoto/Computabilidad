def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0

""" PW-E5: Construyase un programa while equivalente a la siguiente sentencia. 
Las unicas macros permitidas son los macro test
if X1!=X2 then
    X1 := X1+X2
else
	X1 := 0
"""

""" SOLUCIÓN


"""

# Programa original en Python
def original(X1,X2):
 # begin 
 if X1 != X2:	# if X1!=X2 then
  X1 = X1 + X2	# X1 := X1 + X2
 else:	# else
  X1 = 0	# X1 := 0
 # end
 return X1
  

# Añadir tantas variables extra como sean necesarias
def sinMacro(X1,X2,...):
 # begin
 
 
 return X1

# Para probar el programa, invocar el original y el nuevo con 
# el mismo input y comprobar que sale lo mismo
print(original(5,4))
print(sinMacro(5,4,...))
print(original(3,3))
print(sinMacro(3,3,...))