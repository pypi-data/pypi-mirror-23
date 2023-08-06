#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .dslr import DSLR_CAMERAS_RGB_SPECTRAL_SENSITIVITIES
from colour.utilities import CaseInsensitiveMapping

CAMERAS_RGB_SPECTRAL_SENSITIVITIES = CaseInsensitiveMapping(
    DSLR_CAMERAS_RGB_SPECTRAL_SENSITIVITIES)

__all__ = ['CAMERAS_RGB_SPECTRAL_SENSITIVITIES']
