print "Pozdravljen/a v geografskem kvizu!"

mesta_drzav = {
    "Slovenija": "Ljubljana",
    "Hrvaska": "Zagreb",
    "Avstrija": "Dunaj",
    "Italija": "Rim"
}

from random import randint

drzave = mesta_drzav.keys()
mesta = mesta_drzav.values()


while True:
    nakljucna_st = randint(0, 3)
    x = raw_input("Katero je glavno mesto drzave " + str(drzave[nakljucna_st]) + "? ")
    if x == mesta[nakljucna_st]:
        print "Bravo"
    else:
        print "Poskusi se enkrat."
    y = raw_input("Bi rad nadaljeval? (DA / NE) ")
    if y == "NE":
        print "Adijo!"
        break







