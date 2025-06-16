class Koristuvac:
    def __init__(self,ima,nomChitBil):
        self.ima = ima
        self.nomChitBil = nomChitBil
        self.spis =[]


    def vidati_kn_korist(self,kn):
        if len(self.spis)<=3:
            self.spis.append(kn)

    def u_str(self):
        spis_id_kn = ','.join(str(id_kn) for id_kn in self.spis)
        return(f'{self.ima}|{self.nomChitBil}|{spis_id_kn}')

    @classmethod
    def z_str(cls,line):
        pole = line.strip().split('|')
        kor=cls(pole[0],pole[1])
        kor.spis= list(map(int, pole[2].split(','))) if pole[2] else []
        return kor

    def zber_u_file(self,sp_kor):
        with open('koristuvaci.txt','w', encoding='utf-8') as f:
            for k in sp_kor:
                f.write(k.u_str()+'\n')

    def zavant_z_file(self,sp_kor):
        with open('koristuvaci.txt','w', encoding='utf-8') as f:
            sp_kor = [Koristuvac.z_str(line) for line in f]