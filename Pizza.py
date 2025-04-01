
import random

import time

points = 0

pizzas = ['Margarita', 'Pepperoni', 'Pineapple-veggie', 'Cheese']

margarita_ingredients = {'dough', 'basil', 'mozzarella', 'sauce'}
pepperoni_ingredients = {'dough', 'cheese', 'pepperoni', 'sauce'}
pineapple_veggie_ingredients = {'dough', 'veggies', 'pineapple', 'cheese', 'sauce'}
cheese_ingredients = {'dough', 'cheese', 'sauce'}

ingredients = """Ingredients
––––––––––––
Dough
Cheese
Pepperoni
Pineapple
Basil
Mozzarella
Veggies
Sauce"""

def makepizza():
    global points, random_pizza
    print(f"\nWelcome to {shop_name}!")
    time.sleep(1)
    print(f"Hi! Can I get a {random_pizza} pizza?")
    time.sleep(1)
    print(f"One {random_pizza} pizza coming right up!")
    print("""
Order:""", random_pizza)
    print(ingredients)

    while True:
        ingredients_used_str = input('''
What ingredients do you use to make their order?''')
        ingredients_used = set(ingredient.lower().strip() for ingredient in ingredients_used_str.split()) # Split on spaces
        if all(ingredient in {'dough', 'cheese', 'pepperoni', 'pineapple', 'basil', 'mozzarella', 'veggies', 'sauce'} for ingredient in ingredients_used):
            break
        else:
            print("Invalid ingredients. Please use only the listed ingredients, separated by spaces.")


    if ingredients_used == margarita_ingredients and random_pizza == 'Margarita':
        # ... (rest of the if/elif/else structure - same logic as before, but using sets)
        print('Into the oven goes the pizza.')
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('Ding!')
        print('That looks exactly like a', random_pizza, 'pizza! Thanks!')
        print('Plus 1 point!')
        points += 1
    elif ingredients_used == pepperoni_ingredients and random_pizza == 'Pepperoni':
        print('Into the oven goes the pizza.')
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('Ding!')
        print('That looks exactly like a', random_pizza, 'pizza! Thanks!')
        print('Plus 1 point!')
        points += 1
    elif ingredients_used == pineapple_veggie_ingredients and random_pizza == 'Pineapple-veggie':
        print('Into the oven goes the pizza.')
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('Ding!')
        print('That looks exactly like a', random_pizza, 'pizza! Thanks!')
        print('Plus 1 point!')
        points += 1
    elif ingredients_used == cheese_ingredients and random_pizza == 'Cheese':
        print('Into the oven goes the pizza.')
        time.sleep(2)
        print('...')
        time.sleep(1)
        print('Ding!')
        print('That looks exactly like a', random_pizza, 'pizza! Thanks!')
        print('Plus 1 point!')
        points += 1
    else:
        print('Into the oven goes the pizza.')
        time.sleep(0.5)
        print('...')
        time.sleep(0.3)
        print('Ding!')
        print("That doesn't really look like a", random_pizza, 'pizza, but I will eat it.')
    time.sleep(2)
    return points


player_name = input('What\'s your name?')
shop_name = input(f'What should the name of our pizza shop be, {player_name}?')

print(f'Well {player_name}, let\'s get making!')

time.sleep(0.5)

random_pizza = random.choice(pizzas)
makepizza()

random_pizza = random.choice(pizzas)
makepizza()

random_pizza = random.choice(pizzas)
makepizza()

print('Your final score is:', points)

print('Thanks for playing!')
