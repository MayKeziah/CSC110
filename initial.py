#batch-oreinted program that reads first and last names and prints initials

def other():
    fname = "names.dat"
    infile = open(fname, "r")

    data = infile.readlines()
    for line in data:
        print ("Hello,", line, end = " ")
        print("your initials are", end = " ")
        newlist = line.split(" ")
        init = ""
        for name in newlist:
            init = init + name[0]
            print(init)

    infile.close()

other()


def bodine():
    fname = "names.dat"
    infile = open(fname, "r")

    data = infile.readlines()
    for line in data:
        first,last = line.split()
        initfirst = first[0]
        initlast = last[0]

        print("Hello, ", first, " ", last, ". Your initials are ", initfirst + "." + initlast + ".")

    infile.close()
bodine()
