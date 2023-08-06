#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from colour.utilities import CaseInsensitiveMapping, filter_kwargs

from .aces import (log_encoding_ACESproxy, log_decoding_ACESproxy,
                   log_encoding_ACEScc, log_decoding_ACEScc,
                   log_encoding_ACEScct, log_decoding_ACEScct)
from .alexa_log_c import (log_encoding_ALEXALogC, log_decoding_ALEXALogC)
from .arib_std_b67 import oetf_ARIBSTDB67, eotf_ARIBSTDB67
from .bt_709 import oetf_BT709, eotf_BT709
from .bt_1886 import oetf_BT1886, eotf_BT1886
from .bt_2020 import oetf_BT2020, eotf_BT2020
from .canon_log import (log_encoding_CanonLog, log_decoding_CanonLog,
                        log_encoding_CanonLog2, log_decoding_CanonLog2,
                        log_encoding_CanonLog3, log_decoding_CanonLog3)
from .cineon import log_encoding_Cineon, log_decoding_Cineon
from .dci_p3 import oetf_DCIP3, eotf_DCIP3
from .dicom_gsdf import oetf_DICOMGSDF, eotf_DICOMGSDF
from .gamma import function_gamma
from .gopro import log_encoding_Protune, log_decoding_Protune
from .linear import function_linear
from .panalog import log_encoding_Panalog, log_decoding_Panalog
from .panasonic_vlog import log_encoding_VLog, log_decoding_VLog
from .pivoted_log import log_encoding_PivotedLog, log_decoding_PivotedLog
from .red_log import (log_encoding_REDLog, log_decoding_REDLog,
                      log_encoding_REDLogFilm, log_decoding_REDLogFilm,
                      log_encoding_Log3G10, log_decoding_Log3G10,
                      log_encoding_Log3G12, log_decoding_Log3G12)
from .rimm_romm_rgb import (oetf_ROMMRGB, eotf_ROMMRGB, oetf_ProPhotoRGB,
                            eotf_ProPhotoRGB, oetf_RIMMRGB, eotf_RIMMRGB,
                            log_encoding_ERIMMRGB, log_decoding_ERIMMRGB)
from .srgb import oetf_sRGB, eotf_sRGB
from .sony_slog import (log_encoding_SLog, log_decoding_SLog,
                        log_encoding_SLog2, log_decoding_SLog2,
                        log_encoding_SLog3, log_decoding_SLog3)
from .st_2084 import oetf_ST2084, eotf_ST2084
from .viper_log import log_encoding_ViperLog, log_decoding_ViperLog

__all__ = [
    'log_encoding_ACESproxy', 'log_decoding_ACESproxy', 'log_encoding_ACEScc',
    'log_decoding_ACEScc', 'log_encoding_ACEScct', 'log_decoding_ACEScct'
]
__all__ += ['log_encoding_ALEXALogC', 'log_decoding_ALEXALogC']
__all__ += ['oetf_ARIBSTDB67', 'eotf_ARIBSTDB67']
__all__ += ['oetf_BT709', 'eotf_BT709']
__all__ += ['oetf_BT1886', 'eotf_BT1886']
__all__ += ['oetf_BT2020', 'eotf_BT2020']
__all__ += [
    'log_encoding_CanonLog', 'log_decoding_CanonLog', 'log_encoding_CanonLog2',
    'log_decoding_CanonLog2', 'log_encoding_CanonLog3',
    'log_decoding_CanonLog3'
]
__all__ += ['log_encoding_Cineon', 'log_decoding_Cineon']
__all__ += ['oetf_DCIP3', 'eotf_DCIP3']
__all__ += ['oetf_DICOMGSDF', 'eotf_DICOMGSDF']
__all__ += ['function_gamma']
__all__ += ['log_encoding_Protune', 'log_decoding_Protune']
__all__ += ['function_linear']
__all__ += ['log_encoding_Panalog', 'log_decoding_Panalog']
__all__ += ['log_encoding_VLog', 'log_decoding_VLog']
__all__ += ['log_encoding_PivotedLog', 'log_decoding_PivotedLog']
__all__ += [
    'log_encoding_REDLog', 'log_decoding_REDLog', 'log_encoding_REDLogFilm',
    'log_decoding_REDLogFilm', 'log_encoding_Log3G10', 'log_decoding_Log3G10',
    'log_encoding_Log3G12', 'log_decoding_Log3G12'
]
__all__ += [
    'oetf_ROMMRGB', 'eotf_ROMMRGB', 'oetf_ProPhotoRGB', 'eotf_ProPhotoRGB',
    'oetf_RIMMRGB', 'eotf_RIMMRGB', 'log_encoding_ERIMMRGB',
    'log_decoding_ERIMMRGB'
]
__all__ += [
    'log_encoding_SLog', 'log_decoding_SLog', 'log_encoding_SLog2',
    'log_decoding_SLog2', 'log_encoding_SLog3', 'log_decoding_SLog3'
]
__all__ += ['oetf_sRGB', 'eotf_sRGB']
__all__ += ['oetf_ST2084', 'eotf_ST2084']
__all__ += ['log_decoding_ViperLog', 'log_decoding_ViperLog']

