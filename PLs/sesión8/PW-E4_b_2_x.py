def succ(Z):
    return Z + 1
def pred(Z): 
    if Z >= 1:
        return Z - 1
    else:
        return 0


""" Sesion 8-E4-b): Construir un PW que compute f(X)=2^X. Empleando macros: suma y asignacion """
# Pasar f como argumento las k varibles (X1, X2, ...Xk)  del programa while k variables construido
def pw(X1):
  X2 = 0
  X3 = 2
  while X1 != X2:
    while X2 != X3:
        X3 = X3 + X3
        X2 = succ(X2)
    X1 = succ(X1)
    X2 = 0
  X1 = succ(X3)
  X1 = pred(X3)
  return X1


def doselevX(X):
  return print(pw(X,...))

# Para probar el programa, invocar a doselevX
doselevX(3)
