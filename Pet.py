import sys
import os
import random
import time

outside_time = 8
food_time = 10

def p(words):
    print(words)

# More descriptive variable name
possible_attacks = ['you', 'another dog', 'a squirrel']
possible_weather = ['raining', 'thunderstorming', 'clear', 'clear', 'clear', 'clear', 'cloudy', 'snowing', 'foggy']
weather_choices = ['Y', 'Y', 'Y', 'N']  # Renamed for clarity

def bark(at):
    if at == 'player':
        p(f'{dog_name} is barking at you.')
    elif at == 'other dog':
        p(f'{dog_name} is barking at another dog.')
    elif at == 'squirrel':
        p(f'{dog_name} is barking at a squirrel.')
    elif at == 'rand':
        p(f'{dog_name} is barking at {random.choice(possible_attacks)}.')
    else:
        p(f'INTERNAL ERROR: {at} is not defined.')

def weatherchange(wweather):
    global WEATHER  # Important: Declare WEATHER as global when modifying it
    if wweather == 'rain':
        WEATHER = 'raining'
    elif wweather == 'tstorm':
        WEATHER = 'thunderstorming'
    elif wweather == 'clear':
        WEATHER = 'clear'
    elif wweather == 'cloudy':
        WEATHER = 'cloudy'
    elif wweather == 'snow':
        WEATHER = 'snowing'
    elif wweather == 'rand':
        choice = random.choice(weather_choices)  # Use a better variable name
        if choice == 'Y':
            WEATHER = random.choice(possible_weather)
        elif choice == 'N':  # Handle the 'N' case explicitly
            pass  # Keep WEATHER the same (no need to do anything)
        else:
            p(f'INTERNAL ERROR: {choice} is not defined.')
    elif wweather == 'fog':
        WEATHER = 'foggy'
    else:
        p(f'INTERNAL ERROR: {wweather} is not defined.')

def inside():
    global outside_time, food_time  # Declare globals
    os.system('cls' if os.name == 'nt' else 'clear')
    p('You are inside.')
    p(f'It is {WEATHER} outside.')
    if food_time == 0 or outside_time == 0:
        bark('player')
    action = input('What do you want to do? ')  # Added space for better input

    if action == f'feed {dog_name}':
        p(f'You fed {dog_name}.')
        weatherchange('rand')
        food_time = 10
        outside_time -= 1
        inside()

    elif action == 'go outside':
        food_time -= 1
        outside()

    elif action == f'play with {dog_name}':
        p(f'You played with {dog_name}.')
        outside_time -= 1
        food_time -= 1
        inside()

    elif action == f'put {dog_name} in their crate':
        p(f'You put {dog_name} in their crate.')
        weatherchange('rand')
        outside_time -= 1
        food_time -= 1
        action = input('What do you want to do? ') # Added space

        if action == f'let {dog_name} out of their crate':
            p(f'You let {dog_name} out of their crate.')
            inside()

        elif action == 'sleep':
            p('Zzz...')
            time.sleep(2)  # Reduced sleep time for testing
            p(f'You let {dog_name} out of their crate.')
            inside()
        else:
            p("You can't do that")
            inside()

    else:
        p("You can't do that.") # Added period for consistency
        inside()

def outside():
    global food_time, outside_time  # Declare globals
    os.system('cls' if os.name == 'nt' else 'clear')
    p('You are outside.')
    p(f'It is {WEATHER}.')
    if food_time == 0 or outside_time == 0:
        bark('player')
    action = input('What do you want to do? ') # Added space

    if action == f'walk {dog_name}':
        bark('squirrel')
        p(f'You walked {dog_name}.')
        weatherchange('rand')
        outside_time = 8
        food_time -= 1
        outside()

    elif action == 'go inside':
        outside_time -= 1
        food_time -= 1
        inside()

    elif action == f'play with {dog_name}':
        p(f'You played with {dog_name}.')
        outside_time = 8
        food_time -= 1
        outside()

    elif action == f'let {dog_name} off the leash':
        p(f'You let {dog_name} off the leash in your backyard.')
        weatherchange('rand')
        outside_time = 8
        food_time -= 1
        outside()
    else:
        p("You can't do that.")
        outside()


# ALERT
input('Part of this software is missing. Please alert Elijah if there are any issues.')

# GAME
p('Hello!')
WEATHER = 'clear'  # Initialize WEATHER
player_name = input('What is your name? ') # Added space
p(f'Hi, {player_name}!')
dog_name = input('What is the name of your dog? ') # Added space
inside()
