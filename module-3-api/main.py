import requests
import random

pokemon_list = ["pikachu", "eevee", "snorlax", "fennekin", "bulbasaur"]

while True:
    pokemon = random.choice(pokemon_list)

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        abilities = data["abilities"]

        print("WHO'S DAT POKEMON!")
        print("Guess Pokemon [pikachu - eevee - snorlax - fennekin - bulbasaur]!")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Ability: {abilities[0]["ability"]["name"]}")
        print("Only 3 Attempts to guess!")

        for attempt in range(3):
            print(f"Attempts: {attempt}/3")
            guess = input("I choose you! (lowercase only): ")
            if guess not in pokemon_list:
                print("Invalidd Pokemon!!!")
            elif guess == name:
                print("Correct! You guessed the pokemon! \n")
                break
            else:
                print("Wrong! Try again. \n")
        else:
            print("Game Over!")
            print(f"Its: {name}")

        while True: 
            choice = input("Guess Again? [1-Yes/2-No]: ")
            if choice == "1":
                break
            elif choice == "2":
                print("Okay! Thanks for guessing!")
                exit()
    else:
        print("Error!")
        break