def numer_dnia(numer):
    lista=["poniedzialek","wtorek","sroda","czwartek","piatek","sobota","niedziela"]
    return lista[numer-1]

def skrocone_nazwy(dzien):
    if dzien=="poniedzialek":
        return "pon."
    elif dzien=="wtorek":
        return "wt."
    elif dzien=="sroda":
        return "sr."
    elif dzien=="czwartek":
        return "czw."
    elif dzien=="piatek":
        return "pt."
    elif dzien=="sobota":
        return "sob."
    elif dzien=="niedziela":
        return "niedz."