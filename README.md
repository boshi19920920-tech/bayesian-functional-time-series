# Bayesian Functional Time Series Modeling

This repository provides a runnable example of Bayesian latent time series modeling for high dimensional data.
The workflow produces posterior diagnostics and a latent signal recovery figure saved to `results/latent_recovery.png`.

## Why this matters
Many real world datasets are high dimensional, noisy, and evolve over time, while the true driving structure is latent.
This project demonstrates a Bayesian approach for recovering interpretable temporal signals with uncertainty quantification.

## Model at a glance
- Latent time series modeled with a Gaussian random walk prior
- Dimension specific loadings with shrinkage priors
- Observation model with shared noise
- Bayesian inference via MCMC using PyMC
- Outputs include posterior diagnostics and latent recovery plots

## Repository structure
- `src/`: core modeling code
- `notebooks/`: exploratory analysis and examples
- `scripts/`: runnable analysis pipelines
- `data/`: simulated or small example datasets
- `results/`: figures and output summaries

python -m venv .venv
source .venv/bin/activate  # macOS or Linux
# .venv\Scripts\activate  # Windows PowerShell

pip install -r requirements.txt
python scripts/run_simulation.py

## Example output

Running the script generates the following latent signal recovery plot with posterior uncertainty.

![Latent signal recovery](https://raw.githubusercontent.com/boshi19920920-tech/bayesian-functional-time-series/main/results/latent_recovery.png)


## How to run
Create a virtual environment, install dependencies, and run the simulation script.

```bash