LOG_ENCODING_CURVES = CaseInsensitiveMapping({
    'ACEScc': log_encoding_ACEScc,
    'ACEScct': log_encoding_ACEScct,
    'ACESproxy': log_encoding_ACESproxy,
    'ALEXA Log C': log_encoding_ALEXALogC,
    'Canon Log 2': log_encoding_CanonLog2,
    'Canon Log 3': log_encoding_CanonLog3,
    'Canon Log': log_encoding_CanonLog,
    'Cineon': log_encoding_Cineon,
    'ERIMM RGB': log_encoding_ERIMMRGB,
    'Log3G10': log_encoding_Log3G10,
    'Log3G12': log_encoding_Log3G12,
    'Panalog': log_encoding_Panalog,
    'PLog': log_encoding_PivotedLog,
    'Protune': log_encoding_Protune,
    'REDLog': log_encoding_REDLog,
    'REDLogFilm': log_encoding_REDLogFilm,
    'S-Log': log_encoding_SLog,
    'S-Log2': log_encoding_SLog2,
    'S-Log3': log_encoding_SLog3,
    'V-Log': log_encoding_VLog,
    'ViperLog': log_encoding_ViperLog
})
"""
Supported *log* encoding curves.

LOG_ENCODING_CURVES : CaseInsensitiveMapping
    **{'ACEScc', 'ACEScct', 'ACESproxy', 'ALEXA Log C', 'Canon Log 2',
    'Canon Log 3', 'Canon Log', 'Cineon', 'ERIMM RGB', 'Log3G10', 'Log3G12',
    'Panalog', 'PLog', 'Protune', 'REDLog', 'REDLogFilm', 'S-Log', 'S-Log2',
    'S-Log3', 'V-Log', 'ViperLog'}**
"""


def log_encoding_curve(value, curve='Cineon', **kwargs):
    """
    Encodes linear-light values to :math:`R'G'B'` video component signal
    value using given *log* curve.

    Parameters
    ----------
    value : numeric or array_like
        Value.
    curve : unicode, optional
        **{'ACEScc', 'ACEScct', 'ACESproxy', 'ALEXA Log C', 'Canon Log 2',
        'Canon Log 3', 'Canon Log', 'Cineon', 'ERIMM RGB', 'Log3G10',
        'Log3G12', 'Panalog', 'PLog', 'Protune', 'REDLog', 'REDLogFilm',
        'S-Log', 'S-Log2', 'S-Log3', 'V-Log', 'ViperLog'}**, Computation curve.

    Other Parameters
    ----------------
    EI : int,  optional
        {:func:`log_encoding_ALEXALogC`},
        Ei.
    E_clip : numeric, optional
        {:func:`log_encoding_ERIMMRGB`},
        Maximum exposure limit.
    E_min : numeric, optional
        {:func:`log_encoding_ERIMMRGB`},
        Minimum exposure limit.
    I_max : numeric, optional
        {:func:`log_encoding_ERIMMRGB`},
        Maximum code value: 255, 4095 and 650535 for respectively 8-bit,
        12-bit and 16-bit per channel.
    bit_depth : unicode, optional
        {:func:`log_encoding_ACESproxy`},
        **{'10 Bit', '12 Bit'}**,
        *ACESproxy* bit depth.
    black_offset : numeric or array_like
        {:func:`log_encoding_Cineon`, :func:`log_encoding_Panalog`,
        :func:`log_encoding_REDLog`, :func:`log_encoding_REDLogFilm`},
        Black offset.
    density_per_code_value : numeric or array_like
        {:func:`log_encoding_PivotedLog`},
        Density per code value.
    firmware : unicode, optional
        {:func:`log_encoding_ALEXALogC`},
        **{'SUP 3.x', 'SUP 2.x'}**,
        Alexa firmware version.
    linear_reference : numeric or array_like
        {:func:`log_encoding_PivotedLog`},
        Linear reference.
    log_reference : numeric or array_like
        {:func:`log_encoding_PivotedLog`},
        Log reference.
    negative_gamma : numeric or array_like
        {:func:`log_encoding_PivotedLog`},
        Negative gamma.
    method : unicode, optional
        {:func:`log_encoding_ALEXALogC`},
        **{'Linear Scene Exposure Factor', 'Normalised Sensor Signal'}**,
        Conversion method.

    Returns
    -------
    numeric or ndarray
        *Log* value.

    Examples
    --------
    >>> log_encoding_curve(0.18)  # doctest: +ELLIPSIS
    0.4573196...
    >>> log_encoding_curve(0.18, curve='ACEScc')  # doctest: +ELLIPSIS
    0.4135884...
    >>> log_encoding_curve(  # doctest: +ELLIPSIS
    ...     0.18, curve='PLog', log_reference=400)
    0.3910068...
    >>> log_encoding_curve(0.18, curve='S-Log')  # doctest: +ELLIPSIS
    0.3599878...
    """

    function = LOG_ENCODING_CURVES[curve]

    filter_kwargs(function, **kwargs)

    return function(value, **kwargs)


