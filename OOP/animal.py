class Animal:
    pass


class Duck:
    def __init__(self, animal_type):    
        self.aminal_type = None
        self.name = "Donald"
    
    def say(self):
        print("Duck Duck")

    def get_name(self):
        return self.name

def main():
    duck = Duck(animal_type="fly")
    print(duck.get_name())

if __name__ == '__main__':
    main()