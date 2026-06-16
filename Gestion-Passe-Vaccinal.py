def saisie():
    n = 0
    while not 5 <= n <= 100:
        n = int(input("Entrez un nombre entre 5 et 100 : "))
    return n


def valid(ch):
    ok = False

    if len(ch) >= 13:
        if ch[10] == '-' and ch[-1].isdigit():
            ok = True

    return ok


def remplir(tab,n):
    for i in range(n):
        ch = ""
        while not valid(ch):
            ch = input("Entrez les informations du citoyen : ")
        tab[i] = ch


def affiche(tab,n):
    for i in range(n):

        code = tab[i][0:10]

        pos = tab[i].find("-")
        vaccin = tab[i][pos+1:-1]

        doses = tab[i][-1]

        if doses == '2' or (doses == '1' and vaccin == "Johnson"):
            print("Le titulaire du code", code,
            "vous pouvez télécharger votre passe vaccinale")
        else:
            print("Le titulaire du code", code,
            "vous êtes appelé à compléter votre schéma vaccinal")


n = saisie()

tab = [None]*n

remplir(tab,n)

affiche(tab,n)