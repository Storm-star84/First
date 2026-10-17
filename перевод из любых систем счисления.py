# def any_sis_cusl(chislo,Sistema_cusl):
#     otv=''
#     while chislo>0:
#         otv=str(chislo%Sistema_cusl)+otv
#         chislo=chislo//Sistema_cusl
#     return otv
# print(any_sis_cusl(76,5))
import string
def sistema_0_36(chislo,delitel):
    otv=''
    sistema_ch=string.digits+string.ascii_uppercase
    while chislo>0:
        otv=sistema_ch[chislo % delitel]+otv
        chislo=chislo//delitel
    return otv
print(sistema_0_36(76,5))
