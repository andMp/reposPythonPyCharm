class Kniga:
    def __init__(self, naz, avt, rik, ganr, id_kn):
        self.nazva = naz
        self.avtor = avt
        self.rikVid = rik
        self.ganr = ganr
        self.stat = 0
        self.id_kn = id_kn

    def dod_new_kn(self,spis_knig,kortez):
        spis_knig.append(Kniga(naz, avt, rik, ganr, id_kn))

    def vidati_abo_povern_kn(self,kortez):
            ab, kn, dia = kortez
            # if dia == 'povern':
            #     if id_kn in ab.spis:
            #         ab.spisKn.remove(idKn)
            #         kn.vidanaKomu = 0
                    # print(f'Kniga "{kn.nazva}" z id={kn.id_kn} povernuv abonent {ab.ima} z id={ab.nomChitBil}.')
            match dia:
                case 'povern':
                    ab.spis.remove(kn.id_kn)
                    kn.stat = 0
                case 'vidati':
                    ab.spisKn.append(kn.id_Kn)
                    kn.stat = ab.nomChitBil
                case _:
                    return False
            # else dia == 'vidati':
                # ab.spisKn.append(kn.idKn)
                # kn.vidanaKomu = ab.nomAbon
                # return id_kor, id_kn, dia
                # print(f'Kniga "{kn.nazva}" z id={kn.idKn} vidana abonentu {ab.ima} z id={ab.nomAbon}.')
            # else:
            #     print("Невідома дія. Вкажіть 'vidati' або 'povern'.")

    def u_str(self):
        return f"{self.nazva}|{self.avtor}|{self.rikVid}|{self.ganr}|{self.stat}|{self.id_kn}"

    @classmethod
    def z_str(cls, line):
        parts = line.strip().split('|')
        kn = cls(parts[0], parts[1], int(parts[2]), parts[3], int(parts[5]))
        kn.stat = int(parts[4])
        return kn

    def zber_u_file(self,spis_knig):
        with open('knigi.txt', 'w', encoding='utf-8') as f:
            for kn in spis_knig:
                f.write(kn.u_str() + '\n')

    def zavant_z_file(self,spis_kn):
        with open('knigi.txt', 'r', encoding='utf-8') as f:
            spis_kn = [Kniga.z_str(line) for line in f]