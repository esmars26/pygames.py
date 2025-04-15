import random
global points
points = 0

#Removed excessive whitespace from transfer

United_States = '50 stars.'
Trinidad_Tobago = 'Red, with a white and black diagonal.'
Seychelles = 'Five diagonal bands of blue, yellow, red, white, and green.'
Holy_See = 'Yellow and white with keys.'
Romania = 'Blue, yellow , red.'
South_Sudan = 'Black, red, green, and blue triangle.'
United_Arab_Emirates = 'Green, white, black one way, red the other.'
Mozambique = 'Rifle, hoe, book.'
Belgium = 'Black, yellow, red.'
Brunei = 'Royal umbrella, wings of four feathers, upraised hands, crescent moon.'



Countries = [United_States, Trinidad_Tobago, Seychelles, Holy_See, Romania, South_Sudan, United_Arab_Emirates, Mozambique, Belgium, Brunei]


def game():
    global points
    for _ in range(10):
        country = random.choice(Countries)
        print(country)
        if country == United_States:
            guess = input()
            if guess == 'United States':
                print('Nice!')
                points = points+3
            if guess != 'United States':
                print('Try again.')
                guess = input()
                if guess == 'United States':
                    print('Good.')
                    points = points+2
                if guess != 'United States':
                    print('Try again.')
                    guess = input()
                    if guess == 'United States':
                        print('Phew.')
                    if guess != 'United States':
                        print('Oops!')
                        print('The correct answer was United States')
                        

        elif country == Trinidad_Tobago:
            guess = input()
            if guess == 'Trinidad & Tobago':
                print('Nice!')
                points = points+3
            elif guess != 'Trinidad & Tobago':
                print('Try again.')
                guess = input()
                if guess == 'Trinidad & Tobago':
                    print('Good.')
                    points = points+2
                elif guess != 'Trinidad & Tobago':
                    print('Try again.')
                    guess = input()
                    if guess == 'Trinidad & Tobago':
                        print('Phew.')
                    elif guess != 'Trinidad & Tobago':
                        print('Oops!')
                        print('The correct answer was Trinidad & Tobago')


        elif country == Seychelles:
            guess = input()
            if guess == 'Seychelles':
                print('Nice!')
                points = points+3
            elif guess != 'Seychelles':
                print('Try again.')
                guess = input()
                if guess == 'Seychelles':
                    print('Good.')
                    points = points+2
                elif guess != 'Seychelles':
                    print('Try again.')
                    guess = input()
                    if guess == 'Seychelles':
                        print('Phew.')
                    elif guess != 'Seychelles':
                        print('Oops!')
                        print('The correct answer was Seychelles')
                        

        elif country == Holy_See:
            guess = input()
            if guess == 'Holy See':
                print('Nice!')
                points = points+3
            elif guess != 'Holy See':
                print('Try again.')
                guess = input()
                if guess == 'Holy See':
                    print('Good.')
                    points = points+2
                elif guess != 'Holy See':
                    print('Try again.')
                    guess = input()
                    if guess == 'Holy See':
                        print('Phew.')
                    elif guess != 'Holy See':
                        print('Oops!')
                        print('The correct answer was Holy See')
                        

        elif country == Romania:
            guess = input()
            if guess == 'Romania':
                print('Nice!')
                points = points+3
            elif guess != 'Romania':
                print('Try again.')
                guess = input()
                if guess == 'Romania':
                    print('Good.')
                    points = points+2
                elif guess != 'Romania':
                    print('Try again.')
                    guess = input()
                    if guess == 'Romania':
                        print('Phew.')
                    elif guess != 'Romania':
                        print('Oops!')
                        print('The correct answer was Romania')
                        

        elif country == South_Sudan:
            guess = input()
            if guess == 'South Sudan':
                print('Nice!')
                points = points+3
            elif guess != 'South Sudan':
                print('Try again.')
                guess = input()
                if guess == 'South Sudan':
                    print('Good.')
                    points = points+2
                elif guess != 'South Sudan':
                    print('Try again.')
                    guess = input()
                    if guess == 'South Sudan':
                        print('Phew.')
                    elif guess != 'South Sudan':
                        print('Oops!')
                        print('The correct answer was South Sudan')
                        

        elif country == United_Arab_Emirates:
            guess = input()
            if guess == 'United Arab Emirates':
                print('Nice!')
                points = points+3
            elif guess != 'United Arab Emirates':
                print('Try again.')
                guess = input()
                if guess == 'United Arab Emirates':
                    print('Good.')
                    points = points+2
                elif guess != 'United Arab Emirates':
                    print('Try again.')
                    guess = input()
                    if guess == 'United Arab Emirates':
                        print('Phew.')
                    elif guess != 'United Arab Emirates':
                        print('Oops!')
                        print('The correct answer was United Arab Emirates')
                        

        elif country == Mozambique:
            guess = input()
            if guess == 'Mozambique':
                print('Nice!')
                points = points+3
            elif guess != 'Mozambique':
                print('Try again.')
                guess = input()
                if guess == 'Mozambique':
                    print('Good.')
                    points = points+2
                elif guess != 'Mozambique':
                    print('Try again.')
                    guess = input()
                    if guess == 'Mozambique':
                        print('Phew.')
                    elif guess != 'Mozambique':
                        print('Oops!')
                        print('The correct answer was Mozambique')


        elif country == Belgium:
            guess = input()
            if guess == 'Belgium':
                print('Nice!')
                points = points+3
            elif guess != 'Belgium':
                print('Try again.')
                guess = input()
                if guess == 'Belgium':
                    print('Good.')
                    points = points+2
                elif guess != 'Belgium':
                    print('Try again.')
                    guess = input()
                    if guess == 'Belgium':
                        print('Phew.')
                    elif guess != 'Belgium':
                        print('Oops!')
                        print('The correct answer was Belgium')


        elif country == Brunei:
            guess = input()
            if guess == 'Brunei':
                print('Nice!')
                points = points+3
            elif guess != 'Brunei':
                print('Try again.')
                guess = input()
                if guess == 'Brunei':
                    print('Good.')
                    points = points+2
                elif guess != 'Brunei':
                    print('Try again.')
                    guess = input()
                    if guess == 'Brunei':
                        print('Phew.')
                    elif guess != 'Brunei':
                        print('Oops!')
                        print('The correct answer was Brunei')

    print()
    print(f'Points:{points}/30')

game()
