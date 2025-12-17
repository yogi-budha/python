class FlashCard:
    def __init__(self):
        self.fruits = {
            "Apple":"eed",
            "Banana":"yellow",
            "Orange":"orange"
        }
        self.fruit = ""
        self.play = 0
        print("Welcome to the fruits game!")
        self.random_choice()
        self.display()
        if(self.play == 0):
            self.play_game()
    
    def random_choice(self):
        import random
        self.fruit = random.choice(list(self.fruits.keys()))
    
    def display(self):
        print("what is the color of ",self.fruit," ?")
        value = input("")
        if(value == self.fruits[self.fruit]):
            print("Correct!")
        else:
            print("Wrong")
        
    def repeatgame(self):
        self.play = int(input("Enter 0 if you want to play again: "))
        if(self.play == 0):
            self.random_choice()
            self.display()
            self.play_game()
    
    def play_game(self):
        self.repeatgame()

obj = FlashCard()