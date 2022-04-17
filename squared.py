import math

def main():
   #lista de todos los números de 1-100 al cuadrado
   #lista de todos los numeros de 1-100 al cuadrado que no sean divisibles por 3
   squares=[]
   non_div_3=[]
   for i in range(1,101):
       squares.append(i**2)
       if (i**2%3!=0):
           non_div_3.append(i**2)
#   print(squares)
#   print(non_div_3)
   reto=[x for x in range(1,100000) if x%4==0 and x%6==0 and x%9==0 and x<99999]
   print(reto)

if __name__=="__main__":
    main()