from src.model.canvas import Canvas
from src.model.sprite import Sprite
from src.ui.renderer import Renderer


def main():
    canvas = Canvas(25, 6)
    renderer = Renderer(canvas)

    character = Sprite('$')
    horizontal_wall = Sprite('_')
    vertical_wall = Sprite('|')

    for i in range(1, canvas.width - 1):
        canvas.draw(horizontal_wall, i, 0)
        canvas.draw(horizontal_wall, i, canvas.height - 1)

    for i in range(1, canvas.height):
        canvas.draw(vertical_wall, 0, i)
        canvas.draw(vertical_wall, canvas.width - 1, i)

    canvas.draw(character, int(canvas.width / 2), int(canvas.height / 2))
    print(str([character, horizontal_wall, vertical_wall]))
    renderer.render_to_console()


if __name__ == "__main__":
    main()
