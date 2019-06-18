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
