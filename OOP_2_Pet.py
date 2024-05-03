class Dog:
    def __init__(self, name, age, weight, is_male):
        self.name = name 
        self.age = age 
        self.weight = weight
        self.is_male = is_male #Boolean. True if Male, Flase if Female

my_dog = Dog("Moe", 1, 5, False)

print (f"My dog is named {my_dog.name} and she is {my_dog.age} year old. She weighs {my_dog.weight}lbs.")

