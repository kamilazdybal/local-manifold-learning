# Local manifold learning and its link to domain-based physics knowledge

This repository contains code and materials to reproduce the results from the "*Local manifold learning and its link to domain-based physics knowledge*" paper.

> K. Zdybał, G. D'Alessio, A. Attili, A. Coussement, J. C. Sutherland, A. Parente - *Local manifold learning and its link
to domain-based physics knowledge*, 2022, Applications in Energy and Combustion Science

### Our hypothesis

Local PCA can find the intrinsic low-dimensional parameterization of combustion systems in a data-driven way.

### Our methodology

<p align="center">
  <img src="https://github.com/kamilazdybal/local-manifold-learning/raw/main/figures/global-local-PCA.png" width="900">
</p>

## Data availability

All datasets used in the current work are provided in the [`data`](data/) directory. The datasets have been generated with the open-source [Spifire](https://spitfire.readthedocs.io/en/latest/) Python library.

## Reproducing paper results using Jupyter notebooks

All code used to produce the results in the original publication and in the supplementary material can be found in the Jupyter notebooks provided in the [`code`](code/) directory. [PCAfold](https://pcafold.readthedocs.io/en/latest/index.html) library is required.

Below, are the detailed guidelines on reproducing each figure from the original publication:

### 📄 $\S4.1$ The Burke-Schumann model 

This [Jupyter notebook](code/paper-simple-systems-Burke-Schumann.ipynb) can be used to reproduce results in $\S4.1$.

<p align="center">
  <img src="https://github.com/kamilazdybal/local-manifold-learning/raw/main/figures/BS-VQPCA.png" width="300">
</p>

### 📄 $\S4.2$ The chemical equilibrium model 

This [Jupyter notebook](code/paper-simple-systems-Chemical-Equilibrium.ipynb) can be used to reproduce results in $\S4.2$.


### 📄 $\S4.3$ The homogeneous reactor model 

This [Jupyter notebook](code/paper-simple-systems-Homogeneous-Reactor.ipynb) can be used to reproduce results in $\S4.3$.