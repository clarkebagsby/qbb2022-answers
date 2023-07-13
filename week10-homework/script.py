import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# # no filter
# sc.tl.pca(adata)
# sc.pl.pca(adata)
#
# # #filter the adata by this recipe
# sc.pp.recipe_zheng17(adata)
# # # performing pca on the filtered data
# sc.tl.pca(adata)
# # # making a plot with the PCA adata
# sc.pl.pca(adata)

#making neighborhood graph
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
#clustering 
sc.tl.leiden(adata)

sc.tl.tsne(adata)
# sc.pl.tsne(adata)

# sc.tl.umap(adata, maxiter=1000)
# sc.pl.umap(adata)
# #leiden gives a certain number of groups the genes fall inti
# sc.tl.rank_genes_groups(adata, groupby='leiden', method='t-test')
# sc.pl.rank_genes_groups(adata)
#
# sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg')
# sc.pl.rank_genes_groups(adata)



#support plot
sc.pl.tsne(adata, color=['Hba-a1', 'Gad1', 'Gad2', 'Pax6', 'Meg3'], legend_loc='right margin')
sc.pl.tsne(adata, color='leiden', legend_loc='right margin')



# Gad1,2 cell type GABAergic neurons
# Hes1 cell type progenitor neurons
#Pax6 cell type astrocytes
#Meg3 cell type multipolar neurons 
#Hba-a1 cell type erythocytes

        
clusters = {
     '0': 'Gad1-GABAergic neurons',
     '1': '',
     '2': '',
     '3': 'Pax6-astrocytes',
     '4': 'aaSMC',
     '5': '',
     '6': 'Meg3-multipolar neurons',
     '7': '',
     '8': '',
     '9': '',
     '10': '',
     '11': 'Hes1-progentior neurons',
     '12': '',
     '13': '',
     '14': '',
     '15': '',
     '16': '',
     '17': '',
     '18': '',
     '19': 'Hba19-erythocytes',
     '20': '',
     '21': '',
     '22': '',
     '23': '',

}

adata.obs['celltypes'] = adata.obs['leiden'].map(clusters).astype('category')

sc.pl.tsne(adata, color='celltypes', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2,
           save='cell_types.png', show=True)



