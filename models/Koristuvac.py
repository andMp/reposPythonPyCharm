class Koristuvac:
    def __init__(self,ima,nomChitBil):
        self.ima = ima
        self.nomChitBil = nomChitBil
        self.spis =[]


    def vidati_kn_korist(self,kn):
        if len(self.spis)<=3:
            self.spis.append(kn)