import numpy as np
import matplotlib.pyplot as plt

import pymc as pm
import arviz as az


def simulate_data(T: int = 80, D: int = 25, sigma: float = 0.6, seed: int = 42):
    rng = np.random.default_rng(seed)
    t = np.arange(T)

    latent_true = 0.8 * np.sin(2 * np.pi * t / 30) + 0.3 * np.cos(2 * np.pi * t / 12)
    w = rng.normal(0.0, 1.0, size=D)
    Y = latent_true[:, None] * w[None, :] + rng.normal(0.0, sigma, size=(T, D))

    return t, latent_true, Y


def fit_bayesian_latent_model(Y: np.ndarray, rw_sigma: float = 0.25, draws: int = 1000, tune: int = 1000):
    T, D = Y.shape

    with pm.Model() as model:
        latent = pm.GaussianRandomWalk("latent", sigma=rw_sigma, shape=T)
        loading = pm.Normal("loading", mu=0.0, sigma=1.0, shape=D)
        obs_sigma = pm.HalfNormal("obs_sigma", sigma=1.0)

        mu = pm.Deterministic("mu", latent[:, None] * loading[None, :])
        pm.Normal("y_obs", mu=mu, sigma=obs_sigma, observed=Y)

        idata = pm.sample(draws=draws, tune=tune, chains=2, target_accept=0.9, progressbar=True)

    return idata


def plot_results(t, latent_true, idata, save_path: str = "results/latent_recovery.png"):
    latent_post = idata.posterior["latent"].stack(sample=("chain", "draw")).values
    latent_mean = latent_post.mean(axis=1)
    latent_hdi = az.hdi(latent_post.T, hdi_prob=0.94)

    plt.figure()
    plt.plot(t, latent_true, label="true")
    plt.plot(t, latent_mean, label="posterior mean")
    plt.fill_between(t, latent_hdi[:, 0], latent_hdi[:, 1], alpha=0.3, label="94% HDI")
    plt.title("Latent signal recovery")
    plt.xlabel("time")
    plt.ylabel("latent")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.show()


def main():
    t, latent_true, Y = simulate_data()
    idata = fit_bayesian_latent_model(Y)

    az.plot_trace(idata, var_names=["obs_sigma"])
    plt.tight_layout()
    plt.show()

    plot_results(t, latent_true, idata)


if __name__ == "__main__":
    main()
