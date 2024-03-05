# this project will take an input when it comes to current currency and then take an input of a desired currency, and
# then it will return conversion amount, followed by asking for the amount of money you would like to convert.

# conversion rate as of 02/25/2024
conversion_rate = {
        "eur": .92436,
        "jpy": 150.44,
        "gbp": .78948,
        "aud": 1.52500,
        "cad": 1.32140,
        "chf": .88163,
        "cny": 7.19520,
        "hkd": 7.82470,
        "nzd": 1.62050
    }


def exchange(convert_currency, amount):
    if convert_currency in conversion_rate:
        return conversion_rate[convert_currency]*amount
    else:
        return "Conversion currency not supported!! Sorry!!"


while True:
    user_choice = input("Select the currency you wish to convert to:\n"
                        "Euro (EUR)\n"
                        "Japanese Yen (JPY)\n"
                        "British Pound (GBP)\n"
                        "Australian Dollar (AUD)\n"
                        "Canadian Dollar (CAD)\n"
                        "Swiss Franc (CHF)\n"
                        "Chinese Yuan (CNY)\n"
                        "Hong Kong Dollar (HKD)\n"
                        "New Zealand Dollar (NZD): \n").lower()
    if user_choice not in conversion_rate:
        continue
    else:
        break

while True:
    user_amount = input("How many United States Dollars (USD) do you wish to convert\n"
                        "to the selected currency: ")
    if int(user_amount) <= 0:
        continue
    else:
        break

print("USD:", user_amount, "converts to", user_choice.upper() + ":", exchange(user_choice, int(user_amount)))
