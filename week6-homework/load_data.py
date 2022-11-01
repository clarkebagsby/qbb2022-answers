#!/usr/bin/env python

import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = np.copy(mat)
    for i in range(N):
        bg = np.mean(mat[np.arange(i, N), np.arange(N - i)])
        mat2[np.arange(i, N), np.arange(N - i)] -= bg
        if i > 0:
            mat2[np.arange(N - i), np.arange(i, N)] -= bg
    return mat2
def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = np.where(mat[1:-1, 1:-1] == 0)
    nmat = np.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations

    in1_fname, in2_fname, infname_40kb_data, infname_40kb_bins, bin_fname, out_fname = sys.argv[1:7]
    data1 = np.loadtxt(in1_fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = np.loadtxt(in2_fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data_40kb = np.loadtxt(infname_40kb_data, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = np.loadtxt(bin_fname, dtype=np.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    frags_40kb = np.loadtxt(infname_40kb_bins, dtype=np.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    print(frags_40kb)

    chrom = b'chr15'
    chrom_40kb = b'chr15'
    
    start = 11170245 
    end = 12070245
    
    start_40kb = 54878 #this is for the insulation bins
    end_40kb = 54951
    
    start_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1

    start40kb_bin = frags_40kb['bin'][np.where((frags_40kb['chr'] == chrom_40kb) &
                                         (frags_40kb['start'] <= start_40kb) &
                                         (frags_40kb['end'] > start_40kb))[0][0]]
    end40kb_bin = frags_40kb['bin'][np.where((frags_40kb['chr'] == chrom_40kb) &
                                       (frags_40kb['start'] <= end_40kb) &
                                       (frags_40kb['end'] > end_40kb))[0][0]] + 1
    print(start40kb_bin)
    print(end40kb_bin)
# filter the data1/2 frames by the start_bin and end_bin

    data1_new = data1[np.where((data1["F1"] >= start_bin) & (data1["F2"] < end_bin))]
    data2_new = data2[np.where((data2["F1"] >= start_bin) & (data2["F2"] < end_bin))]


# [(343068, 343068, 2459.883712)] --score format
# # log transform the scores from the above code


    data1_new['score'] = np.log(data1_new['score'])
    data2_new['score'] = np.log(data2_new['score'])


# # shift by the start_bin--> Mike said not required because the filtering has done this 

    # data1['F1'] = data1['F1'] - start_bin


# # make matrix with mat[sparse['F1'][i], sparse['F2'][i]] = sparse['score'][i]
    axis_length = end_bin - start_bin # this gives the axises
    

    heatmap_matrix = np.zeros((axis_length, axis_length))

    heatmap_matrix[data1_new['F1'] - start_bin, data1_new['F2'] - start_bin] = data1_new['score'] #forward
    heatmap_matrix[data1_new['F2'] - start_bin, data1_new['F1'] - start_bin] = data1_new['score'] #reverse



    #need to do matrix for data2
    heatmap_matrix2 = np.zeros((axis_length, axis_length))

    heatmap_matrix2[data2_new['F1'] - start_bin, data2_new['F2'] - start_bin] = data2_new['score'] #forward
    heatmap_matrix2[data2_new['F2'] - start_bin, data2_new['F1'] - start_bin] = data2_new['score'] #reverse


# # graph
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(heatmap_matrix, vmax=np.max(heatmap_matrix), cmap = "magma")

    ax[1].imshow(heatmap_matrix2, vmax=np.max(heatmap_matrix2), cmap = "magma")
# difference plot
    remove_1 = remove_dd_bg(heatmap_matrix)
    remove_2 = remove_dd_bg(heatmap_matrix2)

    smooth_1 = smooth_matrix(remove_1)
    smooth_2 = smooth_matrix(remove_2)

    test = smooth_2 - smooth_1

    ax[2].imshow(test, vmax=np.max(test), cmap = "seismic")
    plt.savefig("wk6.png")

# #insulation scores

# #filtering the data by the new bins --> make sure the filtering is correct
    data_40kb_data = data_40kb[np.where((data_40kb["F1"] >= start_40kb) & (data_40kb["F2"] < end_40kb))]

# #log transform the above
    data_40kb_data['score'] = np.log(data_40kb_data['score'])
    

# #making matrix 
    insulator_axis = end40kb_bin - start40kb_bin # this gives the axises
    print(insulator_axis)

    insulator_matrix = np.zeros((insulator_axis, insulator_axis))
    insulator_matrix[data_40kb_data['F1'] - start40kb_bin, data_40kb_data['F2'] - start40kb_bin] = data_40kb_data['score'] #
    




#
# insulation_matrix[data1_length['F1'] - new_start_bin, data1_length['F2'] - new_start_bin] = data1_new['score'] #forward
# insulation_matrix[data1_length['F2'] - new_start_bin, data1_length['F1'] - new_start_bin] = data1_new['score'] #reverse

# for i iin range(5, lenght-4):


# #use heatmap code from above to make another
# #input code from homework
#
#
#
#

if __name__ == "__main__":
    main()