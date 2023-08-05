#!/usr/bin/python
# -*- coding: utf8 -*-
# cp936

#===============================================================================
# 作者：fasiondog
# 历史：1）20130419, Added by fasiondog
#===============================================================================

from . import _trade_sys as csys
from hikyuu.util.unicode import (unicodeFunc, reprFunc)

ConditionBase = csys.ConditionBase
ConditionBase.__unicode__ = unicodeFunc
ConditionBase.__repr__ = reprFunc

CN_OPLine = csys.CN_OPLine