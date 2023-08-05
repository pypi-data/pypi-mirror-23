# wdecoster
import numpy as np
import pandas as pd
from .version import __version__


def getN50(readlengths):
	'''
	Get read N50.
	Based on https://github.com/PapenfussLab/Mungo/blob/master/bin/fasta_stats.py
	'''
	return readlengths[np.where(np.cumsum(readlengths)>=0.5*np.sum(readlengths))[0][0]]


def removeLengthOutliers(df, columnname):
	'''
    Remove records with length-outliers above 3 standard deviations from the median
    '''
	return df[df[columnname] < (np.median(df[columnname]) + 3 * np.std(df[columnname]))]


def aveQual(quals):
	'''	Calculation function: Receive the integer quality scores of a read and return the average quality for that read'''
	return sum(quals) / len(quals)


def readstats(readlengths, qualities):
	'''
	For an array of readlengths, return a dictionary containing:
	- the number of reads
	- the total number of bases sequenced
	- the median length
	- the mean length
	- the top 5 longest reads and their quality
	- the maximum average basecall quality
	- the fraction and number of reads above > Qx (use a set of cutoffs depending on the observed quality scores)
	'''
	res = dict()
	res["NumberOfReads"] = readlengths.size
	res["TotalBases"] = np.sum(readlengths)
	res["MedianLength"] = np.median(readlengths)
	res["MeanLength"] = np.mean(readlengths)
	indices_top_L = np.argpartition(readlengths, -5)[-5:]
	res["MaxLengthsAndQ"] = [list(e) for e in zip(list(readlengths[indices_top_L]),  list(qualities[indices_top_L]))]
	indices_top_Q = np.argpartition(qualities, -5)[-5:]
	res["MaxQualsAndL"] = [list(e) for e in zip(list(readlengths[indices_top_Q]),  list(qualities[indices_top_Q]))]
	qualgroups = [q for q in range(5,50,5) if q < np.amax(qualities) + 5]
	res["QualGroups"] = dict()
	for q in qualgroups:
		numberAboveQ = np.sum(qualities > q)
		res["QualGroups"][q] = (numberAboveQ, numberAboveQ / res["NumberOfReads"])
	return res


def writeStats(datadf, outputfile):
	'''
	Call calculation function and write to file
	'''
	stat = readstats(np.array(datadf["lengths"]), np.array(datadf["quals"]))
	with open(outputfile, 'wt') as output:
		output.write("Number of reads:\t{}\n".format(stat["NumberOfReads"]))
		output.write("Total bases:\t{}\n".format(stat["TotalBases"]))
		output.write("Median read length:\t{}\n".format(stat["MedianLength"]))
		output.write("Mean read length:\t{}\n".format(round(stat["MeanLength"],2)))
		output.write("Readlength N50:\t{}\n".format(getN50(datadf["lengths"])))
		output.write("\n")
		output.write("Top 5 read lengths and their average basecall quality score:\n")
		for length, qual in sorted(stat["MaxLengthsAndQ"], key=lambda x: x[0], reverse=True):
			output.write("Length: {}bp\tQ: {}\n".format(length, round(qual, 2)))
		output.write("\n")
		output.write("Top 5 average basecall quality scores and their read lengths:\n")
		for length, qual in sorted(stat["MaxQualsAndL"], key=lambda x: x[1], reverse=True):
			output.write("Length: {}bp\tQ: {}\n".format(length, round(qual, 2)))
		output.write("\n")
		output.write("Number of reads and fraction above quality cutoffs:\n")
		for q in sorted(stat["QualGroups"].keys()):
			output.write("Q{}:\t{}\t{}%\n".format(q, stat["QualGroups"][q][0], round(100*stat["QualGroups"][q][1],2)))
