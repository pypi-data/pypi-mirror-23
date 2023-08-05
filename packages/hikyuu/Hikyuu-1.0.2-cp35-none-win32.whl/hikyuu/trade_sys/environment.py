#!/usr/bin/python
# -*- coding: utf8 -*-
# cp936

#===============================================================================
# 作者：fasiondog
# 历史：1）20130419, Added by fasiondog
#===============================================================================

from . import _trade_sys as csys
from hikyuu.util.unicode import (unicodeFunc, reprFunc)

EnvironmentBase = csys.EnvironmentBase
EnvironmentBase.__unicode__ = unicodeFunc
EnvironmentBase.__repr__ = reprFunc