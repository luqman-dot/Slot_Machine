import random
import time

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "🔔", "⭐", "7"]
        self.reels = [self.symbols, self.symbols, self.symbols]
        self.balance = 10  # Initial balance for the player

    def spin_reels(self):
        return [random.choice(reel) for reel in self.reels]

    def display_reels(self, results):
        print("Spinning...\n")
        time.sleep(1)

        print(" | ".join(results))

    def check_winning(self, results):
        if results[0] == results[1] == results[2]:
            return True
        return False

    def play(self):
        while self.balance > 0:
            print(f"Current Balance: ${self.balance}")
            play = input("Press Enter to play (or type 'quit' to exit if you are a ckicken 🐔🐔): ")
            if play.lower() == 'quit':
                break

            self.balance -= 1  # Deduct the cost of one spin
            results = self.spin_reels()
            self.display_reels(results)

            if self.check_winning(results):
                win_amount = 10  # Define the win amount
                self.balance += win_amount
                print(f"You win! You got {results[0]} {results[1]} {results[2]}")
                print(f"New Balance: ${self.balance}\n")
            else:
                print("Booo you lose, You are so bad at this.\n")

        print("Game Over. You wasted all your money Betting. Get a job")

if __name__ == "__main__":
    slot_machine = SlotMachine()
    slot_machine.play()
