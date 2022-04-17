def main():
    pal=lambda x: x==x[::-1]
    y=pal("ana")
    print(y)
    print(type(y))
#example of high order function filter
    mylist=[1,4,5,6,9,13,19,21]
    sqrt=list(filter(lambda x: x**2, mylist))#this passess each value of mylist as a parameter for the function
    print (sqrt)
if __name__=="__main__":
    main()