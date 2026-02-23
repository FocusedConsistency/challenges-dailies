def count_medals(winners):
    title = ['Country,Gold,Silver,Bronze,Total']
    totals = {}
    for top3 in winners:
        for i, country in enumerate(top3):
            totals[country] = totals.get(country, [0, 0, 0, 0])
            totals[country][i] += 1
            totals[country][3] += 1
          
    countries = []
    for country, medals in totals.items():
        countries.append(f'{country},{medals[0]},{medals[1]},{medals[2]},{medals[3]}')
    
    sorted_countries = sorted(countries, key=lambda x: (-int(x.split(',')[1]), x.split(',')[0]))

    return '\n'.join(title + sorted_countries)

count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]])
# Country,Gold,Silver,Bronze,Total
# USA,2,1,0,3
# NOR,1,1,1,3
# CAN,0,1,1,2
# SWE,0,0,1,1
