import string


def sistema_0_36(chislo, delitel):
    otv = ''
    sistema_ch = string.digits + string.ascii_uppercase
    while chislo > 0:
        otv = sistema_ch[chislo % delitel] + otv
        chislo = chislo // delitel
    return otv


print(sistema_0_36(76, 5))