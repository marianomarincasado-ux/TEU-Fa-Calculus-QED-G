# Topological Electron Universe (TEU) - Computational Physics Repository

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Physics](https://img.shields.io/badge/Physics-QED%20%7C%20Quantum%20Gravity-purple)
![Status](https://img.shields.io/badge/Status-Research%20Preprint-success)

This repository contains the numerical simulations, analytical resolutions, and stochastic (Monte Carlo) engines that computationally validate the **TEU (Topological Electron Universe)** model. 

The TEU model proposes that the quantum vacuum possesses a sub-diffusive fractal topology (Cantor Dust with dimension $\mu \approx 0.757$). Under this geometric framework, fundamental constants such as the electron mass ($m_e$), the fine-structure constant ($\alpha$), and the universal gravitational constant ($G$) cease to be free parameters and become emergent properties (eigenvalues) of spatial impedance.

---

## 📂 Scripts Directory and Physical Validation

The scripts are divided into three fundamental areas of physics: **Mass Genesis and Symmetries**, **Gravitational Unification**, and **QED Audit ($g-2$)**.

### 1. Mass Genesis and Preservation of Gauge Symmetries
These scripts computationally demonstrate how the interaction between particle spin and the vacuum's fractal roughness generates inertia (mass), without breaking classical electromagnetism.

* 📄 **`teu_mass_gap_solver.py` (Analytical Mass Gap Calculator)**
    * **What it does:** Analytically solves the fractal Klein-Gordon equation using the unified topological parameters ($\alpha^{-1}, K_{geo}$). 
    * **Physics:** Mathematically proves that the electron mass ($9.109 \times 10^{-31}$ kg) is not an intrinsic property, but the Root Mean Square (RMS) of topological scattering events in a Cantor metric.
* 📄 **`teu_photon_mass_solver.py` (Stochastic Symmetry Engine)**
    * **What it does:** Pure Monte Carlo simulation of quantum field transport through a simulated sub-diffusive vacuum.
    * **Physics:** Answers the classic objection: *"If the vacuum is rough, light should have mass"*. The script demonstrates that the electron's Dirac matrices (non-commutative algebra) "stumble" upon the fractal and generate variance (inertia). Conversely, the photon (Spin-1 vector boson) governed by $U(1)$ Gauge symmetry commutes perfectly over the noise, resulting in a stochastic variance of `0.000000`. Light travels massless.
* 📄 **`teu_unified_gauge_mass.py` (The Hybrid Engine)**
    * **What it does:** Combines the physical mass scale derived from CODATA with the stochastic Gauge symmetry filter.
    * **Physics:** Filters the available friction energy in the vacuum through 10 million Monte Carlo steps. The electron preserves its real SI mass (kg) with a convergence error of `0.01%`, while the photon multiplies this physical scale by absolute zero. 

### 2. Unification: Gravity as Attenuated Electrodynamics
Scripts aimed at demonstrating that macroscopic kinematics (Newton/Einstein) are topologically isomorphic to attenuated quantum electrodynamics.

* 📄 **`teu_quantum_gravity_unification.py`**
    * **What it does:** Evaluates gravitational interaction as a coherent superposition of *Zitterbewegung* radiation filtered by the vacuum's depth ($\mathcal{D} \approx 51.52$).
    * **Physics:** Derives the exact value of the Universal Gravitational Constant ($G \approx 6.674 \times 10^{-11}$) starting **exclusively** from electromagnetic ($\alpha$) and geometric parameters, without using torsion balance measurements as inputs.

### 3. QED Audit and $g-2$ Analysis
Scripts used to calibrate the vacuum geometry by isolating divergences in the perturbative coefficients of Quantum Electrodynamics.

* 📄 **`teu_vegas_integration.py`**
    * **What it does:** Implements a variant of the VEGAS Monte Carlo algorithm incorporating a Fractal Density Filter $\mathcal{W}(x; \mu, A)$.
    * **Physics:** Proves that by discounting the "spurious volume" from forbidden topological gaps in the 5th-order integral ($C_5$), the current perturbative consensus ($\approx 6.80$) naturally collapses to the value predicted by the TEU model ($\approx 6.60$).
* 📄 **`teu_g2_anomaly_solver.py`** *(See Run Log below)*
    * **What it does:** Reconstructs the anomalous magnetic moment of the electron using the TEU geometric ansatz instead of Feynman diagrams.

---

## ⚙️ Requirements and Execution

All scripts are written in **Python 3** and are designed to be lightweight, transparent, and auditable. No specialized hardware is required.

**Dependencies:**
```bash
pip install numpy scipy

python teu_unified_gauge_mass.py

VERIFICATION RUN LOG (2026-02-23)
------------------------------------------------
Executed script: teu_g2_anomaly_solver.py
Method: Topological integration vs QED Perturbation

RESULTS:
> Standard Model g-factor: 2.002319304351
> TEU Model g-factor:      2.002319304561

> Delta (g-2):             2.0954e-10

CONCLUSION:
The TEU geometric ansatz reproduces the QED coefficients 
(Schwinger, Sommese, Laporta, Kinoshita) with a precision 
of 10^-10 without employing Feynman diagrams.

his code complements the formal research manuscript.
If you use this code or the TEU model in your research, please cite the official Preprint on Zenodo:
Marín Casado, M. J. (2026). Application of $F^\alpha$-Calculus to the Anomalous Magnetic Moment of the Electron:
A Topological Derivation of QED Coefficients. Zenodo. [Add DOI here when available]Author: M. J. Marín Casado (Independent Researcher)
Contact: mariano.marin.casado@gmail.com
License: MIT License
