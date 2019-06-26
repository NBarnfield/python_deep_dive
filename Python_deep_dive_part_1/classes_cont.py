class Lighting:
    def __init__(self, name: str, colour: str, electricity: int):
        self.name = name
        self.colour = colour
        self.electricity = electricity

    def __str__(self):
        return 'The {0} colour is {1} and takes {2} volts'.format(self.name, self.colour, self.electricity)

    def light_on(self):
        print('---------------------------------')
        print('Lighting turned on')

    def light_off(self):
        print('---------------------------------')
        print('Light turning off')

    # The __repr__ magic method provides clarity on how the instance was instantiated
    def __repr__(self):
        return 'Lighting({0}, {1})'.format(self.name, self.colour)

    # The __eq__ magic method allows comparison of two instances
    # Without overloading the eq method the function will compare memory addresses which will prove false
    # rather than the values they are associated with.
    def __eq__(self, other):
        if isinstance(other, Lighting):
            return self.colour == other.colour and self.electricity == other.electricity
        else:
            return False


dmx_1 = Lighting('dmx_1', 'white', 440)

str(dmx_1)

dmx_1

dmx_2 = Lighting('dmx_2', 'purple', 440)

# As they have different memory addresses and are different instances this must necessarily be true.
dmx_1 is not dmx_2

dmx_3 = Lighting('dmx_3', 'white', 440)

dmx_1 == dmx_3

dmx_1 == 100

