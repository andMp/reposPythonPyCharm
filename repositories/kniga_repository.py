from models.Kniga import Kniga
from views.bibl_view import bibl_view

class KnigaRepository:
    FILE_NAME = 'knigi.txt'

    def filtr_ganr(self,ganr,sp_kn):
        return [kn for kn in sp_kn if kn.ganr == ganr]

    def zavant_z_file(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
                return [Kniga.z_str(line) for line in f]
        except FileNotFoundError:
            return []

    def zber_u_file(self, spisok_knig):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
            for kn in spisok_knig:
                f.write(kn.u_str() + '\n')

    def vidati_abo_povern_kn(self,kortez):
            ab, kn, dia = kortez
            match dia:
                case 'povern':
                    ab.spis.remove(kn.id_kn)
                    kn.stat = 0
                case 'vidati':
                    ab.spis.append(kn.id_kn)
                    kn.stat = ab.nomChitBil
                case _:
                    return False

    def dod_new_kn(self,spis_knig,kortez):
        spis_knig.append(Kniga(*kortez)) # розпаковка кортежу у параметри конструктора