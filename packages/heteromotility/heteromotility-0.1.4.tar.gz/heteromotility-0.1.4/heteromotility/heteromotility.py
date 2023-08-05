#!/usr/bin/env python3
from __future__ import division, print_function

from hmtools import *
from hmstats import GeneralFeatures, MSDFeatures, RWFeatures
from hmtrack import *
from hmio import *
import hmtests
import csv
import glob
import sys
import argparse
#import matplotlib.pyplot as plt
import pickle
import numpy as np
np.seterr(all='raise')

'''
Extracts motility feature information from provided cell locations or paths.

$ heteromotility.py --help

for usage information.
'''

def main():

    # Parse CLI args
    parser = argparse.ArgumentParser('Calculate motility features from cell locations or cell paths')
    parser.add_argument('input_dir', action='store', default = ['./'], nargs = 1, help = "path to input directory of CSVs")
    parser.add_argument('output_dir', action='store', default = ['./'], nargs = 1, help = "directory for motility_statistics.csv export")
    parser.add_argument('--exttrack', action = 'store', default = [False], nargs = 1, help = "specifies external tracking algo, provide location of cell_ids.pickle")
    parser.add_argument('--tracksX', action = 'store', default = [False], nargs = 1, help = "path to input CSV containing N x T matrix of X locations")
    parser.add_argument('--tracksY', action = 'store', default = [False], nargs = 1, help = "path to input CSV containing N x T matrix of Y locations")
    parser.add_argument('--sanity', default = 10000, help = "integer [px] determining the maximum sane movement of an object. Default = 10000 px")
    parser.add_argument('--move_thresh', default = 10, help = "highest speed to check as a threshold for movement [px/frame]. Default = 10")
    parser.add_argument('--seg', action = 'store', default = ['otsu'], nargs = 1, help = "name of an alternate seg method being used")
    parser.add_argument('--detailedbalance', default = [-1], nargs = 1, help = "Split cell paths for detailed balance calculation, with a provided minimum path size")
    parser.add_argument('--dbmax', default = None, nargs = 1, help = 'Maximum tau for detailed balance splitting')
    parser.add_argument('--output_suffix', default = [False], nargs = 1, help = "Optional suffix to place on output csv name")
    parser.add_argument('--interp_lim', default = 3, help = "Number of frames allowed for interpolation if an object is not detected temporarily. Default = 3")
    args = parser.parse_args()

    #------------------------------
    # IMPORT CENTROIDS FROM CSV
    #------------------------------
    input_dir = args.input_dir[0] + '*centroids*.csv'
    output_dir = args.output_dir[0]
    sanity = int(args.sanity)
    move_thresh = int(args.move_thresh)
    seg = args.seg[0]
    exttrack = args.exttrack[0]
    tracksX_path = args.tracksX[0]
    tracksY_path = args.tracksY[0]
    detailed_balance = int(args.detailedbalance[0])
    if args.dbmax != None:
        dbmax = int(args.dbmax[0])
    output_suffix = args.output_suffix[0]
    interp_lim = int(args.interp_lim)

    # Imports a directory of CSVs with centroid positions
    # Creates list of lists, each internal list == one time points
    # inner lists contain tuples with XY coors of centroid locations

    if exttrack == False and tracksX_path == False:
        centroid_arrays = import_centroids(input_dir)
    elif tracksX_path != False:
        tracksX, tracksY = import_tracksXY(tracksX_path, tracksY_path)
    else:
        pass

    if np.any(tracksX) == False:
        sys.exit()

    #------------------------
    # ESTABLISH OBJECT PATHS
    #------------------------

    # See hmtrack.CellPaths for tracking implementation
    # if exttrack has specific an external pickle, load that as the cell_ids instead
    if exttrack == False and tracksX_path == False:
        cp = CellPaths( centroid_arrays = centroid_arrays, sanity_px = sanity, interp_lim = interp_lim )
        cell_ids = cp.cell_ids
    elif tracksX_path != False:
        print('Tracking ', tracksX_path)
        cp = CellPaths(tracksX = tracksX, tracksY = tracksY, sanity_px = sanity, interp_lim = interp_lim)
    else:
        cp = CellPaths( cell_ids = pickle.load( file(exttrack) ), sanity_px = sanity, interp_lim = interp_lim )
        cell_ids = cp.cell_ids

    #------------------------------
    # CHECK FOR REMAINING CELLS
    #------------------------------

    # Checks to see if any cells remain after removing cells
    # that fail the sanity check
    # If no cells are left, exits the script gracefully
    # without pickling cell_ids or removed_ids

    check_remaining_cells(cp.cell_ids)

    #------------------------------
    # DETAILED BALANCE ANALYSIS
    #------------------------------
    if detailed_balance != -1:
        from hmdetail import DetailedBalance
        db = DetailedBalance(cp.cell_ids, min_split = detailed_balance, tau_max = dbmax)
        db.split_id_features(db.multi_split, output_dir=output_dir, output_suffix = output_suffix)
        sys.exit()

    #------------------------------
    # CALCULATE MOTILITY STATISTICS
    #------------------------------

    gf = GeneralFeatures(cp.cell_ids, move_thresh = move_thresh)

    #--------------------------------
    #     MEAN SQUARE DISPLACEMENT
    #--------------------------------

    msdf = MSDFeatures(cp.cell_ids)

    #--------------------------------
    # RANDOM WALK MODELING
    #--------------------------------
    # Compares each cell's path to a random walk using simulations to estimate
    # linearity and net_distance of comparable random walks
    # Compares to kurtosis of random walk displacement distribution (Rayleigh)

    rwf = RWFeatures(cp.cell_ids, gf)

    #------------------------------
    # WRITE STATISTICS TO CSV
    #------------------------------

    # Checks to see if non-standard segmentation is being used
    # Will output file with an altered name if yes
    def check_flags( flags ):
        if 'sobel' in flags[0]:
            output_name = 'motility_statistics_sobel.csv'
            sobel = True
        else:
            output_name = 'motility_statistics.csv'
            sobel = False

        if output_suffix != False:
            output_name = 'motility_statistics_' + output_suffix + '.csv'
            sobel = False

        return output_name, sobel

    flags = [seg, output_suffix]
    output_name, sobel = check_flags( flags )

    ind_outputs = single_outputs_list(cp.cell_ids, gf, rwf, msdf, output_dir, suffix=output_suffix)
    merged_list = make_merged_list(ind_outputs, gf, rwf)
    write_motility_stats(output_dir, output_name, gf, rwf, merged_list)

    #------------------------------
    # Run Unit Tests
    #------------------------------

    #print("test_sanity = ", hmtests.test_sanity())
    #print("test_removal = ", hmtests.test_removal())

if __name__ == "__main__":
    main()
