from src.content import BLOCK_END, NEW_LINE
from src.model.canvas import Canvas


class Renderer:
    """
    Renders a canvas
    """

    _canvas: Canvas

    def __init__(self, canvas: Canvas):
        """
        Initializes the class

        :param canvas: The canvas to render
        """
        self._canvas = canvas

    def render(self, ctx):
        """
        Renders the ascii characters from the canvas, sending a formatted discord message with the given ctx

        :param ctx: The context needed to send a discord message
        """
        ctx.send(BLOCK_END + NEW_LINE + self._canvas.render() + BLOCK_END)

    def render_to_console(self):        # TODO: for testing
        """
        Renders the ascii characters from the canvas, sending a formatted console message
        """
        print(BLOCK_END + NEW_LINE + self._canvas.render() + BLOCK_END)
