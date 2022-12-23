import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()


# no filter
sc.tl.pca(adata)
sc.pl.pca(adata)

#filter the adata by this recipe
sc.pp.recipe_zheng17(adata)
# performing pca on the filtered data
sc.tl.pca(adata)
# making a plot with the PCA adata
sc.pl.pca(adata)

#making neighborhood graph
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
#clustering 
sc.tl.leiden(adata)

sc.tl.tsne(adata)
sc.pl.tsne(adata)

sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata)

sc.tl.rank_genes_groups(adata, groupby='leiden', method='t-test')
sc.pl.rank_genes_groups(adata)

sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg')
sc.pl.rank_genes_groups(adata)

#PC Pericytes, aaSMC arteriolar SMC, MG Microglia, EC1 EpithelialC type 1, vEC venous EC, AC Astrocyte --> cell types picked
marker_genes = ['F13a1','CD86','Ccl8','Neurl3','Pf4','Tagap']
    
    
for i in range(0, len(marker_genes)):
    sc.tl.tsne(adata)
    sc.pl.tsne(adata, color=marker_genes[i]) #not sure why this isnt doing for each one of the indexes


# marker_genes_2 = {'PC': 'F13a1', 'aaSMC':'CD86', 'MG': "Ccl8", 'EC1': 'IGfbpl1', 'vEC': 'Pf4', 'AC': 'Tagap'}
#
# sc.pl.dotplot(adata, marker_genes_2, 'leiden')

# sc.pl.matrixplot(adata, marker_genes_2, 'leiden', dendrogram=True, cmap='Blues', standard_scale='var', colorbar_title='column scaled\nexpression')

clusters = {
     '21': 'PC',
     '4': 'aaSMC',
     '10': 'MG',
     '39': 'EC1',
     '22': 'vEC',
     '15': 'AC'
}

adata.obs['celltypes'] = adata.obs['leiden'].map(clusters).astype('category')

sc.pl.umap(adata, color='celltypes', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2,
           save='cell_types.png', show=True)