LOG_DECODING_CURVES = CaseInsensitiveMapping({
    'ACEScc': log_decoding_ACEScc,
    'ACEScct': log_decoding_ACEScct,
    'ACESproxy': log_decoding_ACESproxy,
    'ALEXA Log C': log_decoding_ALEXALogC,
    'Canon Log 2': log_decoding_CanonLog2,
    'Canon Log 3': log_decoding_CanonLog3,
    'Canon Log': log_decoding_CanonLog,
    'Cineon': log_decoding_Cineon,
    'ERIMM RGB': log_decoding_ERIMMRGB,
    'Log3G10': log_decoding_Log3G10,
    'Log3G12': log_decoding_Log3G12,
    'Panalog': log_decoding_Panalog,
    'PLog': log_decoding_PivotedLog,
    'Protune': log_decoding_Protune,
    'REDLog': log_decoding_REDLog,
    'REDLogFilm': log_decoding_REDLogFilm,
    'S-Log': log_decoding_SLog,
    'S-Log2': log_decoding_SLog2,
    'S-Log3': log_decoding_SLog3,
    'V-Log': log_decoding_VLog,
    'ViperLog': log_decoding_ViperLog
})
"""
Supported *log* decoding curves.

LOG_DECODING_CURVES : CaseInsensitiveMapping
    **{'ACEScc', 'ACEScct', 'ACESproxy', 'ALEXA Log C', 'Canon Log 2',
    'Canon Log 3', 'Canon Log', 'Cineon', 'ERIMM RGB', 'Log3G10', 'Log3G12',
    'Panalog', 'PLog', 'Protune', 'REDLog', 'REDLogFilm', 'S-Log', 'S-Log2',
    'S-Log3', 'V-Log', 'ViperLog'}**
"""


