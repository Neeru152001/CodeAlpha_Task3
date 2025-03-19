import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.root.geometry("400x400")
        self.root.configure(bg="light blue")

        self.card_values = list('AABBCCDDEEFFGGHH')
        random.shuffle(self.card_values)

        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.start_time = time.time()
        self.time_limit = 90  #90 seconds time for finish game

        self.create_buttons()
        self.timer_label = tk.Label(root, text='Time Left:90s', font=('Helvetica', 14), bg='light blue')
        self.timer_label.grid(row=5, column=0, columnspan=4, pady=10)
        self.update_timer()


    def create_buttons(self):
        """Create the 4x4 grid of buttons for the puzzle."""
        for i in range(4):
            row=[]
            for j in range(4):
                btn = tk.Button(self.root, text='?', width=8, height=4, command=lambda x=i,y=j:self.flip_card(x,y))
                btn.grid(row=i, column=j,padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)


    def flip_card(self,x,y):
        """Handles flipping of cards and matching logic."""
        current_button = self.buttons[x][y]
        if current_button['state'] == 'disabled' or self.first_card==(x,y):
            return #ignore already matched or same card clicks
        
        current_button['text'] = self.card_values[x * 4 + y]
        if not self.first_card:
            self.first_card = (x,y)
        elif not self.second_card:
            self.second_card = (x,y)
            self.check_match()


    def check_match(self):
        """Checks if the two selected cards are a match"""
        x1, y1 = self.first_card
        x2, y2 = self.second_card


        if self.card_values[x1 * 4 + y1] == self.card_values[x2 * 4 + y2]:
            self.buttons[x1][y1]['state'] = 'disabled'
            self.buttons[x2][y2]['state'] = 'disabled'
        else:
            self.root.after(1000, lambda:self.hide_cards(x1,y1,x2,y2))

        self.first_card = None
        self.second_card = None
        if all(btn['state']=='disabled' for row in self.buttons for btn in row):
            self.game_won()

    
    def hide_cards(self,x1,y1,x2,y2):
        """Hide unmatched cards after delay."""
        self.buttons[x1][y1]['text'] = '?'
        self.buttons[x2][y2]['text'] = '?'


    def update_timer(self):
        """Time countdown logic"""
        time_left = self.time_limit - int(time.time() - self.start_time)
        if time_left > 0:
            self.timer_label.config(text=f"Time Left: {time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.game_over()


    def game_won(self):
        """Display winning message."""
        messagebox.showinfo("Congratulations!", "You've matched all pairs successfully!")
        self.root.destroy()

    
    def game_over(self):
        """Display game over message time runs out."""
        messagebox.showerror("Game Over", "Time's up! Better Luck Next Time.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()

