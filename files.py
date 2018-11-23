def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    data = infile.read()

    print("data", data)
    print("data split", data.split("\n"))


    infile.close()

main()

def other():
    fname = input("Enter filename: ")
    infile = open(fname, "r")

    data = infile.readlines()
    for line in data:
        print (line)


    infile.close()

other()
