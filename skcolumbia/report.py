class ReportModel:
    """
    The top-level report
    """
    def __init__(self, name):
        self._children = []
        self._name = name

    def add_element(self, element):
        self._children.append(element)

    @property
    def name(self):
        return self._name
