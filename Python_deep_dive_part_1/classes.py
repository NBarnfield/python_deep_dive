class coffee:

    def __init__(self, name: str, milk: str):
        coffee.name = name
        coffee.milk = milk

    def brew(self):
        print('---------------------------------')
        print('You would like a {0} on {1} milk.'.format(coffee.name, coffee.milk))


# Create the first object from the coffee class
full_cream_latte = coffee('latte', 'full cream')
full_cream_latte.brew()

# Create the second object from the coffee class
skim_flat_white = coffee('flat white', 'skim')
skim_flat_white.brew()


class Lighting:

    def __init__(self, name: str, colour: str):
        Lighting.name = name
        Lighting.colour = colour

    def light_on(self):
        print('---------------------------------')
        print('Lighting turned on')

    def light_off(self):
        print('---------------------------------')
        print('Light turning off')


dmx_1 = Lighting('dmx_1', 'white')
dmx_1.light_on()
dmx_1.light_off()
