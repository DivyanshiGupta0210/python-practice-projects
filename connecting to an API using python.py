# API = Application Programming Interface

import requests
base_url = "https://pokeapi.co/api/v2"
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
#response code: like 404 Not Found, we need 200 OK
    # print(response)
    if response.status_code == 200:
        # print("Data retrieved!")
        pokemon_data = response.json() #assigning file type for py dict type key:value pairs
        return(pokemon_data)
    else:
        print(f"Failed to retrieve data. ERROR {response.status_code}")

pokemon_name = input("Enter the name of desired Pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: 
    print(f"Name: {pokemon_info["name"].capitalize()}") #for first letter to be capital
    print(f"ID: {pokemon_info["id"]}") 
    print(f"Height: {pokemon_info["height"]}") 
    print(f"Weight: {pokemon_info["weight"]}") 