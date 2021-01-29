import os
slowo = "kasztan"
zgadniete = ["_"] * len(slowo)
wordlist = list(slowo)
b = 0
def zgadywanie(zgadniete,wordlist,slowo,b):
    zycia = len(wordlist)
    blad = []
    print("####################################################")
    print("#                   GRA WISIELEC                   #")
    print("####################################################\n")
    print("Masz",zycia,"sznas na zgadniecie ukrytego słowa!\n")
    n_zycie= len(wordlist)
    while n_zycie > 0 and zgadniete != wordlist:
        czyste = list(dict.fromkeys(blad))
        print("\nUzyte litery:",czyste)
        print("\nPozostałe sznse: ",n_zycie)
        litera = str(input("\nPodaj litere[Enter]: ")) [0]
        if litera in slowo:
            i = 1
            for word in range(len(wordlist)):
                if litera == str(wordlist[word]):
                    zgadniete[word] = (str(wordlist[word]))
                    os.system('clear')
                    print("Zgadłeś litery:",zgadniete)
                    print("")
                    szubienica(b)
                    if zgadniete == wordlist:
                        print("    __--__--__--__--")
                        print("    __--Wygrales!--__")
                        print("    __--__--__--__--")
                        exit(0)
             
        else:
            b= b + 1
            n_zycie= n_zycie - 1
            os.system('clear')
            blad.append(litera)
            print("Zgadłeś litery:", zgadniete)
            print("")
            szubienica(b)
def szubienica(b):
    if b == 1:
        print("    _______")
    elif b== 2:
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("    _|_______")
    elif b == 3:
        print("     |----")
        print("     |")
        print("     |")
        print("     |")
        print("    _|_______")
    elif b == 4:
        print("     |----|")
        print("     |    0")
        print("     |")
        print("     |")
        print("    _|_______")
    elif b == 5:
        print("     |----|")
        print("     |    0")
        print("     |    |")
        print("     |")
        print("    _|_______")
    elif b == 6:
        print("     |----|")
        print("     |    0")
        print("     |   /|/")
        print("     |")
        print("    _|_______")
    elif b == 7:
        print("     |----|")
        print("     |    0")
        print("     |   \|/")
        print("     |   (-)")
        print("    _|_______")
        print("\n    __--__--__--__--")
        print("    __--Game Over__--")
        print("    __--__--__--__--")
        exit(0)
zgadywanie(zgadniete,wordlist,slowo,b)

