class Cucuri:
    def __init__(self, name:str, latime:float,inaltime:float,lungime:float,fert:bool ):
        self.__name = name
        self.__latime = latime
        self.__inaltime = inaltime
        self.__lungime = lungime
        self.__fert = fert

    def getName(self):
        return self.__name
    def getlatime(self):
        return self.__latime
    def getInaltime(self):
        return self.__inaltime
    def getLungime(self):
        return self.__lungime
    def getFert(self):
        return self.__fert
    
    def __str__(self) -> str:
        return "Detinator: "+self.__name+" Latime: "+str(self.__latime)+" Inaltime: "+str(self.__inaltime)+" Lungime: "+str(self.__lungime)+" Fertilitate: "+str(self.__fert)
    def __repr__(self) -> str:
        return str(self)
        