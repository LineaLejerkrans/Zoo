'''Importera klasserna från klassfilen'''
from djurKlass import Djur
from besökKlass import Besök

''' Läser in informationen från filen'''
def läsFil():
    f = open("djur.txt", "r")
    lista = f.readlines()
    f.close()

    lista.pop(0) # tar bort första elementet i listan
    läsLista = []
    for i in range(len(lista)):
        rad = str(lista[i]).replace("\n", "")
        if len(rad.split("/")) != 4: # ifall det inte finns 4 /-tecken i txtfilen är den raden felskriven och läses inte in
            print("Rad " + str(i+2) + " är felaktig, skippar")
            continue
        läsLista.append(rad) #lägger tillbaka strängen 

    return läsLista 


'''Skapar objekt med informationen från filen'''
def skapaObj(lista, datum, tid):
    for i in range(len(lista)):
        djurInfo = lista[i].split("/") #unik lista för varje djur 
        djur = Djur(djurInfo[0], djurInfo[1], djurInfo[2], djurInfo[3]) #skapar objektet med de olika positionerna från listan som attribut
        lista[i] = djur #lista med djurobjekten

    besökare = Besök(datum, tid) #skapar besöksobjektet

    return lista, besökare
                    

'''Skirver ut relevanta frågor till användaren och läser in svaret'''
'''felkontroll för all inmatning'''
def frågor():
    datum = input("Vilket datum vill du besöka zooet? (dd/mm) ")
    månadsMap = {1:31, 2:29, 3:31, 4:30, 5:31, 6: 30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} #skapar en map för de olika månaderna och hur många dagar de innehåller var 
 
    while True:
        while True:
            try:
                dat = datum.split("/")
                if len(dat) == 2:
                    int(dat[0]) # går det inte att konvertera till siffra är något fel
                    int(dat[1])
                else:
                    raise Exception # om dat inte innehåller 2 posistioner har användaren inte skrivit in något innan "/" och något efter, då är det fel
                break # går if villkoret igenom är allt rätt och loopen bryts
                
            except Exception:
                datum = input("Skriv enligt formatet dd/mm ")

        try:
            dat = datum.split("/")
            maxDag = månadsMap.get(int(dat[1])) # hämtar den andra positionen i dat som är månaden, för att få hur många dagar den månaden har 
            if maxDag == None: # fanns inte i mapen alltså existerar inte månaden
                print("Skriv gilltig månad 1-12 ")
                raise ValueError
            if int(dat[0]) < 1 or int(dat[0]) > maxDag: # skriver man en dag som är mindre än 1 eller större än de antalet dagar som finns i den månaden, så blir det fel
                print("Skriv gilltig dag 1-" + str(maxDag))
                raise ValueError
            break # om allt är rätt bryts loopen

        except ValueError:
            datum = input("Skriv igen ")

    print("Zoot är öppet från 06-23")
    tid = input("Vilken tid vill du komma? (hh-hh)")

    while True:
        while True:
            try:
                ti = tid.split("-") # kollar så det finns ett "-" i svaret
                if len(ti) == 2: # kollar att listan innehåller 2 positioner
                    int(ti[0]) # kollar att de är siffror
                    int(ti[1])
                else:
                    raise Exception
                break

            except Exception: # blir något fel skrivs meddelandet ut
                tid = input("Skriv enligt formatet hh-hh ")

        if int(tid.split("-")[0]) < 25 and int(tid.split("-")[0]) > -1 and int(tid.split("-")[1]) < 25 and int(tid.split("-")[1]) > -1: #kollar att den inmatade tiden existerar
            if int(tid.split("-")[0]) > 5 and int(tid.split("-")[1]) < 24: #kollar om tiden ligger innom zooets öppettider
                if int(tid.split("-")[0]) < int(tid.split("-")[1]): # kollar att ankomsttiden är mindre än avfärdstiden
                    break
                else: 
                    tid = input("Skriv din avfärd efter din ankomst: ")
            else:
                tid = input("Våra öppettider är 06-23, skriv en ny tid: ")
        else:
            tid = input("Skriv en tid mellan 00-24: ")
    
    return datum, tid


'''jämför djurobjektns tider med användarens tider och skriver ut de'''
def jämför(lista, besökare):
    print("Under ditt besök kan du förväntas se: ")
    for i in range(len(lista)): #djurlistan
        if int(lista[i].getVakna()) < int(besökare.getAnkomst()) or int(lista[i].getVakna()) < int(besökare.getLämnar()): # djuret är vaken innan besökaren ankommer eller vaknar innan besökaren lämnar
            if lista[i].getIde().strip() == "vinter": 
                if int(besökare.getMånad()) > 3 and int(besökare.getMånad()) < 11: # om djuret är i ide men besökare kommer under sommaren skrivs djuret ut 
                    skrivUt(i, lista, besökare)
                        
            elif lista[i].getIde().strip() == "sommar":
                if int(besökare.getMånad()) < 5 or int(besökare.getMånad()) > 8: # om djuret är i ide på sommaren men besökaren ankommer på vintern skrivs djuret ut 
                    skrivUt(i, lista, besökare)           
                    
            else: # om djuret inte har ett ide skrivs det alltid ut 
                skrivUt(i, lista, besökare)


"skriver ut djuren ifall de uppfyller villkoren"
def skrivUt(i, lista, besökare):
    if int(lista[i].getMat()) >= int(besökare.getAnkomst()) and int(lista[i].getMat()) < int(besökare.getLämnar()):
        print(lista[i].skrivUt()) # om djuret matas under besökarens tid
    else:
        print(lista[i].getDjur()) # om djuret inte matas under besökarens tid


"main funktionen som anropar de olika funktionerna"
def main():
    while True:
        filLista = läsFil() #information från textfilen fås genom anrop av läsFilen funktioen
        datum, tid = frågor() #datum och tid fås från frågor funktionen

        lista, besökare = skapaObj(filLista, datum, tid) #objekts listan som innehåller djuren, och besöksobjektet
        jämför(lista, besökare) # jämför-funktionen anropas, denna funktion retunerar inget eftersom utskriften sker i funktionen
        svar = input("Vill du köra programmet igen? ja/nej? ")
        if svar.lower() != "ja": # svarar användaren något annat än "ja" avslutas programmet
            break

main() #startar programmet