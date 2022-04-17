def main ():
    my_list = [2, "suup", True, 4.5] ##lista normal
    my_dict = { "firstname": "Richie", "Lastname":"Quiceno"} #diccionario normal

    super_list = [ #This is a list of dictionaries, if I index the first position, I get a dicctionary. 
        { "firstname": "Richie", "Lastname":"Quiceno"},
        { "firstname": "Andres", "Lastname":"Betancur"},
        { "firstname": "maría", "Lastname":"Garavito"},
        { "firstname": "josé", "Lastname":"deFrancisco"}
    ]

    super_dict = { #this is a dictionary of lists, if I index a Key, I will get a list. 
        "natural_nums":[1,2,3,4,5,6],
        "integer_nums": [-1,-2,0,1,2],
        "float_nums": [1.1,1.2,6.58]

    }
  
        
    for key, value in super_dict.items():
        print(key, " " , value)
    
    for x in range(1,len(super_list)):

        print(super_list[x].keys())
def test():
    ml=[1,2,3,4,5]
    mlsqrt= [x*x for x in ml]
    print(mlsqrt)



if __name__=="__main__":
    test()