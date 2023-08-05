#
# greedy.py
#
# Copyright (c) 2016-2017 Junpei Kawamoto
#
# This file is part of rgmining-fraudar.
#
# rgmining-fraudar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rgmining-fraudar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rgmining-fraudar. If not, see <http://www.gnu.org/licenses/>.
#
# This file was originally made by Bryan Hooi et al,
# and distributed under Apache License, Version 2.0.
#

# FRAUDAR: Bounding Graph Fraud in the Face of Camouflage
# Authors: Bryan Hooi, Hyun Ah Song, Alex Beutel, Neil Shah, Kijung Shin, Christos Faloutsos
#
# This software is licensed under Apache License, Version 2.0 (the  "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Version: 1.0
# Date: Oct 3, 2016
# Main Contact: Bryan Hooi (bhooi@andrew.cmu.edu)
"""contains functions that run the greedy detector for dense regions in a sparse matrix.
use aveDegree or sqrtWeightedAveDegree or logWeightedAveDegree on a sparse matrix,
which returns ((rowSet, colSet), score) for the most suspicious block.
"""

from __future__ import division
import numpy as np
import random
from scipy import sparse
from sklearn.utils import shuffle
from fraudar.export.MinTree import MinTree

from logging import getLogger
logger = getLogger(__name__)

np.set_printoptions(threshold='nan')
np.set_printoptions(linewidth=160)

# @profile


def listToSparseMatrix(edgesSource, edgesDest):
    """given a list of lists where each row is an edge, this returns the sparse matrix representation of the data.
    """
    m = max(edgesSource) + 1
    n = max(edgesDest) + 1
    M = sparse.coo_matrix(
        ([1] * len(edgesSource), (edgesSource, edgesDest)), shape=(m, n))
    M1 = M > 0
    return M1.astype('int')


def shuffleMatrix(M):
    """randomly shuffle the rows and columns.
    """
    M = shuffle(M)
    return shuffle(M.transpose()).transpose()


# @profile
def readData(filename):
    """reads matrix from file and returns sparse matrix.

    first 2 columns should be row and column indices of ones.
    """
    # dat = np.genfromtxt(filename, delimiter='\t', dtype=int)
    edgesSource = []
    edgesDest = []
    with open(filename) as f:
        for line in f:
            toks = line.split()
            edgesSource.append(int(toks[0]))
            edgesDest.append(int(toks[1]))
    return listToSparseMatrix(edgesSource, edgesDest)


def detectMultiple(M, detectFunc, numToDetect):
    Mcur = M.copy().tolil()
    res = []
    for i in range(numToDetect):
        ((rowSet, colSet), score) = detectFunc(Mcur)
        res.append(((rowSet, colSet), score))
        (rs, cs) = Mcur.nonzero()
        for i in range(len(rs)):
            if rs[i] in rowSet and cs[i] in colSet:
                Mcur[rs[i], cs[i]] = 0
    return res


def injectCliqueCamo(M, m0, n0, p, testIdx):
    _, n = M.shape
    M2 = M.copy().tolil()

    colSum = np.squeeze(M2.sum(axis=0).A)
    colSumPart = colSum[n0:n]
    colSumPartPro = np.int_(colSumPart)
    colIdx = np.arange(n0, n, 1)
    population = np.repeat(colIdx, colSumPartPro, axis=0)

    for i in range(m0):
        # inject clique
        for j in range(n0):
            if random.random() < p:
                M2[i, j] = 1
        # inject camo
        if testIdx == 1:
            thres = p * n0 / (n - n0)
            for j in range(n0, n):
                if random.random() < thres:
                    M2[i, j] = 1
        if testIdx == 2:
            thres = 2 * p * n0 / (n - n0)
            for j in range(n0, n):
                if random.random() < thres:
                    M2[i, j] = 1
        # biased camo
        if testIdx == 3:
            colRplmt = random.sample(population, int(n0 * p))
            M2[i, colRplmt] = 1

    return M2.tocsc()

# compute score as sum of 1- and 2- term interactions (currently just sum
# of matrix entries)


def c2Score(M, rowSet, colSet):
    return M[list(rowSet), :][:, list(colSet)].sum(axis=None)


def jaccard(pred, actual):
    intersectSize = len(set.intersection(
        pred[0], actual[0])) + len(set.intersection(pred[1], actual[1]))
    unionSize = len(set.union(pred[0], actual[0])) + \
        len(set.union(pred[1], actual[1]))
    return intersectSize / unionSize


def getPrecision(pred, actual):
    intersectSize = len(set.intersection(
        pred[0], actual[0])) + len(set.intersection(pred[1], actual[1]))
    return intersectSize / (len(pred[0]) + len(pred[1]))


