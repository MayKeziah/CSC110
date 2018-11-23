#ENCODING ALGORITHIM
def main():
    message = input("please enter a message to encode: ")
    for ch in message:
        print(ord(ch), end = " ")

main()
