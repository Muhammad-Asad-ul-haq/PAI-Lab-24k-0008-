countries = {
    "China": 1312,
    "India": 1231,
    "USA": 3231,
    "Indonesia": 1373,
    "Pakistan": 220,
    "Bangladesh": 212
}


country_list = list(countries.items())

n = len(country_list)


for i in range(n):
    for j in range(0, n-i-1):
        if country_list[j][1] < country_list[j+1][1]:   
            country_list[j], country_list[j+1] = country_list[j+1], country_list[j]

# print top 3
print("Top 3 Most Populated Countries:")
print(country_list[0])
print(country_list[1])
print(country_list[2])
