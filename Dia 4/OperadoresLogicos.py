# opperador logico Y, O, NO, and,or,not
mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4 < 5) and (5 == 2+3)
print(mi_bool)

mi_bool = (4 < 5) or (5 == 2+3)
print(mi_bool)

texto = "esta frase es verdadera"
mi_bool = ("frase" in texto) and ("verdadera" in texto)

mi_bool = not ('a' != 'a')
print(mi_bool)
mi_bool = not ('a' == 'a')
print(mi_bool)