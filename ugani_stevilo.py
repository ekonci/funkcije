print "UGANI STEVILO"

from random import randint

def main():
    skrita_stevilka = randint(1, 50)

    while True:
        guess = int(raw_input("Ugani stevilko od 1 do 50: "))
        if skrita_stevilka == guess:
            print "Bravo! ta stevilka je %s" %skrita_stevilka
            break
        elif skrita_stevilka > guess:
            print "Premajhno, probaj visjo st."
        elif skrita_stevilka < guess:
            print "Poskusi manjso stevilko"

print main()
