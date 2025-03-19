# CodeAlpha_Task3 <br>
## Memory Puzzle Game Using Python (Tkinter)<br>

# 📌 Introduction<br>
The Memory Puzzle Game is a fun and interactive puzzle game built using Python and the Tkinter library. In this game, players are<br>
presented with a 4x4 grid of cards, each hiding a letter. The goal is to match all pairs of cards within the given time limit of <br>
90 seconds.<br>
This project is ideal for beginners learning GUI development in Python using Tkinter and includes key concepts like:<br>
✅ Tkinter widgets (Buttons, Labels)<br>
✅ Randomization for card placement<br>
✅ Timer implementation using Tkinter's .after() method<br>
✅ Game logic for card matching<br>
✅ User interaction via message boxes (Win or Lose)<br>


# ⚙️ Features<br>
🎯 4x4 Grid: A grid containing 16 cards with 8 matching pairs.<br>
🕒 Timer: Players must match all pairs within 90 seconds.<br>
🔄 Random Card Arrangement: Cards are shuffled randomly at the start of each game.<br>
✅ Win Condition: A congratulatory message appears upon successful completion.<br>
❌ Lose Condition: If the timer runs out before matching all pairs, the player loses.<br>
🔥 Interactive UI: Easy-to-use interface with clean design and intuitive gameplay.<br>


# 🎮 How to Play<br>
1. Launch the game — A 4x4 grid will appear with cards marked as ?.<br>
2. Click a card to reveal its value.<br>
3. Click another card to find its match.<br>
4. If both cards match, they remain revealed and are disabled.<br>
5. If they don’t match, they will flip back after 1 second.<br>
6. Match all pairs within 90 seconds to win the game.<br>
7. If the timer runs out before all pairs are matched, you lose.<br>


# 🧱 Code Explanation<br>
## 1. Import Libraries<br>
• tkinter — Used for creating the GUI.<br>
• messagebox — Provides pop-up messages for win/lose alerts.<br>
• random — Used for shuffling the card values.<br>
• time — Utilized for implementing the countdown timer.<br>

## 2. Class Initialization (__init__ Method)<br>
• The class initializes the Tkinter window.<br>
• The card values are shuffled randomly for each game session to ensure uniqueness.<br>

## 3. Creating the Game Board<br>
• The grid consists of 16 buttons arranged in a 4x4 pattern.<br>
• Each button has a ? indicating a hidden card.<br>

## 4. Card Flipping Logic<br>
• Ensures players can’t click already matched cards or select the same card twice.<br>
• Reveals the value of the clicked card.<br>

## 5. Matching Logic<br>
• Matches the selected cards by comparing their values.<br>
• If the cards don't match, they are hidden again after 1 second.<br>

## 6. Timer Implementation<br>
• The timer starts at 90 seconds.<br>
• The .after() method updates the timer every second.<br>
• If time runs out, the player loses.<br>

## 7. Win/Loss Conditions<br>
• If all cards are matched before the timer ends, a "Congratulations" message appears.<br>
• If time expires before matching all pairs, the game ends with a "Game Over" message.<br>


# 💡 Key Learning Outcomes<br>
By completing this project, you will enhance your skills in: <br>
✅ Python programming.<br>
✅ Tkinter GUI design.<br>
✅ Game logic implementation.<br>
✅ Working with event-driven programming.<br>
✅ Managing timers and controlling game states.<br>


# 🔧 Future Improvements<br>
Here are some ideas to expand the project:<br>
✅ Add difficulty levels with larger grids (e.g., 5x5 or 6x6).<br>
✅ Introduce score tracking based on time remaining.<br>
✅ Add sound effects for better engagement.<br>
✅ Implement a leaderboard to record top scores.<br>
✅ Add hints or limited attempts for extra challenge.<br>


# 🤝 Contributing<br>
Contributions are welcome! If you’d like to improve the game, please:<br>
• Fork the repository.<br>
• Create a new branch for your feature.<br>
• Submit a pull request for review.<br>


# 📝 License<br>
This project is open-source and available under the MIT License.<br>


# 📩 Contact<br>
• Email : neerukct15@gmail.com<br>
• github : https://github.com/Neeru152001<br>

# ⭐ Support<br>
If you found this project helpful, don't forget to leave a ⭐ on the repository!<br>


# ✅ Enjoy Playing the Memory Puzzle Game! 🎯<br>

