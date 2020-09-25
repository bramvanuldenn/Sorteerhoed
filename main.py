import classes

s = classes.Systeem()
inputNaam = str(input("Wat is je naam? "))
afnemer = classes.Afnemer(inputNaam)
for i in s.vragen:
    print(i)
    print(s.vragen[i])
    a = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3
    }
    inputAntwoord = str(input()).lower()
    iterdict = iter(s.vragen[i])
    if inputAntwoord in "abcd":
        val = a[inputAntwoord]
        print(val)
        for i in range(0, val):
            next(iterdict)
        a = (next(iterdict))
        print(a)
        afnemer.addto(a)
        print(afnemer.scoredict)

