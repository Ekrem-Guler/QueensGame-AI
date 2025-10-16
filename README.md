# Linkedin's Queens Game - Making - Backtracking Solving 

This repository contains my implementation of the **Queens Game** from LinkedIn — a variation of the classic **N-Queens Problem**.  
The goal of the game is to place queens on a chessboard so that no two queens attack each other.

I built this project completely in **Python**, with a **backtracking-based solver**, and a **text-based (array) interface** — no GUI required.

---

## 🧩 Problem Description

The challenge:
> Place N queens on an N×N chessboard so that no two queens share the same row, column, or diagonal.

This is a famous example of a **constraint satisfaction problem**, often solved using **recursive backtracking**.

---

## 💡 How I Built It

I built this project in several steps: 

###### You can see more detail explains on the main.py

1. **Board Representation:**  
   I used a 2D list (`table_arr[i][j]`) to represent the chessboard, where:
   - `1001` means there’s a queen,
   - `0` means the square is empty.
   - `-1` means wrong points.

2. **Safety Check Function:**  
   I wrote a function `win_or_not(choice_x,choice_y,table_arr,player_game)` that checks:
   - same column or row
   - digaonals
   - colors

3. **Backtracking Algorithm:**  
   The main solver function tries to place queens row by row:
   - If a position is safe → place the queen and recurse to the next row.
   - If the position fails → backtrack (remove queen recurse the table) and try the next column.

4. **Game Logic:**  
   I also implemented a simple "play" mode where users can input positions as arrays, and the game checks if your configuration is valid.

---

## ⚙️ Features

- Play manually by entering queen positions  
- Automatic solver using backtracking  
- Works for any N×N board  
- Clean and readable Python code
---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   gh repo clone Ekrem-Guler/QueensGame-Making-BacktrackingSolving
   cd QueensGame-Making-BacktrackingSolving
