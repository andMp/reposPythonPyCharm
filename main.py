
# написать To-Do List с CRUD архитектурой и записем и чтением  с файла)

# robFile = "spisokSprav.txt"
# def zavant():
#     zavd =[]
#     try:
#         with open(robFile,"r",encoding="utf-8") as f:
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     p = line.split(" ===== ")
#                     if len(p) == 2:
#                         zavd.append({"Zagolovok": p[0],"Poyasnenna": p[1]})
#     except FileNotFoundError:
#         pass
#     return zavd
#
# def zberZavd(zavd):
#     with open(robFile,"w",encoding="utf-8") as f:
#         for zav in zavd:
#             f.write(f"{zav['Zagolovok']} ===== {zav['Poyasnenna']}\n")
#
# def dodZ(zavd):
#     zag = input("Nazva zavd: ")
#     opis = input("Opis zavd: ")
#     zavd.append({"Zagolovok":zag, "Poyasnenna":opis})
#     zberZavd(zavd)
#     print("Zavdanna dodano.")
#
# def pereglad(zavd):
#     print()
#     if not zavd:
#         print("Zavdanna vidsutni!")
#     else:
#         for i, zav in enumerate(zavd, start=1):
#             print(f"{i}. {zav['Zagolovok']} - {zav['Poyasnenna']}")
#
# def onovl(zavd):
#     pereglad(zavd)
#     try:
#         ind = int(input("Vvedit nomer zavd. dla yogo redaguvanna: ")) - 1
#         if 0<=ind<len(zavd):
#             Zagolovok = input("Nova nazva (shob ne zmin, zaliste poroznim): ")
#             Poyasnenna = input("Opis zavd (shob ne zmin, zaliste poroznim): ")
#             if Zagolovok:
#                 zavd[ind]["Zagolovok"] = Zagolovok
#             if Poyasnenna:
#                 zavd[ind]["Poyasnenna"] = Poyasnenna
#             zberZavd(zavd)
#             print("Zavdanna onovleno.")
#         else:
#             print("Nevirniy nomer.")
#     except ValueError:
#         print("Vvedit virniy nomer.")
#
# def vidal(zavd):
#     pereglad(zavd)
#     try:
#         ind = int(input("Vvedit nomer zavd. dla yogo vidalenna: ")) - 1
#         if 0<=ind<len(zavd):
#             vid = zavd.pop(ind)
#             zberZavd(zavd)
#             print(f"Zavdanna '{vid['Zagolovok']}' vidaleno.")
#         else:
#             print("Nevirniy nomer.")
#     except ValueError:
#         print("Vvedit virniy nomer.")
#
# def main():
#     zavd = zavant()
#     while True:
#         print("\n=== Menu roboti z zavd: ===")
#         print("1. Pereglanuti vsi zavd")
#         print("2. Dodati zavd")
#         print("3. Redaguvati zavd")
#         print("4. Vidaliti zavd")
#         print("5. Exit")
#         vib = input("Oberit bazanu diu: ")
#
#         match vib:
#             case "1":
#                 pereglad(zavd)
#             case "2":
#                 dodZ(zavd)
#             case "3":
#                 onovl(zavd)
#             case "4":
#                 vidal(zavd)
#             case "5":
#                 print("Do pobachenna!")
#                 break
#             case _:
#                 print("Nevirniy nomer.")
#
#
# if __name__ == "__main__":
#     main()





# Написать консольное приложение для управления библиотекой. CRUD, регистрировать читателей,
# оформлять и возвращать книги и просматривать статистику
# (кто взял, кто вернул, кто не вернул, какие книги есть в наличии в каком количестве)
class Chitach:
    def __init__(self, name, id):
        self.name = name
        self.nomAbon = id
        self.spisKn = []

class Kniga:
    def __init__(self, nazva, id):
        self.nazva = nazva
        self.id = id
        self.nayavn = 0

class Bibka:
    def __init__(self):
        self.__spKnig = []
        self.__spChit = []
        self.__nomNewAb = 1
        self.__nomNewKn = 1

    def regCh(self):
        name = input("Введіть ім'я нового відвідувача: ").strip()
        if len(name) < 1:
            print("Ima ne povynna buty porozhnoiu!")
        else:
            newChitach = Chitach(name, self.__nomNewAb)
            self.__spChit.append(newChitach)
            self.__nomNewAb += 1
            print(f'Vi dodali novogo vidviduvacha biblioteki za imam "{newChitach.name}", yogo abon.nomer {newChitach.nomAbon}.')

    def reestrKn(self):
        nazva = input("Vvedit nazvu knigi: ").strip()
        if len(nazva) < 1:
            print("Nazva ne povynna buty porozhnoiu!")
        else:
            newKniga = Kniga(nazva, self.__nomNewKn)
            self.__spKnig.append(newKniga)
            self.__nomNewKn += 1
            print(f'Vi dodali knigu pid nazvou "{newKniga.nazva}" do biblioteki, ii nomer {newKniga.id}.')

    def vidatiKn(self):
        try:
            while True:
                idAb = input("Vvedit id abonenta: ")
                ab = [ab for ab in self.__spChit if ab.self.nomAbon == idAb]
                if not ab:
                    print(f'Abonement z nomerom {idAb} visutniy.')
                else:
                    idKn = input("Vvedit id knigi: ")
                    kn = [kn for kn in self.__spKnig if kn.self.id == idKn]
                    if not kn:
                        print(f'Kniga z id {idKn} visutna.')
                    else:
                        ab.spisKn.append(kn.self.id)
                        kn.self.nayavn = ab.self.nomAbon
                        print(f'Kniga "{kn.self.nazva}" z id={kn.self.id} vidana abonentu {ab.self.name} z id={ab.self.nomAbon}.')
        except:
            print("Pomilka!")

    def povernKn(self):
        try:
            while True:
                idAb = input("Vvedit id abonenta: ")
                ab = [ab for ab in self.__spChit if ab.self.nomAbon == idAb]
                if not ab:
                    print(f'Abonement z nomerom {idAb} visutniy.')
                else:
                    idKn = input("Vvedit id knigi: ")
                    kn = [kn for kn in self.__spKnig if kn.self.id == idKn]
                    if not kn:
                        print(f'Kniga z id {idKn} visutna.')
                    else:
                        ab.spisKn.remove(idKn)
                        kn.self.nayavn = 0
                        print(f'Kniga "{kn.self.nazva}" z id={kn.self.id} povernuv abonent {ab.self.name} z id={ab.self.nomAbon}.')
        except:
            print("Pomilka!")

    def stat(self):
        while True:
            print("\nZagalna statistika:")
            print(f'- zagalna kilkist abonentiv: {len.self.__spChit}')
            print(f'- zagalna kilkist abonentiv: {len.self.__spKnig}')
            print(f'- kilkist vidanih knig: {len.list(filter(lambda k: k.nayavn != 0, self.__spKnig))}')
            print(f'- kilkist knig v nayavn: {len.list(filter(lambda k: k.nayavn == 0, self.__spKnig))}')


                print("\nVarianti statistiki:")
                print("1. Pereglanuti zagalnu statistiku")
                print("2. Abonenti z knigami")
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


if __name__ == '__main__':
    main()