def getRecall(pred, actual):
    intersectSize = len(set.intersection(
        pred[0], actual[0])) + len(set.intersection(pred[1], actual[1]))
    return intersectSize / (len(actual[0]) + len(actual[1]))


def getFMeasure(pred, actual):
    prec = getPrecision(pred, actual)
    rec = getRecall(pred, actual)
    return 0 if (prec + rec == 0) else (2 * prec * rec / (prec + rec))


def getRowPrecision(pred, actual, idx):
    intersectSize = len(set.intersection(pred[idx], actual[idx]))
    return intersectSize / len(pred[idx])


def getRowRecall(pred, actual, idx):
    intersectSize = len(set.intersection(pred[idx], actual[idx]))
    return intersectSize / len(actual[idx])


def getRowFMeasure(pred, actual, idx):
    prec = getRowPrecision(pred, actual, idx)
    rec = getRowRecall(pred, actual, idx)
    return 0 if (prec + rec == 0) else (2 * prec * rec / (prec + rec))


def sqrtWeightedAveDegree(M):
    _, n = M.shape
    colSums = M.sum(axis=0)
    colWeights = 1.0 / np.sqrt(np.squeeze(colSums.A) + 5)
    colDiag = sparse.lil_matrix((n, n))
    colDiag.setdiag(colWeights)
    W = M * colDiag
    return fastGreedyDecreasing(W, colWeights)


def logWeightedAveDegree(M):
    (_, n) = M.shape
    colSums = M.sum(axis=0)
    colWeights = 1.0 / np.log(np.squeeze(colSums.A) + 5)
    colDiag = sparse.lil_matrix((n, n))
    colDiag.setdiag(colWeights)
    W = M * colDiag
    logger.info("finished computing weight matrix")
    return fastGreedyDecreasing(W, colWeights)


def aveDegree(M):
    _, n = M.shape
    return fastGreedyDecreasing(M, [1] * n)


def subsetAboveDegree(M, col_thres, row_thres):
    M = M.tocsc()
    (m, n) = M.shape
    colSums = np.squeeze(np.array(M.sum(axis=0)))
    rowSums = np.squeeze(np.array(M.sum(axis=1)))
    colValid = colSums > col_thres
    rowValid = rowSums > row_thres
    M1 = M[:, colValid].tocsr()
    M2 = M1[rowValid, :]
    rowFilter = [i for i in range(m) if rowValid[i]]
    colFilter = [i for i in range(n) if colValid[i]]
    return M2, rowFilter, colFilter


# @profile
def fastGreedyDecreasing(M, colWeights):
    (m, n) = M.shape
    Ml = M.tolil()
    Mlt = M.transpose().tolil()
    rowSet = set(range(0, m))
    colSet = set(range(0, n))
    curScore = c2Score(M, rowSet, colSet)
    bestAveScore = curScore / (len(rowSet) + len(colSet))
    logger.info("finished setting up greedy")
    # *decrease* in total weight when *removing* this row
    rowDeltas = np.squeeze(M.sum(axis=1).A)
    colDeltas = np.squeeze(M.sum(axis=0).A)
    logger.info("finished setting deltas")
    rowTree = MinTree(rowDeltas)
    colTree = MinTree(colDeltas)
    logger.info("finished building min trees")

    numDeleted = 0
    deleted = []
    bestNumDeleted = 0

    while rowSet and colSet:
        if (len(colSet) + len(rowSet)) % 100000 == 0:
            logger.info("current set size = %d", len(colSet) + len(rowSet))
        (nextRow, rowDelt) = rowTree.getMin()
        (nextCol, colDelt) = colTree.getMin()
        if rowDelt <= colDelt:
            curScore -= rowDelt
            for j in Ml.rows[nextRow]:
                colTree.changeVal(j, -colWeights[j])
            rowSet -= {nextRow}
            rowTree.changeVal(nextRow, float('inf'))
            deleted.append((0, nextRow))
        else:
            curScore -= colDelt
            for i in Mlt.rows[nextCol]:
                rowTree.changeVal(i, -colWeights[nextCol])
            colSet -= {nextCol}
            colTree.changeVal(nextCol, float('inf'))
            deleted.append((1, nextCol))

        numDeleted += 1
        curAveScore = curScore / (len(colSet) + len(rowSet))

        if curAveScore > bestAveScore:
            bestAveScore = curAveScore
            bestNumDeleted = numDeleted

    # reconstruct the best row and column sets
    finalRowSet = set(range(m))
    finalColSet = set(range(n))
    for i in range(bestNumDeleted):
        if deleted[i][0] == 0:
            finalRowSet.remove(deleted[i][1])
        else:
            finalColSet.remove(deleted[i][1])
    return ((finalRowSet, finalColSet), bestAveScore)
