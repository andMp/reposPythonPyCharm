
import random
import time
import os
import msvcrt

WIDTH = 20
HEIGHT = 10

class Kulka:
    def __init__(self, x):
        self.x = x
        self.y = 0

    def Padinna(self):
        self.y += 1

class Platforma:
    def __init__(self):
        self.x = WIDTH // 2
        self.width = 7

    def vLivo(self):
        if self.x > 0:
            self.x -= 1

    def vPravo(self):
        if self.x + self.width < WIDTH:
            self.x += 1

    def Roztash(self, x):
        return self.x <= x < self.x + self.width

class Gra:
    def __init__(self):
        self.platform = Platforma()
        self.kulki = []
        self.rahunok = 0
        self.sproba = 3
        self.shvidk = 0.4

    def stvorKulki(self):
        x = random.randint(0, WIDTH - 1)
        self.kulki.append(Kulka(x))

    def onovl(self):
        os.system("cls" if os.name == "nt" else "clear")

        pole = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

        for kulka in self.kulki:
            if 0 <= kulka.y < HEIGHT:
                pole[kulka.y][kulka.x] = "0"

        for i in range(self.platform.width):
            px = self.platform.x + i
            pole[HEIGHT - 1][px] = "="

        for row in pole:
            print("".join(row))
        print(f"\nRahunok: {self.rahunok}   Sprob: {self.sproba}")

    def logika(self):
        for kulka in self.kulki:
            kulka.Padinna()

        for kulka in self.kulki[:]:
            if kulka.y == HEIGHT - 1:
                if self.platform.Roztash(kulka.x):
                    self.rahunok += 1
                else:
                    self.sproba -= 1
                self.kulki.remove(kulka)

    def get_char(self):
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8').lower()
        return ""

    def proces(self):
        try:
            while self.sproba > 0:
                if random.random() < 0.3:
                    self.stvorKulki()

                self.onovl()
                hid = self.get_char()

                platform_speed = 3 if hid in ("a", "d") else 1

                if hid == "a":
                    for _ in range(platform_speed):
                        self.platform.vLivo()
                elif hid == "d":
                    for _ in range(platform_speed):
                        self.platform.vPravo()

                self.logika()

                self.shvidk = max(0.1, 0.4 - self.rahunok * 0.01)
                time.sleep(self.shvidk)

            self.onovl()
            print("\nKinec gri!")
            print(f"Vi zibrali: {self.rahunok}")
        except KeyboardInterrupt:
            print("\nVihid z gri.")

if __name__ == "__main__":
    game = Gra()
    game.proces()










