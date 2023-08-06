# -*- coding: utf-8 -*-
#
# Copyright 2015-2017 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl
"""
.. currentmodule:: co2mpas

.. autosummary::
    :nosignatures:
    :toctree: _build/co2mpas/

    ~model
    ~io
    ~batch
    ~datasync
    ~plot
    ~plan
    ~utils
    ~report
"""

from ._version import (__version__, __updated__, __file_version__, __input_file_version__)

__copyright__ = "Copyright (C) 2015-2017 European Commission (JRC)"
__license__   = "EUPL 1.1+"
__title__     = "co2mpas"
__summary__   = "Vehicle simulator predicting NEDC CO2 emissions from WLTP " \
                "time-series."
__uri__       = "https://co2mpas.io"
version       = __version__
