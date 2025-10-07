def total_registered_cases(data, country):
    return sum(data[country])

def total_registered_cases_per_country(data):
    totals = {}
    for country in data:
        totals[country] = sum(data[country])
    return totals

def country_with_most_cases(data):
    totals = total_registered_cases_per_country(data)
    max_country = None
    max_cases = 0
    for country, total in totals.items():
        if total > max_cases:
            max_cases = total
            max_country = country
    return max_country
