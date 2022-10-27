from ascii_renderer.screen import Screen
from ascii_renderer.renderer import Renderer
from ascii_renderer.char import Char


def main():
    screen = Screen(25, 6)
    renderer = Renderer(print, screen)

    character = Char('$')
    horizontal_wall = Char('_')
    vertical_wall = Char('|')

    for i in range(1, screen.width - 1):
        screen.draw(horizontal_wall, i, 0)
        screen.draw(horizontal_wall, i, screen.height - 1)

    for i in range(1, screen.height):
        screen.draw(vertical_wall, 0, i)
        screen.draw(vertical_wall, screen.width - 1, i)

    screen.draw(character, int(screen.width / 2), int(screen.height / 2))
    renderer.render()


if __name__ == "__main__":
    main()
