
# написать To-Do List с CRUD архитектурой и записем и чтением  с файла)

robFile = "spisokSprav.txt"
def zavant():
    zavd =[]
    try:
        with open(robFile,"r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    p = line.split(" ===== ")
                    if len(p) == 2:
                        zavd.append({"Zagolovok": p[0],"Poyasnenna": p[1]})
    except FileNotFoundError:
        pass
    return zavd

def zberZavd(zavd):
    with open(robFile,"w",encoding="utf-8") as f:
        for zav in zavd:
            f.write(f"{zav['Zagolovok']} ===== {zav['Poyasnenna']}\n")

def dodZ(zavd):
    zag = input("Nazva zavd: ")
    opis = input("Opis zavd: ")
    zavd.append({"Zagolovok":zag, "Poyasnenna":opis})
    zberZavd(zavd)
    print("Zavdanna dodano.")

def pereglad(zavd):
    print()
    if not zavd:
        print("Zavdanna vidsutni!")
    else:
        for i, zav in enumerate(zavd, start=1):
            print(f"{i}. {zav['Zagolovok']} - {zav['Poyasnenna']}")

def onovl(zavd):
    pereglad(zavd)
    try:
        ind = int(input("Vvedit nomer zavd. dla yogo redaguvanna: ")) - 1
        if 0<=ind<len(zavd):
            Zagolovok = input("Nova nazva (shob ne zmin, zaliste poroznim): ")
            Poyasnenna = input("Opis zavd (shob ne zmin, zaliste poroznim): ")
            if Zagolovok:
                zavd[ind]["Zagolovok"] = Zagolovok
            if Poyasnenna:
                zavd[ind]["Poyasnenna"] = Poyasnenna
            zberZavd(zavd)
            print("Zavdanna onovleno.")
        else:
            print("Nevirniy nomer.")
    except ValueError:
        print("Vvedit virniy nomer.")

def vidal(zavd):
    pereglad(zavd)
    try:
        ind = int(input("Vvedit nomer zavd. dla yogo vidalenna: ")) - 1
        if 0<=ind<len(zavd):
            vid = zavd.pop(ind)
            zberZavd(zavd)
            print(f"Zavdanna '{vid['Zagolovok']}' vidaleno.")
        else:
            print("Nevirniy nomer.")
    except ValueError:
        print("Vvedit virniy nomer.")

def main():
    zavd = zavant()
    while True:
        print("\n=== Menu roboti z zavd: ===")
        print("1. Pereglanuti vsi zavd")
        print("2. Dodati zavd")
        print("3. Redaguvati zavd")
        print("4. Vidaliti zavd")
        print("5. Exit")
        vib = input("Oberit bazanu diu: ")

        match vib:
            case "1":
                pereglad(zavd)
            case "2":
                dodZ(zavd)
            case "3":
                onovl(zavd)
            case "4":
                vidal(zavd)
            case "5":
                print("Do pobachenna!")
                break
            case _:
                print("Nevirniy nomer.")


if __name__ == "__main__":
    main()





# Написать консольное приложение для управления библиотекой. CRUD, регистрировать читателей,
# оформлять и возвращать книги и просматривать статистику
# (кто взял, кто вернул, кто не вернул, какие книги есть в наличии в каком количестве)
# class Chitach:
#     def __init__(self, name):
#         self.name = name
#         self.spis = []
#
# class Kniga:
#     def __init__(self, nazva):
#         self.nazva = nazva
#         self.nayavn = 'nemaE'
#
# class Bibka:
#     def __init__(self):
#         self.__spKnig = []
#         self.__spChit = []
#     def regCh(self,name):
#         self.__spChit.append(Chitach(name))
#     def reestrKn(self, nazva):
#         self.__spKnig.append(Kniga(nazva))
#     def vidKn(self, nazvaKn, priz):
#         try:
#             if self.__spKnig.count(Kniga.nazva===nazvaKn):
#                 if :
#
#             else:
#                 print(f"Kniga {nazvaKn} vidsutna в нашій бібліотеці.")
#         except:
#             print("Якась помилка, якщо цікаво розбирайся.")









