# -*- coding: utf-8 -*-
u"""
Created on 2015-7-13

@author: cheng.li
"""

import sys
import os

thisFilePath = os.path.abspath(__file__)

sys.path.append(os.path.sep.join(thisFilePath.split(os.path.sep)[:-3]))

import unittest
import PyFin.tests.api as api
import PyFin.tests.Analysis as Analysis
import PyFin.tests.DateUtilities as DateUtilities
import PyFin.tests.Env as Env
import PyFin.tests.Math as Math
import PyFin.tests.POpt as POpt
import PyFin.tests.PricingEngines as PricingEngines
import PyFin.tests.Utilities as Utilities


def test():
    print('Python ' + sys.version)
    suite = unittest.TestSuite()

    tests = unittest.TestLoader().loadTestsFromTestCase(api.TestDateUtilities)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TestDataProviders)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TestSecurityValueHolders)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TestCrossSectionValueHolder)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TestSecurityValues)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TestTransformer)
    suite.addTest(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TechnicalAnalysis.TestStatelessTechnicalAnalysis)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TechnicalAnalysis.TestStatelessTechnicalAnalysis)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Analysis.TechnicalAnalysis.TestStatefulTechnicalAnalysis)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(DateUtilities.TestCalendar)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(DateUtilities.TestDate)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(DateUtilities.TestPeriod)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(DateUtilities.TestSchedule)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Env.TestSettings)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Distributions.TestDistribution)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(PricingEngines.TestBlackFormula)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(PricingEngines.TestSabrFormula)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(PricingEngines.TestSVIInterpolation)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Accumulators.TestAccumulatorImpl)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Accumulators.TestAccumulatorsArithmetic)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Accumulators.TestStatefulAccumulators)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Accumulators.TestStatelessAccumulators)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Timeseries.TestNormalizers)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Accumulators.TestPerformancers)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Math.Timeseries.TestTimeseries)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(POpt.TestOptimizer)
    suite.addTests(tests)
    tests = unittest.TestLoader().loadTestsFromTestCase(Utilities.TestAsserts)
    suite.addTests(tests)

    res = unittest.TextTestRunner(verbosity=3).run(suite)
    if len(res.errors) >= 1 or len(res.failures) >= 1:
        sys.exit(-1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    test()
