# from repositories.kniga_repository import KnigaRepository

class bibl_view():
    @staticmethod
    def start_menu():
        print('\n\tMenu roboti z bibliotekoyu:')
        print('1. Додати нову книгу')
        print('2. Додати нового читача')
        print('3. Вивести всі книги')
        print('4. Відфільтрувати книги за жанром')
        print('5. Видати книгу користувачу')
        print('6. Повернення книги до бібліотеки')
        print('7. Перегляд списку користувачів і книг, які їм видали')
        print('8. Зберегти зміни')
        print('9. Вихід')

    @staticmethod
    def dod_knigu(id_kn):
        print('\nДодавання нової книги:')
        nazva = input("Введіть назву книги: ")
        avtor = input("Введіть автора книги: ")
        try:
            rikVid = int(input("Введіть рік видання: "))
        except ValueError:
            print("Неправильний формат року. Встановлено 0.")
            rikVid = 0
        ganr = input("Введіть жанр книги: ")
        return nazva, avtor, rikVid, ganr, id_kn

    @staticmethod
    def dod_new_chit():
        print('\nДодавання нового читача:')
        return input("Введіть ім'я нового читача: ")

    @staticmethod
    def print_knigi(spis):
        if not spis:
            print("Knigi v biblioteci vidsutni.")
        else:
            for i, kn in enumerate(spis, start=1):
                print(f'{i}. Kniga "{kn.nazva}", avtor: {kn.avtor}, rik vidanna: {kn.rikVid}, ganr: {kn.ganr}, nayavnist: {'v biblioteci' if kn.stat==0 else 'na rukah'}, id knigi = {kn.id_kn}.')

    @staticmethod
    def zapit_ganr():
        return input("Введіть жанр книги: ")

    @staticmethod
    def vid_povern_kn(sp_chit, sp_kn, dia):
        id_kor = input("Vvedit nomer chitackogo biletu: ")
        ab = next((a for a in sp_chit if a.nomChitBil == id_kor), None)
        if not ab:
            print(f'Koristuvac z nomerom {id_kor} vidsutniy.')
            return
        else:
            id_kn = int(input("Vvedit id knigi: "))
            kn = next((kn for kn in sp_kn if kn.id_kn == id_kn), None)
            if not kn:
                print(f'Kniga z id {id_kn} vidsutna.')
                return
            if dia == 'vidati' and kn.stat != 0:
                print(f'Kniga z id {id_kn} uzhe vydana.')
                return
            else:
                if dia == 'povern':
                    if id_kn in ab.spis:
                        return ab, kn, dia
                    else:
                        print("Abonent ne mae ciei knigi.")
                        return
                elif dia == 'vidati':
                    return ab, kn, dia
                else:
                    print("Невідома дія. Вкажіть 'vidati' або 'povern'.")

    @staticmethod
    def per_kor(sp_chit, sp_kn):
        print("\nKoristuvaci biblioteki:")
        for i, ab in enumerate(sp_chit, start=1):
            print(f"{i}. Koristuvac: {ab.ima}, nomer chit. biletu: {ab.nomChitBil},")
            print(f"\tknigi: {', '.join(kn.nazva for kn in sp_kn if kn.id_kn in ab.spis)}.")

    @staticmethod
    def zber_zm():
        print('Zmini zberezeni!')

    @staticmethod
    def vihid():
        print('Do pobacenna!\nPrograma zaversila svoyu robotu!')

    @staticmethod
    def show_message(message):
        print(message)