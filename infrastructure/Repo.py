from domain.Class import Cucuri

class Repo:
    def __init__(self):
        self.__data = []

    def __str__(self) -> str:
        s=''
        for elem in self.__data:
            s+=str(elem)+"\n"
        return s
    
    def addC(self,name,latime,inaltime,lungime,fertilitate):
        """
        Purpose: add detinator
        """
        if name== None:
            raise ValueError("Invalid")
        if latime<0 or inaltime<0 or lungime<0:
            raise ValueError("Invalid")
        if type(fertilitate)!=bool:
            raise ValueError("Invalid")
        for elem in self.__data:
            if elem.getName() == name:
                raise ValueError("Are cuc deja!!!")
        self.__data.append(Cucuri(name,latime,inaltime,lungime,fertilitate))

    def removeC(self):
        """
        Purpose: sterge nefertilii
        """
        for i in range(len(self.__data)-1,-1,-1):
            if self.__data[i].getFert() == False:
                self.__data.remove(self.__data[i])
            
    def sortC(self):
        """
        Purpose: Sort dupa volum cuc
        """
        return self.__data.sort(key= lambda x:(x.getInaltime()*x.getlatime()*x.getLungime()))

        