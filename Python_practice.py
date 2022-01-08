counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]


#for county, voters in counties_dict.items():
    #print(county + " county has " +  str(voters) + " registered voters.")

#for county_dict in voting_data:
    #print(county_dict)

#for i in range(len(voting_data)):
    #print(voting_data[i])

#for county_dict in voting_data:
    #for value in county_dict.values():
       # print(value)

#for county_dict in voting_data:
    #print(county_dict["county"])


#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters")

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']} registered voters")
