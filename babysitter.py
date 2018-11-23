#Ch7.7 Q7

def main():
    start = min2hour(input('Please input the start time in format "hour:min" using the 24 hour system: '))
    end = min2hour(input('Please input the end time in format "hour:min" using the 24 hour system: '))
    FirstBill = (21 - start) * 2.5
    SecondBill = (end - 21) * 1.75
    Bill = FirstBill + SecondBill
    print(Bill)

def min2hour(time):
    #hour:min
    hours, mins = time.split(":")
    mins = eval(mins)*5/3*0.01
    newtime = eval(hours) + mins
    print(newtime.format(
    #return newtime

main()
