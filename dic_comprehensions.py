def main():
    dict= { x:x**3 for x in range(1,101) if x**3%3!=0 }
    for keys,values in dict.items():
        print(keys, " ", values)
    print(dict)
    #crear un diccionario cuyas llaves sean los primeros 1000 numeros naturales y sus valores sean sus raíces cuadradas
    reto={ y: round(y**(1/2),2) for y in range(1,1001) }
    print(reto)
if __name__ == "__main__":
    main()
