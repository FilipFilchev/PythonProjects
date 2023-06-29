# Singleton - Creational Pattern

class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton._instance = Singleton()
        return Singleton._instance

# Usage:
obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()
print(obj1 is obj2)  # Output: True


# Factory - Creational Pattern

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()

# Usage:
animal = AnimalFactory.create_animal('dog')
print(animal.speak())  # Output: Woof!


# Decorator - Structural Pattern

class Coffee:
    def get_cost(self):
        pass

    def get_description(self):
        pass

class PlainCoffee(Coffee):
    def get_cost(self):
        return 2.0

    def get_description(self):
        return "Plain Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_description(self):
        return self.decorated_coffee.get_description()

class MilkCoffee(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)

    def get_cost(self):
        return super().get_cost() + 0.5

    def get_description(self):
        return super().get_description() + ", Milk"

# Usage:
coffee = PlainCoffee()
coffee_with_milk = MilkCoffee(coffee)
print(coffee_with_milk.get_cost())  # Output: 2.5
print(coffee_with_milk.get_description())  # Output: Plain Coffee, Milk


# Observer - Behavioral Pattern

class Observer:
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

class MessagePublisher:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

# Usage:
publisher = MessagePublisher()
user1 = User("John")
user2 = User("Jane")

publisher.attach(user1)
publisher.attach(user2)

publisher.notify("Hello, World!")  # Output: John received message: Hello, World!
                                   #         Jane received message: Hello, World!

publisher.detach(user1)

publisher.notify("New message!")  # Output: Jane received message: New message!


# Strategy - Behavioral Pattern

class Strategy:
    def execute(self, x, y):
        pass

class AddStrategy(Strategy):
    def execute(self, x, y):
        return x + y

class SubtractStrategy(Strategy):
    def execute(self, x, y):
        return x - y

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, x, y):
        return self.strategy.execute(x, y)

# Usage:
add_strategy = AddStrategy()
calculator = Calculator(add_strategy)
result = calculator.execute_strategy(5, 3)
print(result)  # Output: 8

subtract_strategy = SubtractStrategy()
calculator.strategy = subtract_strategy
result = calculator.execute_strategy(5, 3)
print(result)  # Output: 2
