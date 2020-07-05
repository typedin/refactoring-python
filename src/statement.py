from src.createStatementData import createStatementData
from src.currency import usd


def statement(invoice, plays):
    return renderPlainText(createStatementData(invoice, plays))


def renderPlainText(data):
    result = "Statement for {}\n".format(data.get("customer"))

    for perf in data.get("performances"):
        result += " {}: {} ({} seats)\n".format(
            perf.get("play").get("name"),
            usd(perf.get('amount')),
            perf.get("audience")
        )

    result += "Amount owed is {}\n".format(usd(data.get("totalAmount")))
    result += "You earned {} credits\n".format(data.get("totalVolumeCredits"))

    return result
