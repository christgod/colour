#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DSLR Cameras Spectral Sensitivities
===================================

Defines *DSLR* cameras *RGB* spectral sensitivities.

Each *DSLR* camera data is in the form of a *dict* of
:class:`colour.characterisation.cameras.RGB_SpectralSensitivities` classes as
follows::

    {'name': RGB_SpectralSensitivities,
    ...,
    'name': RGB_SpectralSensitivities}

The following *DSLR* cameras are available:

-   Nikon 5100 (NPL)
-   Sigma SDMerill (NPL)

See Also
--------
`Cameras Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/characterisation/cameras.ipynb>`_

References
----------
.. [1]  Darrodi, M. M., Finlayson, G., Goodman, T., & Mackiewicz, M. (2015).
        Reference data set for camera spectral sensitivity estimation.
        Journal of the Optical Society of America A, 32(3), 381.
        doi:10.1364/JOSAA.32.000381
"""

from __future__ import division, unicode_literals

from colour.characterisation import RGB_SpectralSensitivities
from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2017 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES_DATA',
           'DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES']

DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES_DATA = {
    'Nikon 5100 (NPL)': {
        'red': {
            380.0: 0.00156384299336578000,
            385.0: 0.00189691771384825000,
            390.0: 0.00000000000000000000,
            395.0: 0.00000000000000000000,
            400.0: 0.00000000000000000000,
            405.0: 0.00071776703300973298,
            410.0: 0.00292397466563330000,
            415.0: 0.01293626801713740000,
            420.0: 0.04959786481566520000,
            425.0: 0.07607250435970400200,
            430.0: 0.07658892708274399300,
            435.0: 0.06833381956036009600,
            440.0: 0.06131816189646559900,
            445.0: 0.05473314457789760200,
            450.0: 0.04886204743702320100,
            455.0: 0.04284591974257399800,
            460.0: 0.04022845332691499900,
            465.0: 0.04340795992263239700,
            470.0: 0.04762021431177430200,
            475.0: 0.05077188480559390000,
            480.0: 0.05280329597225499900,
            485.0: 0.05257122025495090300,
            490.0: 0.04789463902845950100,
            495.0: 0.04823994170483859900,
            500.0: 0.05022924089718029700,
            505.0: 0.05507649735001429700,
            510.0: 0.06370211901178619900,
            515.0: 0.08038951305895999900,
            520.0: 0.10038750399831201000,
            525.0: 0.11861314902313400000,
            530.0: 0.12360875120338000000,
            535.0: 0.10306249932787701000,
            540.0: 0.07634108360672720000,
            545.0: 0.05278086364640900000,
            550.0: 0.04118873831058649700,
            555.0: 0.03904385351931050100,
            560.0: 0.04254429440089119900,
            565.0: 0.06021313241068020100,
            570.0: 0.11179621705066800000,
            575.0: 0.26967059703276203000,
            580.0: 0.56450337990639099000,
            585.0: 0.85360126947261405000,
            590.0: 0.98103242181506201000,
            595.0: 1.00000000000000000000,
            600.0: 0.96307105371259005000,
            605.0: 0.90552061898043101000,
            610.0: 0.83427841652645296000,
            615.0: 0.76798733762510296000,
            620.0: 0.70366798041157996000,
            625.0: 0.63916484476123703000,
            630.0: 0.57081292173776299000,
            635.0: 0.49581796193158800000,
            640.0: 0.43833913452368101000,
            645.0: 0.38896992260406899000,
            650.0: 0.34295621205484700000,
            655.0: 0.29278541836293998000,
            660.0: 0.23770718073119301000,
            665.0: 0.16491386803178501000,
            670.0: 0.09128771706377150600,
            675.0: 0.04205615047283590300,
            680.0: 0.02058267877678380100,
            685.0: 0.01028680596369610000,
            690.0: 0.00540759846247261970,
            695.0: 0.00272409261591003000,
            700.0: 0.00127834798711079000,
            705.0: 0.00078123118374132301,
            710.0: 0.00047981421940270001,
            715.0: 0.00049133356428571098,
            720.0: 0.00017414897796340199,
            725.0: 0.00012017462571764001,
            730.0: 0.00000000000000000000,
            735.0: 6.1199999999999997e-05,
            740.0: 0.00000000000000000000,
            745.0: 0.00000000000000000000,
            750.0: 0.00031099754946016501,
            755.0: 0.00000000000000000000,
            760.0: 0.00000000000000000000,
            765.0: 0.00000000000000000000,
            770.0: 8.5599999999999994e-05,
            775.0: 0.00013831372865247499,
            780.0: 3.6199999999999999e-05},
        'green': {
            380.0: 0.00011500000000000000,
            385.0: 0.00152114360178015000,
            390.0: 0.00057430499183558695,
            395.0: 0.00000000000000000000,
            400.0: 0.00000000000000000000,
            405.0: 0.00119722386224553000,
            410.0: 0.00133571498448177000,
            415.0: 0.01319431696052810100,
            420.0: 0.06497102451249539600,
            425.0: 0.11510308718828900000,
            430.0: 0.13706582547087201000,
            435.0: 0.15242852584030600000,
            440.0: 0.16864005450745301000,
            445.0: 0.18329934605049600000,
            450.0: 0.19603263456229600000,
            455.0: 0.21733653278361301000,
            460.0: 0.25424357380995000000,
            465.0: 0.30864811930649899000,
            470.0: 0.37346871184252001000,
            475.0: 0.42915806139893697000,
            480.0: 0.45965432432137399000,
            485.0: 0.47106435446394301000,
            490.0: 0.48885616444524799000,
            495.0: 0.53715178104087602000,
            500.0: 0.61649118695883898000,
            505.0: 0.70700638759968903000,
            510.0: 0.80096424601366301000,
            515.0: 0.88137256686267296000,
            520.0: 0.93887792119838498000,
            525.0: 0.98446559576523596000,
            530.0: 1.00000000000000000000,
            535.0: 0.99084026557129701000,
            540.0: 0.96154626462922099000,
            545.0: 0.92814388346877297000,
            550.0: 0.88910231592076505000,
            555.0: 0.83494222924161199000,
            560.0: 0.77631807500187500000,
            565.0: 0.70731424532056497000,
            570.0: 0.63579620249170998000,
            575.0: 0.56551528450380395000,
            580.0: 0.49275517253522499000,
            585.0: 0.42475654159075799000,
            590.0: 0.35178931226078303000,
            595.0: 0.27817849879541801000,
            600.0: 0.21167353249961901000,
            605.0: 0.15671644549433000000,
            610.0: 0.11803962073050200000,
            615.0: 0.08885249534231440300,
            620.0: 0.07010184404853669900,
            625.0: 0.05690899470893220200,
            630.0: 0.04729879101895839700,
            635.0: 0.04119589002556579800,
            640.0: 0.03525207084991220000,
            645.0: 0.03069313144532450100,
            650.0: 0.02680396295683950100,
            655.0: 0.02352430119871520100,
            660.0: 0.02034633252474659900,
            665.0: 0.01545848325340879900,
            670.0: 0.00944075104617158980,
            675.0: 0.00508102204063505970,
            680.0: 0.00291019166901752010,
            685.0: 0.00162657557793382010,
            690.0: 0.00092251569139627796,
            695.0: 0.00049743349969026901,
            700.0: 0.00041215940263165701,
            705.0: 0.00031692634104666300,
            710.0: 0.00025621496960251102,
            715.0: 0.00000000000000000000,
            720.0: 0.00024353518865341200,
            725.0: 6.0200000000000000e-05,
            730.0: 0.00000000000000000000,
            735.0: 0.00000000000000000000,
            740.0: 0.00000000000000000000,
            745.0: 1.7099999999999999e-05,
            750.0: 5.2099999999999999e-05,
            755.0: 8.8499999999999996e-05,
            760.0: 0.00000000000000000000,
            765.0: 0.00000000000000000000,
            770.0: 0.00013799999999999999,
            775.0: 0.0001786501727059410,
            780.0: 4.2500000000000003e-05},
        'blue': {
            380.0: 0.00180956039402335990,
            385.0: 0.00048982814544150399,
            390.0: 0.00087943069176996504,
            395.0: 0.00000000000000000000,
            400.0: 0.00153246068848051000,
            405.0: 0.00569805602282062030,
            410.0: 0.01660828769874150200,
            415.0: 0.07879120559214590500,
            420.0: 0.36171350364994898000,
            425.0: 0.65970462106512295000,
            430.0: 0.75534360010359503000,
            435.0: 0.81045312707380701000,
            440.0: 0.87494523362472998000,
            445.0: 0.92671273991178704000,
            450.0: 0.96314088025989897000,
            455.0: 0.98065048133510302000,
            460.0: 1.00000000000000000000,
            465.0: 0.99640467488711104000,
            470.0: 0.98896988650084305000,
            475.0: 0.95660139953157997000,
            480.0: 0.90495886986980800000,
            485.0: 0.83940927710351598000,
            490.0: 0.75146259578963404000,
            495.0: 0.66010202032260801000,
            500.0: 0.56706879193613802000,
            505.0: 0.47935094782603899000,
            510.0: 0.39406273870351299000,
            515.0: 0.31427061879449603000,
            520.0: 0.24981663439426000000,
            525.0: 0.20182351924718100000,
            530.0: 0.16163395085177601000,
            535.0: 0.13516143147333401000,
            540.0: 0.10998875716043301000,
            545.0: 0.08639435407789379500,
            550.0: 0.06525313059219839400,
            555.0: 0.04785595345227559900,
            560.0: 0.03413932303860940000,
            565.0: 0.02401990976851929900,
            570.0: 0.01976793598476750100,
            575.0: 0.01634844781073010000,
            580.0: 0.01381733937020259900,
            585.0: 0.01195294647966710000,
            590.0: 0.01000909395820090100,
            595.0: 0.00758776308929657970,
            600.0: 0.00645584463521649970,
            605.0: 0.00522978285684488030,
            610.0: 0.00365998459503786990,
            615.0: 0.00395538505488667040,
            620.0: 0.00396835221654468030,
            625.0: 0.00349138004486036990,
            630.0: 0.00404302103181797010,
            635.0: 0.00418929985295813000,
            640.0: 0.00554676856500057980,
            645.0: 0.00546423323547744030,
            650.0: 0.00597382847392098970,
            655.0: 0.00630906774763779000,
            660.0: 0.00610412697742267980,
            665.0: 0.00483655792375416000,
            670.0: 0.00302664794586984980,
            675.0: 0.00172169700987674990,
            680.0: 0.00078065128657817595,
            685.0: 0.00056963070848184102,
            690.0: 0.00027523296133938200,
            695.0: 0.00029672137857068598,
            700.0: 0.00024951192304202899,
            705.0: 8.5000000000000006e-05,
            710.0: 0.00041916895092770603,
            715.0: 0.00015331743444139899,
            720.0: 1.8300000000000001e-05,
            725.0: 0.00000000000000000000,
            730.0: 0.00033869381945204901,
            735.0: 0.00000000000000000000,
            740.0: 0.00000000000000000000,
            745.0: 0.00016527828734010200,
            750.0: 0.00017755262214537101,
            755.0: 0.00000000000000000000,
            760.0: 2.4300000000000001e-05,
            765.0: 6.1799999999999998e-05,
            770.0: 0.00026260703183506501,
            775.0: 0.00028050537004191899,
            780.0: 0.00000000000000000000}},
    'Sigma SDMerill (NPL)': {
        'red': {
            400.0: 0.00562107440608700020,
            410.0: 0.00650335624511722000,
            420.0: 0.07407911289140040000,
            430.0: 0.04302295946292879900,
            440.0: 0.03450952562247010200,
            450.0: 0.01889156723434350100,
            460.0: 0.00731107699680200000,
            470.0: 0.04549915123096019700,
            480.0: 0.05676752921111680200,
            490.0: 0.13419592065917799000,
            500.0: 0.16475268997837600000,
            510.0: 0.21712641978639199000,
            520.0: 0.30648343835824399000,
            530.0: 0.34984579614888500000,
            540.0: 0.44374258133259298000,
            550.0: 0.44488860528126301000,
            560.0: 0.47897575674702603000,
            570.0: 0.50950291481073895000,
            580.0: 0.59262909378530504000,
            590.0: 0.67383327560697603000,
            600.0: 0.71403771488106504000,
            610.0: 0.86000761311495100000,
            620.0: 0.89810302849565204000,
            630.0: 1.00000000000000000000,
            640.0: 0.99494213311245205000,
            650.0: 0.92085127736137995000,
            660.0: 0.18143311631425299000,
            670.0: 0.00630978795372749960,
            680.0: 0.00528874383171553000},
        'green': {
            400.0: 0.00632809751263116970,
            410.0: 0.00976180459591275040,
            420.0: 0.02527177008261050100,
            430.0: 0.08375118585311219800,
            440.0: 0.14370381974360999000,
            450.0: 0.18361168930882199000,
            460.0: 0.40909478009952999000,
            470.0: 0.51595564086176404000,
            480.0: 0.60120664662705503000,
            490.0: 0.67031679980136305000,
            500.0: 0.75258747153475802000,
            510.0: 0.84381384368944201000,
            520.0: 0.90151724558812696000,
            530.0: 0.91975030668767699000,
            540.0: 0.96799429052157804000,
            550.0: 0.95725231064041105000,
            560.0: 0.95204791860047400000,
            570.0: 0.97628014458399803000,
            580.0: 0.97258624388955806000,
            590.0: 1.00000000000000000000,
            600.0: 0.96948452757777404000,
            610.0: 0.95441319124850699000,
            620.0: 0.93335435890921303000,
            630.0: 0.92571406833636205000,
            640.0: 0.88486439541503403000,
            650.0: 0.76165184741615699000,
            660.0: 0.14052437057150499000,
            670.0: 0.00414367215817645990,
            680.0: 0.00183198958165669010},
        'blue': {
            400.0: 0.16215942413307899000,
            410.0: 0.28549837804628603000,
            420.0: 0.39690431060902098000,
            430.0: 0.50831024317175599000,
            440.0: 0.62211847246948804000,
            450.0: 0.73742136245769496000,
            460.0: 0.94538036670138004000,
            470.0: 0.96441494770280400000,
            480.0: 1.00000000000000000000,
            490.0: 0.98598021188452500000,
            500.0: 0.98340266357529005000,
            510.0: 0.96969219567072595000,
            520.0: 0.94280817402079797000,
            530.0: 0.89664279918070899000,
            540.0: 0.88444590220041897000,
            550.0: 0.86791899071597101000,
            560.0: 0.83375679584908402000,
            570.0: 0.83204140240572999000,
            580.0: 0.80054956384778198000,
            590.0: 0.78289512474646505000,
            600.0: 0.73946953007191796000,
            610.0: 0.66718640174985699000,
            620.0: 0.62043627806816704000,
            630.0: 0.61116087876956704000,
            640.0: 0.55173556195710605000,
            650.0: 0.46538831744516401000,
            660.0: 0.07961907836720690000,
            670.0: 0.00059244446107236802,
            680.0: 0.00468563680483140980}}}

DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES = CaseInsensitiveMapping({
    'Nikon 5100 (NPL)': RGB_SpectralSensitivities(
        'Nikon 5100 (NPL)',
        DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES_DATA['Nikon 5100 (NPL)']),
    'Sigma SDMerill (NPL)': RGB_SpectralSensitivities(
        'Sigma SDMerill (NPL)',
        DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES_DATA['Sigma SDMerill (NPL)'])})
"""
*DSLR* cameras *RGB* spectral sensitivities.

DSL_CAMERAS_RGB_SPECTRAL_SENSITIVITIES : CaseInsensitiveMapping
    **{Nikon 5100 (NPL), Sigma SDMerill (NPL)}**
"""