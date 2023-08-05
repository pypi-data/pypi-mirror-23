'''
#---------------------------
# MODULE CONTENTS
#---------------------------
Functions to/for:
Manipulate/shape data structures

'''
from __future__ import print_function
import numpy as np

def dict2array(d):
    # takes dict of lists
    # d = {0: [a1, a2, a3], 1: [b1,b2,b3], 2: [...]}
    # merges into list of lists
    # output = [ [a1,a2,a3], [], [] ]
    output = []
    for u in d:
        output.append(list(d[u]))
    return output

def dictofdict2array(top_dict):
	# Takes dict of
	# dict_of_dict = { a: {x1 : a1, x2 : a2, x3 : a3},
	#				   b: {x1 : b1, x2 : b2, x3 : b3},
	#				   c: {x1 : c1, x2 : c2, x3 : c3} }
	# Outputs list of lists
	# output = [ [a1,b1,c1], [a2,b2,c2]... ]
	output = []
	i = 0
	while i < len( top_dict[ list(top_dict)[0] ] ):
		row = []
		for key1 in top_dict:
			row.append( top_dict[key1][ list(top_dict[key1])[i] ] )
		output.append(row)
		i += 1
	return output

def tripledict2array(top_dict):
	output = []
	j = 0
	while j < len( top_dict[ list(top_dict)[0] ][ list(top_dict[ list(top_dict)[0] ])[0] ] ):
		row = []
		for key1 in top_dict:
			for key2 in top_dict[key1]:
				if type(top_dict[key1][key2][ list(top_dict[key1][key2])[j] ]) == list:
					for item in top_dict[key1][key2][ list(top_dict[key1][key2])[j] ]:
						row.append(item)
				else:
					row.append( top_dict[key1][key2][ list(top_dict[key1][key2])[j] ] )
		output.append(row)
		j += 1
	return output

def cell_ids2tracks(cell_ids):
    N = len(cell_ids)
    T = len(cell_ids[list(cell_ids)[0]])
    tracksX = np.zeros([N,T])
    tracksY = np.zeros([N,T])

    n_count = 0
    for c in cell_ids:
        cell = cell_ids[c]
        for t in range(T):
            tracksX[n_count, t] = cell[t][0]
            tracksY[n_count, t] = cell[t][1]
        n_count = n_count + 1

    return tracksX, tracksY

# Super fast deduping of lists, preserves order
# Credit to Peterbe
# http://www.peterbe.com/plog/uniqifiers-benchmark
def dedupe(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

# Takes a list of lists of lists [ [ [], ... ], [ [], ... ], ...]
# Returns list of lists, with each nth list containing the values of the
# nth tertiary lists merged together
import itertools
def merge_flat_lists(lists):
	# lists = [
    #           [ [...], [...], [...] ],
    #           [ [...], [...], ... ], ...
    #                                        ]
	merged_list = []
	i = 0
	while i < len(lists[0]):
		tmp_list = []
		for l in lists:
			tmp_list.append(l[i])

		tmp_merged = list( itertools.chain( *tmp_list ) )
		merged_list.append(tmp_merged)
		i += 1

	# merged_list = [ [all vals for one cell], [...], ... ]
	return merged_list

def single_outputs_list(cell_ids, gf, rwf, msdf, output_dir, suffix=None):
    # Creates a list of lists for writing out statistics
    # Ea. internal list is a single cell's stats
    output_list = []
    if suffix:
        output_dir = output_dir + str(suffix)
    for cell in cell_ids:
        output_list.append([ output_dir, cell, gf.total_distance[cell], gf.net_distance[cell],
                            gf.linearity[cell], gf.spearmanrsq[cell], gf.progressivity[cell], gf.max_speed[cell],
                            gf.min_speed[cell], gf.avg_speed[cell], msdf.alphas[cell], rwf.hurst_RS[cell], rwf.nongaussalpha[cell],
                            rwf.disp_var[cell], rwf.disp_skew[cell], rwf.diff_linearity[cell], rwf.diff_net_dist[cell] ])

    return output_list

def make_merged_list(ind_outputs, gf, rwf):
    autocorr_array = dict2array(rwf.autocorr)
    #partial_acorr_array = dict2array(rwf.partial_acorr)
    diff_kurtosis_array = dictofdict2array(rwf.diff_kurtosis)
    #diff_moving_kurt_array = tripledict2array(rwf.diff_moving_kurt)
    avg_moving_speed_array = dictofdict2array( gf.avg_moving_speed )
    time_moving_array = dictofdict2array( gf.time_moving )
    turn_list = tripledict2array(gf.turn_stats)
    theta_list = tripledict2array(gf.theta_stats)

    merged_list = merge_flat_lists([ind_outputs, diff_kurtosis_array, avg_moving_speed_array, time_moving_array, autocorr_array, turn_list, theta_list])
    return merged_list
