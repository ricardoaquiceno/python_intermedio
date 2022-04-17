from unicodedata import name


DATA = [ #esto es una constante, cuando está en mayúsculas es porque es constante
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def main():
    #A function to get the names of the people that master python with lamba accessing in 2 different ways to the dicctionary
    all_py_dev= list(map(lambda x : x["name"],list(filter(lambda x : x.get("language")=='python',DATA))))
    print(all_py_dev)
    #A function to bring all Platzi workers with Lambda
    all_platzi_lambda= list(map(lambda x: x["name"],list(filter(lambda x : x["organization"]=="Platzi",DATA))))
    print(all_platzi_lambda)
    #A function that brings all the adults
    all_adults=list(filter(lambda x : x["age"]>=18,DATA))
    print(all_adults)
    #A function to get the names of the people that master python comprehension
    py_devs=[worker["name"] for worker in DATA if worker["language"]=="python"]
    print(py_devs)
    #A function to bring all Platzi workers with comprehension
    all_platzi_comp=[x["name"] for x in DATA if x["organization"]=="Platzi"]
    print (all_platzi_comp)
    #a fuction that adds true if someone is older than 70Yo or false if not
    old= list(map(lambda x : x | {"old":x["age"]>70},DATA)) #here we are using a pipe operator "|" to add dictionaries, this is from V3.9 
    print(old)



if __name__=="__main__":
    main()