import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.coin_results = {"HEADS": 0, "TAILS": 0}
        self.die_results = {i: 0 for i in range(1, 7)}
    def flip_coin(self):
        return random.choice(["HEADS", "TAILS"])
    def roll_die(self):
        return random.randint(1, 6)

    def ultra_permutation(self, num_tosses,num_rolls):
        for _ in range(num_tosses):
            self.flip_coin()
            for _ in range(num_rolls):
                self.roll_die()
                if isinstance(self.chosen_side[0],str) and isinstance(self.chosen_side[1],int):
                    self.score += 1

    def simulate_coin_tosses(self, num_tosses):
        for _ in range(num_tosses):
            result = self.flip_coin()
            self.coin_results[result] += 1
        print(f"{self.name} flipped the coin {num_tosses} times: {self.coin_results['HEADS']} HEADS, {self.coin_results['TAILS']} TAILS.")
    
    def simulate_die_rolls(self, num_rolls):
        for _ in range(num_rolls):
            result = self.roll_die()
            self.die_results[result] += 1
        print(f"{self.name} rolled the die {num_rolls} times: {self.die_results}.")

    def choose(self,option):
        if option in ["HEADS", "TAILS",1,2,3,4,5,6]:
            self.chosen_side = option
        else:
            raise ValueError("Invalid side. Choose 'HEADS' or 'TAILS' or a die roll (1-6).")
    
    def calculate_score(self):
        if hasattr(self, 'chosen_side'):
            if isinstance(self.chosen_side, str):
                self.score = self.coin_results[self.chosen_side]
            else:
                self.score = self.die_results[self.chosen_side]
        else:
            raise ValueError("No side chosen. Use choose() method first.")

class Store:
    def __init__(self,player:Player):
        self.player = player
        self.items = {"Extra Toss": 10, "Double Score": 20}
        self.purchased_items = []
    
    def buy_item(self, item_name):
        if item_name in self.items:
            cost = self.items[item_name]
            if self.player.score >= cost:
                self.player.score -= cost
                self.purchased_items.append(item_name)
                print(f"{self.player.name} purchased {item_name} for {cost} points.")
            else:
                print(f"Not enough points to purchase {item_name}.")
        else:
            print(f"Item {item_name} not found in store.")
    
    def buff(self):
        for item in self.purchased_items:
            if item == "Extra Toss":
                self.player.simulate_coin_tosses(5)  # Simulate 5 extra tosses
            elif item == "Double Score":
                self.player.score *= 2  # Double the score

p1 = Player("Alice")
p1.simulate_die_rolls(10**6)
p1.choose(("HEADS",1))
p1.calculate_score()
store = Store(p1)
store.buy_item("Double Score")
score_before_buff = p1.score
store.buff()
score_after_buff = p1.score
print(f"Score before buff: {score_before_buff}, Score after buff: {score_after_buff}")
