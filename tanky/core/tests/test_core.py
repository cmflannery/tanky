#!/usr/bin/env python
import numpy as np
from core.parameters import DesignParameters


def test_DesignParameters():
    TestParams = DesignParameters
    DesignParameters.prompt_sf()
