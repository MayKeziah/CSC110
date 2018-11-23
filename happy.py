#happy.py

def happy():
    return "Happy Birthday to you!\n"

def VerseFor(person):
    lyrics = happy()*2 + "Happy Birthday, dear " + person + ".\n" + happy()
    return lyrics

def main ():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(VerseFor(person))

main()
