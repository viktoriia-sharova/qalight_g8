class Human:
    def __init__(self, age):
        self.age = age
        self.favourite_drink = 'beer'

    def drink(self):
        if self.age < 18:
           self.favourite_drink = 'juice'
        print(f"Human likes to drink {self.favourite_drink}")
human = Human(age=22)
human.drink()
human = Human(age=17)
human.drink()

class Worker(Human):
    def __init__(self, age,salary):
        super().__init__(age)
        self.salary = salary
        if self.salary > 1000:
            self.favourite_drink = 'whiskey'

worker = Worker(age=30,salary=2000)
print("Human likes to drink", worker.favourite_drink)
worker.drink()