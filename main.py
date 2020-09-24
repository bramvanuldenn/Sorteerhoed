from Sorteerhoed import classes

s = classes.Systeem()
vragendict = s.vragen
inputNaam = str(input("Wat is je naam? "))
afnemer = classes.Afnemer(inputNaam)
print(s.vragen)
for i in vragendict:
    v = vragendict[i]
    print(v[0])
    print(f"A:{v[1]} B:{v[2]} C:{v[3]} D:{v[4]}")
    i = str(input()).lower()
    while i not in "abcd":
        print("verkeerde input")
        i = str(input()).lower()
    afnemer.addTo(i)



print(afnemer.scoredict)
