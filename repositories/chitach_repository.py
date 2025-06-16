from models.Koristuvac import Koristuvac

class KoristuvacRepository:
    FILE_NAME = 'koristuvaci.txt'

    def zavant_z_file(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
                return [Koristuvac.z_str(line) for line in f]
        except FileNotFoundError:
            return []

    def zber_u_file(self, spisok_chitaciv):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as f:
            for ch in spisok_chitaciv:
                f.write(ch.u_str() + '\n')

    def dod_new_chit(self,spis_kor,ima,nomChitBil):
        new_kor = Koristuvac(ima, nomChitBil)
        spis_kor.append(new_kor)
        return new_kor