#!/usr/bin/python
# -*- coding: utf8 -*-
# gb18030

#===============================================================================
# 作者：fasiondog
# 历史：1）20130311, Added by fasiondog
#===============================================================================

import unittest

from test_init import *
from hikyuu.trade_sys.condition import *

class ConditionPython(ConditionBase):
    def __init__(self):
        super(ConditionPython, self).__init__("ConditionPython")
        self.setParam("n", 10)
        self._m_flag = False
        
    def isValid(self, datetime):
        return self._m_flag
    
    def _reset(self):
        if self._m_flag:
            self._m_flag = False
        else:
            self._m_flag = True
            
    def _clone(self):
        p = ConditionPython()
        p._m_flag = self._m_flag
        return p

class ConditionTest(unittest.TestCase):
    def test_ConditionBase(self):
        p = ConditionPython()
        self.assertEqual(p.name, "ConditionPython")
        self.assertEqual(p.getParam("n"), 10)
        p.setParam("n",20)
        self.assertEqual(p.getParam("n"), 20)
        self.assertEqual(p.isValid(Datetime(200101010000)), False)
        p.reset()
        self.assertEqual(p.isValid(Datetime(200101010000)), True)
        
        p_clone = p.clone()
        self.assertEqual(p_clone.name, "ConditionPython")
        self.assertEqual(p_clone.getParam("n"), 20)
        self.assertEqual(p_clone.isValid(Datetime(200101010000)), True)

        p.setParam("n", 1)
        p_clone.setParam("n", 3)
        self.assertEqual(p.getParam("n"), 1)
        self.assertEqual(p_clone.getParam("n"), 3)
                 
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(ConditionTest)
