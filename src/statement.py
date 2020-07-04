from math import floor
from pprint import pprint


def usd(aNumber):
    return '${:,.2f}'.format(aNumber / 100)


def statement(invoice, plays):
    statementData = {}
    statementData["customer"] = invoice["customer"]
    statementData["performances"] = invoice["performances"]

    return renderPlainText(statementData, plays)


def renderPlainText(data, plays):
    result = "Statement for {}\n".format(data['customer'])

    def playFor(aPerformance):
        return plays[aPerformance["playID"]]

    def volumeCreditsFor(aPerformance):
        result = 0
        result += max(aPerformance['audience'] - 30, 0)

        if playFor(aPerformance)["type"] == "comedy":
            result += floor(aPerformance["audience"] / 5)
        return result

    def amountFor(aPerformance):
        result = 0
        if playFor(aPerformance)["type"] == "tragedy":
            result = 40000
            if aPerformance["audience"] > 30:
                result += 1000 * (aPerformance["audience"] - 30)
        elif playFor(aPerformance)["type"] == "comedy":
            result = 30000
            if aPerformance["audience"] > 20:
                result += 10000 + 500 * (aPerformance["audience"] - 20)
            result += 300 * aPerformance["audience"]
        else:
            raise Exception("unknown type: {}".format(
                playFor(aPerformance)["type"]))
        return result

    def totalVolumeCredits():
        result = 0
        for perf in data['performances']:
            result += volumeCreditsFor(perf)
        return result

    def totalAmount():
        result = 0
        for perf in data["performances"]:
            result += amountFor(perf)
        return result

    for perf in data['performances']:
        result += " {}: {} ({} seats)\n".format(
            playFor(perf)["name"],
            usd(amountFor(perf)), perf["audience"])

    totalAmount = totalAmount()

    result += "Amount owed is {}\n".format(usd(totalAmount))
    result += "You earned {} credits\n".format(totalVolumeCredits())

    return result
