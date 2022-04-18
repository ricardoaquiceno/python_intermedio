def read():
    #read all
    numbers = []
    with open("./numbers.txt", "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Richie","Mango","Majo"]
    with open("./names.txt","w",encoding="utf-8") as y:
        for i in names:
            y.write(i+"\n")
        print("done")



def main():
    read()
    write()


if __name__=="__main__":
    main()