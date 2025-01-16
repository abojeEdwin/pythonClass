def find_Country(country,state):
    countries = {"USA": {"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
                 "Canada": {"Onatario": {"Toronto": 2930000, "Ottawa": 994837}}
                 }
    for state in countries.values():
        cities = state["California"]
        print(f'The population of', state["California"])
            #cities = country["California"]
            #return cities
    #for state in countries.values():
     #   cities = state["Onatario"]["Toronto"]
      #  print(f'The population of is', state["Onatario"])

country = input("Enter country :")
state = input("Enter state :")

answer = find_Country(country,state)