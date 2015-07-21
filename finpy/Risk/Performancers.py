# -*- coding: utf-8 -*-
u"""
Created on 2015-7-17

@author: cheng.li
"""

from finpy.Risk.Accumulators import MovingMaxer
from finpy.Risk.Accumulators import MovingAverager
from finpy.Risk.Accumulators import MovingVariancer
from finpy.Risk.Accumulators import MovingCorrelation
import math


class MovingSharp(object):

    def __init__(self, window):
        self._mean = MovingAverager(window)
        self._var = MovingVariancer(window, False)
        self._window = window

    def push(self, value, benchmark=0.0):
        '''
        @value: annualized return value
        @benchmark: annualized benchmark treasury bond yield
        '''
        self._mean.push(value - benchmark)
        self._var.push(value)

    def result(self):
        if len(self._mean._con) >= 2:
            return self._mean.result() / math.sqrt(self._var.result())


class MovingAlphaBeta(object):

    def __init__(self, window):
        self._pReturnMean = MovingAverager(window)
        self._mReturnMean = MovingAverager(window)
        self._pReturnVar = MovingVariancer(window)
        self._mReturnVar = MovingVariancer(window)
        self._correlationHolder = MovingCorrelation(window)

    def push(self, pReturn, mReturn, rf=0.0):
        self._pReturnMean.push(pReturn - rf)
        self._mReturnMean.push(mReturn - rf)
        self._pReturnVar.push(pReturn - rf)
        self._mReturnVar.push(mReturn - rf)
        self._correlationHolder.push((pReturn - rf, mReturn - rf))

    def result(self):
        if len(self._pReturnMean._con) >= 2:
            corr = self._correlationHolder.result()
            pStd = math.sqrt(self._pReturnVar.result())
            mStd = math.sqrt(self._mReturnVar.result())
            beta = corr * pStd / mStd
            alpha = self._pReturnMean.result() - beta * self._mReturnMean.result()
            return alpha, beta


class MovingDrawDown(object):

    def __init__(self, window):
        self._maxer = MovingMaxer(window+1)
        self._maxer.push(0.0)
        self._runningCum = 0.0
        self._highIndex = 0
        self._runningIndex = 0

    def push(self, value):
        '''
        :param value: expected to be exponential annualized return
        :return:
        '''
        self._runningIndex += 1
        self._runningCum += value
        self._maxer.push(self._runningCum)
        self._currentMax = self._maxer.result()
        if self._runningCum >= self._currentMax:
            self._highIndex = self._runningIndex

    def result(self):
        '''
        :return: (draw down, duration, high index)
        '''
        return self._runningCum - self._currentMax, self._runningIndex - self._highIndex, self._highIndex


if __name__ == "__main__":
    mv = MovingDrawDown(5)

    value = [-0.01, -0.05, -0.02, 0.03, 0.04, 0.03, -0.01, 0.005, -0.02, -0.04, 0.2]

    for v in value:
        mv.push(v)
        print(mv.result())









