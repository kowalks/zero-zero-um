import game
import screens

my_game = game.Game()
title_screen = screens.TitleScreen()
title_screen.run(my_game.running)
my_game.close()