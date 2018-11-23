#Old MacDonald

def oldmac():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"

	
def onfarm(animal):
    return "And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n"

	
def witha(sound):
    soundlines = "With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.\n" + "Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ".\n"
    return soundlines

def verse(animal, sound):
    lyrics = oldmac() + onfarm(animal) + witha(sound) + oldmac()
    return lyrics

def main():
    thevar = ["Cow Moo", "Horse Neigh", "Pig Oink"]
    for i in thevar:
        animal,sound = i.split()
        print(verse(animal, sound))

main()
