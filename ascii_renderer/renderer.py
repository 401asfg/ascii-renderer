from typing import Any, Callable, Coroutine
from ascii_renderer.renderable import Renderable


class Renderer:
    """
    Renders a renderable
    """

    _send_to_output: Callable[[str], Coroutine[Any, Any, None]]
    _renderable: Renderable

    def __init__(self, send_to_output: Callable[[str], Coroutine[Any, Any, None]], renderable: Renderable):
        """
        Initializes the class

        :param send_to_output: The function used to send the given renderable's rendering as a message when this class' render
        function is called
        :param renderable: The renderable to render to the output, specified in the given send_to_output function
        """
        self._send_to_output = send_to_output
        self._renderable = renderable

    async def render(self):
        """
        Renders the ascii characters from the renderable to the output, specified in the send_to_output function
        """
        rendering = self.renderable.render()
        await self.send_to_output(rendering)

    @property
    def send_to_output(self) -> Callable[[str], Coroutine[Any, Any, None]]:
        return self._send_to_output

    @property
    def renderable(self) -> Renderable:
        return self._renderable
