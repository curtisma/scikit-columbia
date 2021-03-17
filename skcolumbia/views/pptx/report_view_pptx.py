from typing import Union
from pathlib import Path
from ...report import ReportModel


class ReportViewPPTX:
    def __init__(self, report_model: ReportModel) -> None:
        self._model = report_model

    def save(self, file: Union[str, Path]) -> None:
        pass

    def _element_factory(self):
        self._model.create()
