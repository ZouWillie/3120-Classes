class Animal:
    def __init__(self, name): 
        self._name = name
        print("Hello, I am", self._name)

    def talk(self):
        print("Hi, I am a animal")

    def eat(self, eat):
        self._eat = eat
        print("I am eating a", self._eat)

    def species(self, species):
        self._species = species
        print("I am a", self._species)

    def sleep(self, sleeping):
        self._sleep = sleeping
        print("I am sleeping in a", self._sleep)

    def fight(self, fight):
        self._fight = fight
        print("I am fighting a ", self._fight)

    def flee(self, escape):
        self._escape = escape
        print("I am escaping from a", self._escape)