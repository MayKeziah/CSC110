#DECODING ALGORITHIM

def main():
    inString = input("Please enter the unicode-encoded message: ")

    message = ""
    for numStr in inString.split(" "):
        codeNum = eval(numStr)
        message = message + chr(codeNum)
    print(message)

main()
