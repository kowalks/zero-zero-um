import game
import screens

while True:
    my_game = game.Game()
    title_screen = screens.TitleScreen()
    title_screen.run(my_game.running)