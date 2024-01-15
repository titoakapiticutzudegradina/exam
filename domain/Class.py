class Restourant:
    def __init__(self,id:int, name:str, tema:str,rating:int):
        self.__id = id
        self.__name = name
        self.__tema = tema
        self.__rating = rating

    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getTema(self):
        return self.__tema
    def getRating(self):
        return self.__rating
        
    def setId(self,id):
        self.__id = id
    def setName(self,name):
        self.__name = name
    def setTema(self,tema):
        self.__tema = tema
    def setRating(self,raiting):
        self.__rating = raiting

    def __str__(self) -> str:
        return "Id: " + str(self.__id) + " Name:  "+self.__name + " Tema: "+ self.__tema + " Rating: "+ str(self.__rating)
    def __repr__(self) -> str:
        return str(self)