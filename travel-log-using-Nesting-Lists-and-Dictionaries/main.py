capital = {"france" : ["paris","amsterdam","lille"]
						,"germany" : ["berlin","hamburg","stuggert"]
}
print(capital["france"][0]) # retriving paris using nested dict and list using key
#  nest dict inside dict
travel_log = {
						"france" : {"cities_visited" : ["paris","amsterdam","lille"],"total_visit" : 4}
						,"germany" : {"cities_visited":["berlin","hamburg","stuggert"],"total_visit" : 4}
}
print(travel_log["germany"]["cities_visited"][2],{"total_visit"})

print(travel_log["germany"]
["total_visit"])

# nest dict inside list

travel_log2 = [
{"contry":"france" , 
"cities_visited" : ["paris","amsterdam","lille"],"total_visit" : 4},
{"contry" : "germany" ,
"cities_visited":["berlin","hamburg","stuggert"],"total_visit" : 4}
]
print(travel_log2[0]["contry"])