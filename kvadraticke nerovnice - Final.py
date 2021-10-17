#!/usr/bin/env python3
import math


#<patří>
#(nepatří)
#D = bb -4ac
#x1,2 = -b +- D.sqrt / 2a

#Zadáme abc
print("Zadej hodnoty a,b,c")
a = int(input("zadej hodnotu A: "))
b = int(input("zadej hodnotu B: "))
c = int(input("zadej hodnotu C: "))

#vybereme operator
print("Vyber operátor z nabídky:\n1. >=\n2. <=\n3. >\n4. <")
op = int(input("Vyber si z nabídky: "))

#spárujeme operátor s příslušnými závorkami
if op == 1:
    op = ">="
    LZavorka = "<"
    PZavorka = ">"
    NekonecnoL = "("
    NekonecnoP = ")"
if op == 2:
    op = "<="
    LZavorka = "<"
    PZavorka = ">"    
    NekonecnoL = "("
    NekonecnoP = ")"
if op == 3:
    op = ">" 
    LZavorka = "("
    PZavorka = ")"
    NekonecnoL = "("
    NekonecnoP = ")"
if op == 4:
    op = "<"
    LZavorka = "("
    PZavorka = ")"
    NekonecnoL = "("
    NekonecnoP = ")"
else:
    print("Zadal jsi neplatnou hodnotu. ")

#ukážeme si jak vypadá rovnice, jen pro klid duše a estetickou stránku programu, jinak je to k ničemu
rovnice = (f"{a}x^2 + {b}x + {c} {op} 0")
print(f"Rovnice vypadá takto: \n{rovnice}")
print("----------------------")

#Spočítáme Diskriminant (D) a x1,2
b2 = b**2
DD = b2 - 4 * a * c
D = float(DD)

#postaráme se aby se neodmocňovala nula
if D <= 0:
    a2 = 2 * a
    x11 = -b - D
    x22 = -b + D
    x1 = x11 / a2
    x2 = x22 / a2
if D > 0:
    odmD = math.sqrt(D)
    a2 = 2 * a
    x11 = -b - odmD
    x22 = -b + odmD
    x1 = x11 / a2
    x2 = x22 / a2

#uspořádáme x1,2 - nejvíce jednoduchou cestou :D 
if x1 > x2:
    x3 = x1
    x4 = x2
    x1 = x4
    x2 = x3
else:
    x1 = x1
    x2 = x2

#rozvětvíme D
if D > 0:
    print("Parabola protíná osu X ve dvou bodech")
    if a > 0:
        print(f"interval je: \n{NekonecnoL}-nekonečno; {x1}{PZavorka} a {LZavorka}{x2}; nekonečno{NekonecnoP}")
    if a < 0:
        print(f"Interval je: \n {LZavorka}{x1}; {x2}{PZavorka}")
if D == 0:
    print("Parabola protíná osu X v jednom bodě.")
    if a > 0:
        print(f"Interval je {LZavorka}{x1}{PZavorka}")        
    if a < 0:
        print(f"Interval je {NekonecnoL}-nekonečno; {x1}{PZavorka} a {LZavorka}{x2}; nekonečno{NekonecnoP}")
if D < 0:
    print("Parabola neprotíná osu X.")
    if a > 0:
        print("Tato nerovnice nemá řešení - je jím prázdná množina.")
    if a < 0:
        print("Řešením jsou všechna R.")