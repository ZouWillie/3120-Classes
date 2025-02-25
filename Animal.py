class Animal:
    def __init__(self, animal, name, sex, traits, aggression):
        self.animal = animal
        self.name = name
        self.sex = sex
        self.traits = traits
        self.aggression = aggression

    def type(self):
        print(f"I am a {self.animal}")

    def eat(self, food):
        print(self.__name, "is eating", food)

    def sleep(self):
        print(self.__name, "is sleeping")

    def move(self):
        print(self.__name, "is moving around")

    def play(self):
        print(self.__name, "is playing")


    def fight(self, fight):
        self._fight = fight
        print("I am fighting a ", self._fight)

    def flee(self, escape):
        self._escape = escape
        print("I am escaping from a", self._escape)
  
    def favorite_meals(self, other):
        print (f"My favorite meal to eat is {self.__FavoriteMeal}")
        print (f"I also enjoy {other}")


    def NameLiking(self, liking):
        if liking.lower() == "yes":
            print(f"My name is {self.name}")
        else:
            self.name = input("What would you want your name to be?")

    def love(self, attraction):
        print(f"I identify as a {self.sex} and I am attracted to {attraction}")

    def show_traits(self, other):
        print(f"My traits are {self.traits}")
        print(f"I'm also {other}")

    def show_aggression(self):
        print(f"I act {self.aggression}")
        reasoning = input("Why do I act this way?")