from math import floor


def createStatementData(invoice, plays):

    def enrichPerformance(aPerformance):
        result = aPerformance
        result.update({
            "play": playFor(result),
        })
        result.update({
            "amount": amountFor(result),
        })
        result.update({
            "volumeCredits": volumeCreditsFor(result)
        })

        return result

    def volumeCreditsFor(aPerformance):
        result = 0
        result = max(aPerformance.get("audience") - 30, 0)

        if aPerformance.get("play").get("type") == "comedy":
            result += floor(aPerformance.get("audience") / 5)
        return result

    def totalVolumeCredits(data):
        result = 0
        for perf in data.get("performances"):
            result += volumeCreditsFor(perf)
        return result

    def playFor(aPerformance):
        return plays.get(aPerformance.get("playID"))

    def totalAmount(data):
        result = 0
        for perf in data.get("performances"):
            result += perf.get("amount")
        return result

    def amountFor(aPerformance):
        result = 0
        if playFor(aPerformance).get("type") == "tragedy":
            result = 40000
            if aPerformance.get("audience") > 30:
                result += 1000 * (aPerformance.get("audience") - 30)
        elif playFor(aPerformance).get("type") == "comedy":
            result = 30000
            if aPerformance.get("audience") > 20:
                result += 10000 + 500 * (aPerformance.get("audience") - 20)
            result += 300 * aPerformance.get("audience")
        else:
            raise Exception("unknown type: {}".format(
                aPerformance.get("play").get("type")))

        return result

    result = {}
    result.update({
        "customer": invoice.get("customer"),
        "performances": list(map(enrichPerformance, invoice["performances"]))
    })
    result.update({
        "totalAmount": totalAmount(result),
        "totalVolumeCredits": totalVolumeCredits(result)
    })

    return result
