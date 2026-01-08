# Bayesian Functional Time Series Modeling

This repository develops Bayesian models to extract interpretable latent signals from high dimensional time series data. 
The methods are designed for noisy, sparse, and evolving real world datasets.

## Motivation
Many real world systems generate high dimensional longitudinal data where underlying structure is unobserved and evolves over time. 
This project focuses on uncovering such latent structure using Bayesian inference.

## Methods
- Bayesian functional PCA and factor models
- Temporal priors for time dependent structure
- MCMC based inference
- Model diagnostics and simulation based validation
- Alignment and smoothing of latent trajectories

## Repository Structure
- src: core modeling code
- notebooks: exploratory analysis and examples
- scripts: runnable analysis pipelines
- data: small example or simulated datasets
- results: figures and output summaries

## Tech Stack
Python and R, Bayesian modeling, time series analysis, reproducible workflows

## Quick start
Open notebooks/01_simulated_example.ipynb for an end to end example on simulated high dimensional time series data.
The notebook fits a Bayesian latent factor model in PyMC and visualizes posterior uncertainty for the recovered latent signal.
