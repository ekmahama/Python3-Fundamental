class Animal(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def GetName(self):
        return self._name
    def GetAge(self):
        return self._age
    def speak(self):
        print("I am an animal")
    def walk(self):
        print("I am walking")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def Bark(self):
        print("Wo Wo Wo")
    def speak(self):
        super().speak() # use the speak method from animal
        print("I am a dog")
    def walk(self): # Overriding walk method.
        print("I walk like a dog.")

if __name__=="__main__":
    test = Animal("nam1",2)
    print(f"Age: {test.GetAge()}")
    print(f"Name: {test.GetName()}")
    test.GetName()
    test.speak()
    test.walk()

    print("===============================")
    dog = Dog("terror", 3)
    dog.Bark()
    dog.speak()
    dog.walk()

        