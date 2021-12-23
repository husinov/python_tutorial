city = {'Tashkent', 'Moscow', 'New York', 'Sydney', 'London', 'Singapur', 'Tokyo'}

country = {'Singapur', 'Seul', 'Moscow'}

# print(city.difference(country))
# city.add('Monaco')
# city.pop()
# city.discard('London')    #doesn't raise an error
# city.remove('Moscow')     #raise an error
# city.difference_update(country)
# city.update(country)
# a = city.union(country)
# a = city.intersection(country)
# city.intersection_update(country)
# print(city.isdisjoint(country))
# print(country.issubset(city))
# print(city.issuperset(country))
# print(city.symmetric_difference(country))
# city.symmetric_difference_update(country)

for i in city:
    print(i, end = ' ')
