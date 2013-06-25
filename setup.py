from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "1.0.0",
    description = "A Tic-Tac-Toe game written in Python",
    name = "Doyler's Tic-Tac-Toe v1.0",

    # targets to build
    console = ["tictactoe.py"],
    )
