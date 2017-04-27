#Caroline Lee
#3/09/17
#Lab - Stock Performance Analysis
#	Load stock data from .csv file
#	Slice each np array by year and compute specified measurements
#	Compute overall specified measurements for each np array
#	Score based on chosen data points

import numpy as np

#load data into separate arrays for each column 
AAPL_array, MSFT_array, XOM_array, SPX_array = np.loadtxt('stock_px.csv',
												dtype='float', 
												skiprows=1,
												delimiter=',', 
												usecols=(1,2,3,4), 
												unpack=True
												)

#get min,max,mean,med,var of specific year slice
def process_slice(arr, year):
	slice_min = np.amin(arr)
	slice_max = np.amax(arr)
	slice_mean = np.mean(arr)
	slice_med = np.median(arr)
	slice_var = np.var(arr)

	#put slice stats in np array
	slice_stats =np.array([('Min', slice_min), ('Max', slice_max), ('Mean', slice_mean), 
	('Median', slice_med), ('Variance', slice_var)], dtype=[('keys', '|S8'), 
	('data', 'f4')])#indexed

	#print data for visual aid
	print year + ": " + "Min = " + str(slice_min) + \
	" | Max = " + str(slice_max) + " | Mean = " + str(slice_mean) + \
	" | Med = " + str(slice_med) + " |  Var = " + str(slice_var) 

	#return np array containing slice stats
	return slice_stats

#get min,max,mean,med,var of overall array	
def process_overall(arr):
	min_overall = np.amin(arr)
	max_overall = np.amax(arr)
	mean_overall = np.mean(arr)
	med_overall = np.median(arr)
	var_overall = np.var(arr)

	#put overall stats in np array
	overall_stats = np.array([('Overall Min', min_overall), ('Overall Max', max_overall),
		('Overall Mean', mean_overall), ('Overall Median', med_overall),
		 ('Overall Var', var_overall)], dtype=[('keys', '|S32'), ('data', 'f4')])#indexed

	#print data for visual aid
	print "\nOverall Min: " + str(min_overall) + "\nOverall Max: " + \
	str(max_overall) + "\nOverall Mean: " + str(mean_overall) + \
	"\nOverall Median: " + str(med_overall) + "\nOverall Variance: " + \
	str(var_overall) + "\n"

	#return np array containing overall stats
	return overall_stats

#this is my own metric - (overall variance)/(percent of growth from 1st year to 8th year)
def give_score(ov, s03, s11):
	begin_mean = s03['data'][2]#find data points using indexing
	end_mean = s11['data'][2]
	growth = ((end_mean - begin_mean)/begin_mean)*100
	score = ov['data'][4]/growth
	return np.around(score, 2)

#slice array by year, get stats from defs above
def slice_and_dice(array, name):
	print name
	slice_03 = array[:252]
	stats_03 = process_slice(slice_03, '2003')
	slice_04 = array[252:504]
	stats_04 = process_slice(slice_04, '2004')
	slice_05 = array[504:756]
	stats_05 = process_slice(slice_05, '2005')
	slice_06 = array[756:1007]
	stats_06 = process_slice(slice_06, '2006')
	slice_07 = array[1007:1258]
	stats_07 = process_slice(slice_07, '2007')
	slice_08 = array[1258:1511]
	stats_08 = process_slice(slice_08, '2008')
	slice_09 = array[1511:1763]
	stats_09 = process_slice(slice_09, '2009')
	slice_10 = array[1763:2015]
	stats_10 = process_slice(slice_10, '2010')
	slice_11 = array[2015:2214]
	stats_11 = process_slice(slice_11, '2011')

	#get overall stats
	overall = process_overall(array) 

	#get score
	final_score = give_score(overall, stats_03, stats_11)

	#print score for visual aid
	print "Lee Score: " + str(final_score) + "\n"

#------------MAIN---------------#  
#	   compute all stats 	    #	
slice_and_dice(AAPL_array, 'AAPL')
slice_and_dice(MSFT_array, 'MSFT')
slice_and_dice(XOM_array, 'XOM')
slice_and_dice(SPX_array, 'SPX')

