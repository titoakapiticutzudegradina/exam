from domain.Class import Restourant

class Repo:
    def __init__(self):
        self.__data=[]

    def __str__(self):
        s= ''
        for elem in self.__data:
            s+= str(elem)+ "\n"
        return s
    def addF(self,id,name,tema,rating):
        """
        Purpose: Add a restaurant to the list
        """
        if id == None or name == None or tema == None or rating == None:
            raise ValueError ("Invalid")
        if tema not in ["italian","unguresc","taranesc","american","sobolanesc"]:
            raise ValueError ("Invalid")
        if rating<0 and rating>5:
            raise ValueError ("Invalid")
        for elem in self.__data:
            if elem.getId() == id:
                raise ValueError ("Already here")
        self.__data.append(Restourant(id,name,tema,rating))

    def removeF(self,raiting):
        """
        Purpose: Removes restaurants if rating under a given value
        """
        for i in range(len(self.__data)-1,-1,-1):
            if self.__data[i].getRating() < raiting:
                self.__data.remove(self.__data[i])

    def getF(self, tema):
        """
        Purpose: Gets all restaurants w given tema, alphabetical
        """
        result = []
        if tema not in ["italian","unguresc","taranesc","american","sobolanesc"]:
            raise ValueError ("Invalid")
        for elem in self.__data:
            if elem.getTema() == tema:
                result.append(elem)
        result.sort(key=lambda x:x.getName(),reverse=False)
        return result
        
        
        