class Djur:
    ''' Djurklassen håller informationen och djuren olika tider för att senare kunna 
    jämföra med besökarens tider '''
    def __init__(self, namn, vakenTid, matningsTid, ide=False):
        ''' Lagrar tid för ide, när djuret är vaket och tid för matning'''
        self.__namn = namn
        self.__vakenTid = vakenTid
        self.__matningsTid = matningsTid 
        self.__ide = ide

    def skrivUt(self):
        '''Skriver ut nanet på djuret och ifall djurets matningstid infaller med besöket skrivs även det ut'''
        return self.__namn + "\t--   matas vid:" + self.__matningsTid + "  --\t" 

    def getVakna(self):
        vaknar = self.__vakenTid.split("-")
        return vaknar[0]

    def getDjur(self):
        return self.__namn

    def getMat(self):
        return self.__matningsTid

    def getIde(self):
        return self.__ide