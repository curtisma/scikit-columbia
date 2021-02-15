from .base_element import BaseElement


class Section(BaseElement):
    """
    A container for other elements of the report.
    """

    def __init__(self, name="", elements=None):
        if elements is not None:
            self._elements = elements
        else:
            self._elements = []
        self.name = name

    @property
    def elements(self):
        return self._elements

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val,str):
            self._name = val
        else:
            self.name = str(val)
