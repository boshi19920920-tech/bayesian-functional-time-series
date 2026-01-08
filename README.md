# Bayesian Functional Time Series Modeling

This repository provides a runnable example of Bayesian latent time series modeling for high dimensional data. 
It produces posterior diagnostics and a latent signal recovery figure saved to results/latent_recovery.png.

## Why it matters
Many real world datasets are high dimensional and evolve over time, while the true drivers are latent and noisy. 
This project demonstrates a Bayesian workflow to recover interpretable temporal structure with uncertainty quantification.

## Model at a glance
- Latent time series: Gaussian random walk prior
- Dimension loadings: Normal priors
- Observation model: Normal likelihood with shared noise
- Inference: MCMC sampling in PyMC
- Outputs: posterior diagnostics and latent recovery plot with uncertainty intervals

## Repository structure
- src: core modeling code
- notebooks: exploratory analysis and examples
- scripts: runnable pipelines
- data: small example or simulated datasets
- results: figures and output summaries

## How to run
Create a virtual environment, install dependencies, and run the script.

```bash
python -m venv .venv
source .venv/bin/activate  # macOS or Linux
# .venv\\Scripts\\activate  # Windows PowerShell

pip install -r requirements.txt
python scripts/run_simulation.py
