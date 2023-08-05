boardgame aims to gather several simple boardgames like TicTacToe or Connect 4

Home-page: UNKNOWN
Author: Surya Ambrose
Author-email: surya.ambrose@gmail.com
License: MIT
Description: 
        boardgame aims to gather several simple boardgames like TicTacToe or Connect 4
        
        Each game is described by a State and a Model. A State represents the current
        state of the game (obviously) but can also provide a value for that state. This
        value is helpful for AI playing the game. A Model represents the rules of the
        game and is used to describe which moves are possible from a given state, and
        what would be their resulting states.
        
        Aside of those two elements is a Viewer, whose purpose is to display the
        current state of the game and to handle human actions.
        
        Above all this, a Controller handles the state, the model, the player actions
        returned by the viewer or the AI actions to run the game. This Controller is
        generic and does not need to be overwritten for each game.
        
Platform: UNKNOWN
Classifier: Development Status :: 2 - Pre-Alpha
Classifier: Environment :: Console
Classifier: Intended Audience :: Developers
Classifier: Intended Audience :: End Users/Desktop
Classifier: License :: OSI Approved :: MIT License
Classifier: Programming Language :: Python :: 2.7
Classifier: Topic :: Games/Entertainment :: Board Games
