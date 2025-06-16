class Kniga:
    def __init__(self, naz, avt, rik, ganr, id_kn):
        self.nazva = naz
        self.avtor = avt
        self.rikVid = rik
        self.ganr = ganr
        self.stat = 0
        self.id_kn = id_kn

    def u_str(self):
        return f"{self.nazva}|{self.avtor}|{self.rikVid}|{self.ganr}|{self.stat}|{self.id_kn}"

    @classmethod
    def z_str(cls, line):
        parts = line.strip().split('|')
        kn = cls(parts[0], parts[1], int(parts[2]), parts[3], int(parts[5]))
        kn.stat = int(parts[4])
        return kn