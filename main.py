from secrets import choice

vsiKont=[]
def stvorKont():
    print("Zapovnit dani nizce:")
    ima=input("Ima: ")
    telefon=input("Telefon: ")
    email=input("Email: ")
    adresa = input("Adresa: ")
    kontNS=[]
    n=int(input("Vvedit k-st kontaktiv pri NS: "))
    for i in range(n):
        imaNS = input("Ima: ")
        telefonNS = input("Telefon: ")
        emailNS = input("Email: ")
        adresaNS = input("Adresa: ")
        kontNS.append({
            "ima": imaNS,
            "telefon": telefonNS,
            "email": emailNS,
            "adresa": adresaNS
        })
    kont={
        "ima": ima,
        "telefon": telefon,
        "email": email,
        "adresa": adresa,
        "kontNS": kontNS
    }
    vsiKont.append(kont)
    print("Kontakt dodan!")

def pereglad():
    if not vsiKont:
        print("Vsi kontaktov")
    else:
        for i, kont in enumerate(vsiKont,start=1):
            print(f"\nKontakt #{i}:")
            print(f" Ima: {kont['ima']}")
            print(f" Telefon: {kont['telefon']}")
            print(f" Email: {kont['email']}")
            print(f" Adresa: {kont['adresa']}")
            print(" Kontakti NS:")
            for j, kNS in enumerate(kont['kontNS'], start=1):
                print(f" [{j}]Ima: {kNS['ima']}, Telefon: {kNS['telefon']}, Email: {kNS['email']}, Adresa: {kNS['adresa']}")

def redag():
    pereglad()
    try:
        nK=int(input("Vvedit nomer kontakta dla redaguvanna: "))-1
        if 0 <= nK <= len(vsiKont):
            kont=vsiKont[nK]
            print(f"Ne vvodte dani shob ne zminuvati.")
            nName=input(f"Nove ima kontakta [{kont['ima']}]: ") or kont['ima']
            nTel = input(f"Noviy telefon [{kont['telefon']}]: ") or kont['telefon']
            nEmail= input(f"Noviy email [{kont['email']}]: ") or kont['email']
            nAddr= input(f"Nova adresa [{kont['adresa']}]: ") or kont['adresa']
            kont['ima']=nName
            kont['telefon']=nTel
            kont['email']=nEmail
            kont['adresa']=nAddr
            print(f"Kontakt onovlen!")
        else:
            print("Nevirniy nomer kontakta.")
    except ValueError:
        print("Vvedit nomer kontakta.")
def vidal():
    pereglad()
    try:
        nk = int(input("Vvedit nomer kontakta dla vidalenna: "))
        if 0 <= nk <= len(vsiKont):
            vsiKont.pop(nk)
            print(f"Kontakt vidalen!")
        else:
            print("Nevirniy nomer kontakta.")
    except ValueError:
        print("Vvedit nomer kontakta.")

def main():
    while True:
        print("\n=== Menu kontaktiv ===")
        print("1.Stvoriti kontakt")
        print("2.Pereglanuti vsi kontakti")
        print("3.Redaguvati kontakt")
        print("4.Vidaliti kontakt")
        print("5.Zaversiti robotu.")
        c = input("Zrobit vas vibir: ")
        if c == '1':
            stvorKont()
        elif c == '2':
            pereglad()
        elif c == '3':
            redag()
        elif c == '4':
            vidal()
        elif c == '5':
            print("Zaversenna roboti!")
            break
        else:
            print("Ne virno! Sprobuy znov!")

if __name__ == "__main__":
    main()