def log_decoding_curve(value, curve='Cineon', **kwargs):
    """
    Decodes :math:`R'G'B'` video component signal value to linear-light values
    using given *log* curve.

    Parameters
    ----------
    value : numeric or array_like
        Value.
    curve : unicode, optional
        **{'ACEScc', 'ACEScct', 'ACESproxy', 'ALEXA Log C', 'Canon Log 2',
        'Canon Log 3', 'Canon Log', 'Cineon', 'ERIMM RGB', 'Log3G10',
        'Log3G12', 'Panalog', 'PLog', 'Protune', 'REDLog', 'REDLogFilm',
        'S-Log', 'S-Log2', 'S-Log3', 'V-Log', 'ViperLog'}**, Computation curve.

    Other Parameters
    ----------------
    EI : int,  optional
        {:func:`log_decoding_ALEXALogC`},
        Ei.
    E_clip : numeric, optional
        {:func:`log_decoding_ERIMMRGB`},
        Maximum exposure limit.
    E_min : numeric, optional
        {:func:`log_decoding_ERIMMRGB`},
        Minimum exposure limit.
    I_max : numeric, optional
        {:func:`log_decoding_ERIMMRGB`},
        Maximum code value: 255, 4095 and 650535 for respectively 8-bit,
        12-bit and 16-bit per channel.
    bit_depth : unicode, optional
        {:func:`log_decoding_ACESproxy`},
        **{'10 Bit', '12 Bit'}**,
        *ACESproxy* bit depth.
    black_offset : numeric or array_like
        {:func:`log_decoding_Cineon`, :func:`log_decoding_Panalog`,
        :func:`log_decoding_REDLog`, :func:`log_decoding_REDLogFilm`},
        Black offset.
    density_per_code_value : numeric or array_like
        {:func:`log_decoding_PivotedLog`},
        Density per code value.
    firmware : unicode, optional
        {:func:`log_decoding_ALEXALogC`},
        **{'SUP 3.x', 'SUP 2.x'}**,
        Alexa firmware version.
    linear_reference : numeric or array_like
        {:func:`log_decoding_PivotedLog`},
        Linear reference.
    log_reference : numeric or array_like
        {:func:`log_decoding_PivotedLog`},
        Log reference.
    negative_gamma : numeric or array_like
        {:func:`log_decoding_PivotedLog`},
        Negative gamma.
    method : unicode, optional
        {:func:`log_decoding_ALEXALogC`},
        **{'Linear Scene Exposure Factor', 'Normalised Sensor Signal'}**,
        Conversion method.

    Returns
    -------
    numeric or ndarray
        *Log* value.

    Examples
    --------
    >>> log_decoding_curve(0.457319613085418)  # doctest: +ELLIPSIS
    0.1...
    >>> log_decoding_curve(  # doctest: +ELLIPSIS
    ...     0.413588402492442, curve='ACEScc')
    0.1...
    >>> log_decoding_curve(  # doctest: +ELLIPSIS
    ...     0.391006842619746, curve='PLog', log_reference=400)
    0.1...
    >>> log_decoding_curve(  # doctest: +ELLIPSIS
    ...     0.359987846422154, curve='S-Log')
    0.1...
    """

    function = LOG_DECODING_CURVES[curve]

    filter_kwargs(function, **kwargs)

    return function(value, **kwargs)


__all__ += ['LOG_ENCODING_CURVES', 'LOG_DECODING_CURVES']
__all__ += ['log_encoding_curve', 'log_decoding_curve']

OETFS = CaseInsensitiveMapping({
    'ARIB STD-B67': oetf_ARIBSTDB67,
    'BT.1886': oetf_BT1886,
    'BT.2020': oetf_BT2020,
    'BT.709': oetf_BT709,
    'DCI-P3': oetf_DCIP3,
    'DICOM GSDF': oetf_DICOMGSDF,
    'ProPhoto RGB': oetf_ProPhotoRGB,
    'RIMM RGB': oetf_RIMMRGB,
    'ROMM RGB': oetf_ROMMRGB,
    'sRGB': oetf_sRGB,
    'ST 2084': oetf_ST2084
})
"""
Supported opto-electrical transfer functions (OETF / OECF).

OETFS : CaseInsensitiveMapping
    **{'ARIB STD-B67', 'sRGB', 'BT.1886', 'BT.2020', 'BT.709', 'DCI-P3',
    'DICOM GSDF', 'ROMM RGB', 'ProPhoto RGB', 'RIMM RGB', 'ST 2084'}**
"""


