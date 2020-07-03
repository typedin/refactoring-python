from math import floor


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = "Statement for {}".format(invoice['customer'])
    result += "\n"

    def formatCurrency(aNumber):
        return '${:,.2f}'.format(aNumber)

    for perf in invoice['performances']:
        play = plays[perf["playID"]]
        thisAmount = 0

        if play["type"] == "tragedy":
            thisAmount = 40000
            if perf["audience"] > 30:
                thisAmount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            thisAmount = 30000
            if perf["audience"] > 20:
                thisAmount += 10000 + 500 * (perf["audience"] - 20)
            thisAmount += 300 * perf["audience"]
        else:
            raise Exception("unknown type: {}".format(play["type"]))

        volumeCredits += max(perf['audience'] - 30, 0)

        if play["type"] == "comedy":
            volumeCredits += floor(perf["audience"] / 5)

        result += " {}: {} ({} seats)\n".format(
            play["name"], formatCurrency(thisAmount / 100), perf["audience"])

        totalAmount += thisAmount

    result += "Amount owed is {}\n".format(formatCurrency(totalAmount / 100))
    result += "You earned {} credits\n".format(volumeCredits)

    return result
