my_dictionary = {}
print(my_dictionary)
print(type(my_dictionary))
print("********************************************")
my_information = {'name': 'Dionysia', 'age': 28, 'location': 'Athens'}
print(my_information)
print("********************************************")
cities = ('Paris', 'Athens', 'Madrid')
my_dictionary = dict.fromkeys(cities)
print(my_dictionary)
print("********************************************")
city = ('Paris', 'Athens', 'Madrid')
continent = 'Europe'
my_dictionary = dict.fromkeys(city, continent)
print(my_dictionary)
print("**********************************************")
year_of_creation = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}
print(year_of_creation.values())