def oetf(value, function='sRGB', **kwargs):
    """
    Encodes estimated tristimulus values in a scene to :math:`R'G'B'` video
    component signal value using given opto-electronic transfer function
    (OETF / OECF).

    Parameters
    ----------
    value : numeric or array_like
        Value.
    function : unicode, optional
        **{'ARIB STD-B67', 'sRGB', 'BT.1886', 'BT.2020', 'BT.709', 'DCI-P3',
        'DICOM GSDF', 'ROMM RGB', 'ProPhoto RGB', 'RIMM RGB', 'ST 2084'}**,
        Computation function.

    Other Parameters
    ----------------
    E_clip : numeric, optional
        {:func:`oetf_RIMMRGB`},
        Maximum exposure level.
    I_max : numeric, optional
        {:func:`oetf_ROMMRGB`, :func:`oetf_RIMMRGB`},
        Maximum code value: 255, 4095 and 650535 for respectively 8-bit,
        12-bit and 16-bit per channel.
    L_B : numeric, optional
        {:func:`oetf_BT1886`},
        Screen luminance for black.
    L_W : numeric, optional
        {:func:`oetf_BT1886`},
        Screen luminance for white.
    L_p : numeric, optional
        {:func:`oetf_ST2084`},
        Display peak luminance :math:`cd/m^2`.
    is_12_bits_system : bool
        {:func:`oetf_BT2020`},
        *BT.709* *alpha* and *beta* constants are used if system is not 12-bit.
    r : numeric, optional
        {:func:`oetf_ARIBSTDB67`},
        Video level corresponding to reference white level.

    Returns
    -------
    numeric or ndarray
        :math:`R'G'B'` video component signal value.

    Examples
    --------
    >>> oetf(0.18)  # doctest: +ELLIPSIS
    0.4613561...
    >>> oetf(0.18, function='BT.2020')  # doctest: +ELLIPSIS
    0.4090077...
    >>> oetf(  # doctest: +ELLIPSIS
    ...     0.18, function='ST 2084', L_p=1000)
    0.1820115...
    """

    function = OETFS[function]

    filter_kwargs(function, **kwargs)

    return function(value, **kwargs)


EOTFS = CaseInsensitiveMapping({
    'ARIB STD-B67': eotf_ARIBSTDB67,
    'BT.1886': eotf_BT1886,
    'BT.2020': eotf_BT2020,
    'BT.709': eotf_BT709,
    'DCI-P3': eotf_DCIP3,
    'DICOM GSDF': eotf_DICOMGSDF,
    'ProPhoto RGB': eotf_ProPhotoRGB,
    'RIMM RGB': eotf_RIMMRGB,
    'ROMM RGB': eotf_ROMMRGB,
    'sRGB': eotf_sRGB,
    'ST 2084': eotf_ST2084
})
"""
Supported electro-optical transfer functions (EOTF / EOCF).

EOTFS : CaseInsensitiveMapping
    **{'ARIB STD-B67', 'sRGB', 'BT.1886', 'BT.2020', 'BT.709', 'DCI-P3',
    'DICOM GSDF', 'ROMM RGB', 'ProPhoto RGB', 'RIMM RGB', 'ST 2084'}**
"""


def eotf(value, function='sRGB', **kwargs):
    """
    Decodes :math:`R'G'B'` video component signal value to tristimulus values
    at the display using given electro-optical transfer function (EOTF / EOCF).

    Parameters
    ----------
    value : numeric or array_like
        Value.
    function : unicode, optional
        **{'ARIB STD-B67', 'sRGB', 'BT.1886', 'BT.2020', 'BT.709', 'DCI-P3',
        'DICOM GSDF', 'ROMM RGB', 'ProPhoto RGB', 'RIMM RGB', 'ST 2084'}**,
        Computation function.

    Other Parameters
    ----------------
    E_clip : numeric, optional
        {:func:`eotf_RIMMRGB`},
        Maximum exposure level.
    I_max : numeric, optional
        {:func:`eotf_ROMMRGB`, :func:`eotf_RIMMRGB`},
        Maximum code value: 255, 4095 and 650535 for respectively 8-bit,
        12-bit and 16-bit per channel.
    L_B : numeric, optional
        {:func:`eotf_BT1886`},
        Screen luminance for black.
    L_W : numeric, optional
        {:func:`eotf_BT1886`},
        Screen luminance for white.
    L_p : numeric, optional
        {:func:`eotf_ST2084`},
        Display peak luminance :math:`cd/m^2`.
    is_12_bits_system : bool
        {:func:`eotf_BT2020`},
        *BT.709* *alpha* and *beta* constants are used if system is not 12-bit.
    r : numeric, optional
        {:func:`eotf_ARIBSTDB67`},
        Video level corresponding to reference white level.

    Returns
    -------
    numeric or ndarray
        Tristimulus values at the display.

    Examples
    --------
    >>> eotf(0.461356129500442)  # doctest: +ELLIPSIS
    0.1...
    >>> eotf(0.409007728864150,
    ...     function='BT.2020')  # doctest: +ELLIPSIS
    0.1...
    >>> eotf(  # doctest: +ELLIPSIS
    ...     0.182011532850008, function='ST 2084', L_p=1000)
    0.1...
    """

    function = EOTFS[function]

    filter_kwargs(function, **kwargs)

    return function(value, **kwargs)


__all__ += ['OETFS', 'EOTFS']
__all__ += ['oetf', 'eotf']
