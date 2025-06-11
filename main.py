
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
    def __init__(self, name, idCh):
        self.name = name
        self.nomAbon = idCh
        self.spisKn = []

class Kniga:
    def __init__(self, nazva, idKn):
        self.nazva = nazva
        self.idKn = idKn
        self.vidanaKomu = 0

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
            print(f'Vi dodali novogo vidviduvacha biblioteki za imyam "{newChitach.name}", yogo abon.nomer {newChitach.nomAbon}.')

    def reestrKn(self):
        nazva = input("Vvedit nazvu knigi: ").strip()
        if len(nazva) < 1:
            print("Nazva ne povynna buty porozhnoiu!")
        else:
            newKniga = Kniga(nazva, self.__nomNewKn)
            self.__spKnig.append(newKniga)
            self.__nomNewKn += 1
            print(f'Vi dodali knigu pid nazvou "{newKniga.nazva}" do biblioteki, ii nomer {newKniga.idKn}.')

    def povernORvidati(self,dia):
        try:
                idAb = int(input("Vvedit id abonenta: "))
                ab = next((a for a in self.__spChit if a.nomAbon == idAb), None)
                if not ab:
                    print(f'Abonement z nomerom {idAb} vidsutniy.')
                else:
                    idKn = int(input("Vvedit id knigi: "))
                    kn = next((kn for kn in self.__spKnig if kn.idKn == idKn), None)
                    if not kn:
                        print(f'Kniga z id {idKn} vidsutna.')
                        return
                    if dia == 'vidati' and kn.vidanaKomu != 0:
                        print(f'Kniga z id {idKn} uzhe vydana.')
                        return
                    else:
                        if dia=='povern':
                            if idKn in ab.spisKn:
                                ab.spisKn.remove(idKn)
                                kn.vidanaKomu = 0
                                print(f'Kniga "{kn.nazva}" z id={kn.idKn} povernuv abonent {ab.name} z id={ab.nomAbon}.')
                            else:
                                print("Abonent ne mae ciei knigi.")
                        elif dia=='vidati':
                            ab.spisKn.append(kn.idKn)
                            kn.vidanaKomu = ab.nomAbon
                            print(f'Kniga "{kn.nazva}" z id={kn.idKn} vidana abonentu {ab.name} z id={ab.nomAbon}.')

        except Exception as e:
            print(f"Pomilka: {e}")

    def stat(self):
        while True:
                print("\nVarianti statistiki:")
                print("1. Pereglanuti zagalnu statistiku")
                print("2. Abonenti z knigami")
                print("3. Exit")

                vib = input("Oberit bazanu diu: ")
                match vib:
                    case "1":
                        print("\nZagalna statistika:")
                        print(f'- zagalna kilkist abonentiv: {len(self.__spChit)}')
                        print(f'- zagalna kilkist knig: {len(self.__spKnig)}')
                        print(f'- kilkist vidanih knig: {len(list(filter(lambda k: k.vidanaKomu != 0, self.__spKnig)))}')
                        print(f'- kilkist knig v nayavn: {len(list(filter(lambda k: k.vidanaKomu == 0, self.__spKnig)))}')
                    case "2":
                        print("\nAbonenti z knigami:")
                        spAb = [ab for ab in self.__spChit if len(ab.spisKn) > 0]
                        for i, ab in enumerate(spAb, start=1):
                            print(f"{i}. {ab.name}. Knigi: {', '.join(kn.nazva for kn in self.__spKnig if kn.idKn in ab.spisKn)}.")
                    case "3":
                        print("Do pobachenna!")
                        break
                    case _:
                        print("Nevirniy nomer.")

def main():
    bib = Bibka()
    while True:
        print("\n=== Menu biblioteki: ===")
        print("1. Zareestruvati chitacha")
        print("2. Zareestruvati knigu")
        print("3. Vidati knigu")
        print("4. Povernenna knigi")
        print("5. Statistika")
        print("6. Exit")

        vib = input("Oberit bazanu diu: ").strip()
        match vib:
            case "1":
                bib.regCh()
            case "2":
                bib.reestrKn()
            case "3":
                bib.povernORvidati('vidati')
            case "4":
                bib.povernORvidati('povern')
            case "5":
                bib.stat()
            case "6":
                print("Do pobachenna!")
                break
            case _:
                print("Nevirniy nomer.")

if __name__ == '__main__':
    main()

# import random
# import time
# import os
# import msvcrt
#
# WIDTH = 20
# HEIGHT = 10
#
# class Kulka:
#     def __init__(self, x):
#         self.x = x
#         self.y = 0
#
#     def Padinna(self):
#         self.y += 1
#
# class Platforma:
#     def __init__(self):
#         self.x = WIDTH // 2
#         self.width = 7
#
#     def vLivo(self):
#         if self.x > 0:
#             self.x -= 1
#
#     def vPravo(self):
#         if self.x + self.width < WIDTH:
#             self.x += 1
#
#     def Roztash(self, x):
#         return self.x <= x < self.x + self.width
#
# class Gra:
#     def __init__(self):
#         self.platform = Platforma()
#         self.kulki = []
#         self.rahunok = 0
#         self.sproba = 3
#         self.shvidk = 0.4
#
#     def stvorKulki(self):
#         x = random.randint(0, WIDTH - 1)
#         self.kulki.append(Kulka(x))
#
#     def onovl(self):
#         os.system("cls" if os.name == "nt" else "clear")
#
#         pole = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
#
#         for kulka in self.kulki:
#             if 0 <= kulka.y < HEIGHT:
#                 pole[kulka.y][kulka.x] = "0"
#
#         for i in range(self.platform.width):
#             px = self.platform.x + i
#             pole[HEIGHT - 1][px] = "="
#
#         for row in pole:
#             print("".join(row))
#         print(f"\nRahunok: {self.rahunok}   Sprob: {self.sproba}")
#
#     def logika(self):
#         for kulka in self.kulki:
#             kulka.Padinna()
#
#         for kulka in self.kulki[:]:
#             if kulka.y == HEIGHT - 1:
#                 if self.platform.Roztash(kulka.x):
#                     self.rahunok += 1
#                 else:
#                     self.sproba -= 1
#                 self.kulki.remove(kulka)
#
#     def get_char(self):
#         if msvcrt.kbhit():
#             return msvcrt.getch().decode('utf-8').lower()
#         return ""
#
#     def proces(self):
#         try:
#             while self.sproba > 0:
#                 if random.random() < 0.3:
#                     self.stvorKulki()
#
#                 self.onovl()
#                 hid = self.get_char()
#
#                 platform_speed = 3 if hid in ("a", "d") else 1
#
#                 if hid == "a":
#                     for _ in range(platform_speed):
#                         self.platform.vLivo()
#                 elif hid == "d":
#                     for _ in range(platform_speed):
#                         self.platform.vPravo()
#
#                 self.logika()
#
#                 self.shvidk = max(0.1, 0.4 - self.rahunok * 0.01)
#                 time.sleep(self.shvidk)
#
#             self.onovl()
#             print("\nKinec gri!")
#             print(f"Vi zibrali: {self.rahunok}")
#         except KeyboardInterrupt:
#             print("\nVihid z gri.")
#
#
# if __name__ == "__main__":
#     game = Gra()
#     game.proces()










