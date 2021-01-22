travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(contry,visit,city):
	new_log = {}
	new_log["contry"] = contry
	new_log["visits"] = visit
	new_log["cities"] = city
	travel_log.append(new_log)
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 50, ["Mumbai", "Pune"])
print(travel_log)



