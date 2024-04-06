"""
Codewars Coding Challenge

Day 99/366

Level 8kyu

Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"

https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
"""

def rps(p1, p2):
    # Tentukan aturan Gunting Kertas Batu
    rules = {
        'rock': {'rock': 'Draw!', 'paper': 'Player 2 won!', 'scissors': 'Player 1 won!'},
        'paper': {'rock': 'Player 1 won!', 'paper': 'Draw!', 'scissors': 'Player 2 won!'},
        'scissors': {'rock': 'Player 2 won!', 'paper': 'Player 1 won!', 'scissors': 'Draw!'}
    }
    
    # Mengembalikan hasil berdasarkan pilihan pemain 1 dan pilihan pemain 2
    return rules[p1][p2]