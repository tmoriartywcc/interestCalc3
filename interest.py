def getInput():
    interest_rate = float(input("Enter Interest Rate: "))

    while interest_rate < 0:
        interest_rate = float(input("Error please enter positive number.  Enter Interest Rate: "))

    dollar_amt = float(input("Enter Dollar Amount: "))

    while dollar_amt < 0:
        dollar_amt = float(input("Error please enter positive number.  Enter Dollar Amount: "))

    return interest_rate, dollar_amt

def calc_interest(interest_rate, dollar_amt):
    new_amt = dollar_amt * (1 + interest_rate)
    return new_amt

def outputResult(dollar_amt):
    print('$', format(dollar_amt, '.2f'), sep='')

interest_rate, dollar_amt = getInput()
new_amt = calc_interest(interest_rate, dollar_amt)
outputResult(new_amt)