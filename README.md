# TLR9_Anisotropy

---

## Overview
These scripts were written by Dr. Stevie Reikine, while working in the lab of [Dr. Yorgo Modis](https://www.med.cam.ac.uk/modis/). 
They generate simulations of Fluorescence Anisotropy data for a binding model. The model is defined explicitly in the scripts. 

### Data

The data that was used to fit K1 and K4 for the paper is provided as a .txt file. 

### Fluorescence Anisotropy

Fluorescence Anisotropy can be a nice technique for determining the binding affinity between a small ligand (e.g. an oligonucleotide) and its larger binding partner (e.g. a protein). 

Some useful links to futher understand the technique: 
(1) [A good overview of the technique](https://www.horiba.com/en_en/technology/measurement-and-control-techniques/spectroscopy/fluorescence-spectroscopy/what-is-fluorescence-anisotropy-or-fluorescence-polarization/)

(2) [A thorough explanation of fitting Kd to FP data is found in CHAPTER 8 of this detailed guide.](https://research.fhcrc.org/content/dam/stripe/hahn/methods/biochem/beacon_fluorescence_guide.pdf)

(3) [A nice example of how to apply this technique](https://www.bmglabtech.com/high-throughput-protein-dna-measurement-using-fluorescence-anisotropy/)

### Equilibrium Binding Model

The simulations were performed to assess subsets of the equilibrium binding model of ssDNA binding to TLR9 and inducing dimerization. 
The full model of equilibrium binding that was examined is presented below in panel (A). 
The relationships between the macroscopic equilibrium binding constants is given in (B), and the solution for the concnetration of bound DNA, [D]bound, at equilibrium is presented in (C). 

![EquilibriumModel.png](EquilibriumModel.png)

### Description of the scripts

1. Simulation of D binding to P when there are two binding sites on the protein (P) for DNA (D). Assuming that the two binding sites are independent, the script takes the binding constants to these two sites (ie. microscopic binding constants Ka and Kb) and generates anisotropy data. If the two binding sites are independent, as we assume here, then the relationship between Ka, Kb and K1, K2 is explicitly defined. 

2. Simulation of a simplified version of the model where dimerization only occurs through K1 and K4. The script takes a given K1 and K4 and generates anisotropy data over a given range of P0. 

3. Fit of K1 and K4 to the data. 
