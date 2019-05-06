

def wymiana(pierwszy):
    lista=list(pierwszy)
    pierwsza_litera=lista[0]
    ostatnia_litera=lista[-1]
    lista[-1]=pierwsza_litera
    lista[0]=ostatnia_litera
    wynik="".join(lista)
    print(wynik)

pierwszy=input()
wymiana(pierwszy)

Print(„Wszystkiego najlepszego”)
