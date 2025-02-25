class Animal:
    def __init__(self, animal, name, sex, traits, aggression):
        self.animal = animal
        self.name = name
        self.sex = sex
        self.traits = traits
        self.aggression = aggression

    def type(self):
        print(f"I am a {self.animal}")

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