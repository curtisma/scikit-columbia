===============
scikit-columbia
===============

A technical report generator for communicating conclusions and supporting data in a concise and pythonic manner.

Data Presentation Options
-------------------------

- Plots
  - Matplotlib 
- Tables
  - `Pandas <https://pandas.pydata.org/>`_

Output Formats
--------------

Supports presenting reports in multiple output formats:

* PPTX
* PDF
* XLSX
* Qt GUI

Origin of the Name
==================
The library is named in honor of the space shuttle columbia.  It was inspired by articles on how part of the cause of the tragedy was a poorly presented technical report.  

- `Power Point Does Rocket Science <https://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0001yB>`_
- `Death by PowerPoint: the slide that killed seven people <https://mcdreeamiemusings.com/blog/2019/4/13/gsux1h6bnt8lqjd7w2t2mtvfg81uhx>`
- `Why Edward Tufte is Wrong <https://eslide.com/why-edward-tufte-is-wrong/>`_

Installation
============
It can be installed as a package from either conda-forge or pip.  It can also be installed from source for development and extension.

Conda
-----

PIP
---

Source
------

Development
===========

Architecture
------------
A model-view-controller (MVC) architecture is used for the core classes.

Extension
---------
scikit-columbia is implemented as a namespace package to enable easy extension by dependents.

Related Projects
----------------
- `ReportLab <https://www.reportlab.com/>`_
  - `PollyReports <https://pythonhosted.org/PollyReports/tutorial.html>`_
- `POD <http://appyframe.work/pod.html>`_
- `PythonReports <http://pythonreports.sourceforge.net/index.shtml>`_
- `Datapane <https://datapane.com/>`_

Scikit
------
This `scikit <https://www.scipy.org/scikits.html>`_ supports the presentation of data from `scipy projects <https://www.scipy.org/index.html>`_.
