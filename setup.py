from distutils.core import setup
import py2exe

setup(
    version = "1.0.0",
    description = "A Tic-Tac-Toe game written in Python",
    name = "Doyler's Tic-Tac-Toe v1.0",

    console = ["tictactoe.py"],
)
