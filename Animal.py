class Animal:
    def __init__(self,AnimalType,Name,Gender,FavoriteMeal,PersonalityTrait): 
        self.__AnimalType=AnimalType
        self.__Name=Name
        self.__Gender=Gender
        self.__FavoriteMeal=FavoriteMeal
        self.__PersonalityTrait=PersonalityTrait
        
        
    def type(self):
        print(f"I am a {self.__AnimalType}")

    def NameLiking(self, liking):
        if liking == "Yes":
             print(f"My name is {self.__Name}")
        elif liking == "yes":
            print(f"My name is {self.__Name}")
        else: 
            Name= input("What would you want your name to be:")
        

    def love(self,attraction):
        print(f"I identify as a {self.__Gender} and I am attracted to {attraction}")

    def favorite_meals(self, other):
        print (f"My favorite meal to eat is {self.__FavoriteMeal}")
        print (f"I also enjoy {other}")

    def PersonalityTrait(self):
        print(f"I act {self.__PersonalityTrait}")
        reasoning=input("Why act like this?")
    
