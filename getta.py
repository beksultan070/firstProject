country = ['usa','german', 'russia', 'kyrgyzstan', 'korea']
europe = ['german', 'france', 'russia', 'poland',]
new_country = set(country)
names = new_country.symmetric_difference(europe)
print(tuple(names))

# ('usa', 'kyrgyzstan', 'korea', 'france', 'poland')