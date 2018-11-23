def main():
    print ("Hello, World!")

main()

def repeat(repetitions):
    if repetitions > 100:
        print ("No.")
        return
    for x in range(0, repetitions):
        main()

        
