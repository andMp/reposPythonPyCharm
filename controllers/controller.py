from views.bibl_view import bibl_view
from models.Kniga import Kniga
from models.Koristuvac import Koristuvac
from repositories.kniga_repository import KnigaRepository
from repositories.chitach_repository import KoristuvacRepository

class Biblioteka_controller:
    def __init__(self, view):
        self.kniga_repo=KnigaRepository()
        self.chitac_repo=KoristuvacRepository()
        self.view = view

        self.sp_kn = self.kniga_repo.zavant_z_file()
        self.sp_kor = self.chitac_repo.zavant_z_file()

        self.id_new_kor = len(self.sp_kor) + 1
        self.id_new_kn = len(self.sp_kn) + 1

    def run(self):
        while True:
            self.view.start_menu()
            var = input('Оберіть бажану дію:')
            match var:
                case '1':
                    kortez = self.view.dod_knigu(self.id_new_kn)
                    self.kniga_repo.dod_new_kn(self.sp_kn, kortez)
                    self.id_new_kn += 1
                    self.view.show_message(f'До бібліотеки додано книгу "{kortez[0]}" зa номером {kortez[4]}')
                case '2':
                    ima = self.view.dod_new_chit()
                    chit= self.chitac_repo.dod_new_chit(self.sp_kor,ima,self.id_new_kor)
                    self.id_new_kor+=1
                    self.view.show_message(f"Створений новий читацький запис! Читач {chit.ima}, має номер читацького білету {chit.nomChitBil}.")
                case '3':
                    self.view.show_message('Перелік книг бібліотеки:')
                    self.view.print_knigi(self.sp_kn)
                case '4':
                    ganr = self.view.zapit_ganr()
                    filtr_kn = self.kniga_repo.filtr_ganr(ganr, self.sp_kn)
                    self.view.show_message(f'\tПерелік книг бібліотеки в жанрі "{ganr}":')
                    self.view.print_knigi(filtr_kn)
                case '5':
                    kortez=self.view.vid_povern_kn(self.sp_kor,self.sp_kn,'vidati')
                    if(kortez):
                        if(len(kortez[0].spis)<=3):
                            self.kniga_repo.vidati_abo_povern_kn(kortez)
                            self.view.show_message(f'Читач "{kortez[0].ima}" з номером читацького білету {kortez[0].nomChitBil} отримав книгу "{kortez[1].nazva}" за номером {kortez[1].id_kn} .')
                        else:
                            self.view.show_message('Книгу видати не можливо! Читач не може отримати більше 3-х книжок!')
                case '6':
                    kortez = self.view.vid_povern_kn(self.sp_kor, self.sp_kn, 'povern')
                    if (kortez):
                        self.kniga_repo.vidati_abo_povern_kn(kortez)
                        self.view.show_message(
                            f'Читач "{kortez[0].ima}" з номером читацького білету {kortez[0].nomChitBil} повернув книгу "{kortez[1].nazva}" за номером {kortez[1].id_kn}.')
                case '7':
                    self.view.per_kor(self.sp_kor,self.sp_kn)
                case '8':
                    self.chitac_repo.zber_u_file(self.sp_kor)
                    self.kniga_repo.zber_u_file(self.sp_kn)
                    self.view.show_message("Зміни збережені у файл!")
                case '9':
                    self.view.vihid()
                    break
