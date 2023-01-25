class Besök:
    '''Besöksklassen håller information om tiden och datumet för besökaren'''
    def __init__(self, datum, tid):
        self.__datum = datum
        self.__tid = tid

    def getDatum(self):
        månad = self.__datum.split("/")
        return månad[1]

    def getAnkomst(self):
        tid = self.__tid.split("-")
        return tid[0]

    def getLämnar(self):
        tid = self.__tid.split("-")
        return tid[1]