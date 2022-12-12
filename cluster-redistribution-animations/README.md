
# Animations of cluster re-distribution inside VQPCA

The animations below show how cluster definitions change iteratively during VQPCA. 

## Chemical equilibrium (EQ) dataset

### Auto scaling on a dataset $\mathbf{X} = [T, Y_i]$

#### Initialization with $f$-bins

The observations in clusters get re-distributed in an iterative process from the initial bins of the mixture fraction ($f$) vector:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0mf-scaling-auto-q1-k8.gif)

#### Random initialization

The observations in clusters get re-distributed in an iterative process from the initial randomly generated clusters:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0randombest-scaling-auto-q1-k8.gif)

#### Uniform initialization

The observations in clusters get re-distributed in an iterative process from the initial uniformly generated clusters:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0uniform-scaling-auto-q1-k8.gif)

### Pareto scaling on a dataset $\mathbf{X} = [Y_i]$

#### Initialization with $f$-bins

The observations in clusters get re-distributed in an iterative process from the initial bins of the mixture fraction ($f$) vector:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0mf-scaling-pareto-q1-k8.gif)

#### Random initialization

The observations in clusters get re-distributed in an iterative process from the initial randomly generated clusters:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0randombest-scaling-pareto-q1-k8.gif)

#### Uniform initialization

The observations in clusters get re-distributed in an iterative process from the initial uniformly generated clusters:

![Screenshot](clusters-animation-EQ-CH4-VQPCA-idx0uniform-scaling-pareto-q1-k8.gif)

## Direct numerical simulation (DNS) dataset
