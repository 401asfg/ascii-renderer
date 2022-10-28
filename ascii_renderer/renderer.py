from typing import Any, Callable, Coroutine

from ascii_renderer.screen import Screen


class Renderer:
    """
    Renders a screen
    """

    _send_to_output: Callable[[str], Coroutine[Any, Any, None]]
    _screen: Screen

    def __init__(self, send_to_output: Callable[[str], Coroutine[Any, Any, None]], screen: Screen):
        """
        Initializes the class

        :param send_to_output: The function used to send the given screen's render as a message when this class' render
        function is called
        :param screen: The screen to render to the output, specified in the given send_to_output function
        """
        self._send_to_output = send_to_output
        self._screen = screen

    async def render(self):
        """
        Renders the ascii characters from the screen to the output, specified in the send_to_output function
        """
        screen_render = self.screen.render()
        await self.send_to_output(screen_render)

    @property
    def send_to_output(self) -> Callable[[str], Coroutine[Any, Any, None]]:
        return self._send_to_output

    @property
    def screen(self) -> Screen:
        return self._screen
