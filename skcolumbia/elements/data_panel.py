from .base_element import BaseElement


class DataPanel(BaseElement):
    """
    Presents a set of data
    """

    def __init__(self, title):
        self._title = ""

    @property
    def title(self):
        return self._title
