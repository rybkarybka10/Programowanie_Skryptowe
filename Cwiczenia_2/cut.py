def cut(delim='\t', field=[]):
    tekst = input()
    wejscie = []
    odpowiedz = []
    while tekst != "":
        wejscie.append(tekst)
        tekst = input()
    field = [int(i)-1 for i in field]
    s = [i.split(delim) for i in wejscie]
    for i in range(len(s)):
        for ind, matched in enumerate(s[i]):
            if ind in field:
                odpowiedz.append(matched)

    return odpowiedz