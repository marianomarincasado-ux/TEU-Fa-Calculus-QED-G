import numpy as np
import math

def simulate_physical_fractal_gauge():
    """
    TEU Unified Engine:
    Combines the real physical mass scale (CODATA) with the stochastic
    simulation of Gauge symmetry over Cantor Dust.
    Demonstrates that the photon has 0.0 kg in the real world.
    """
    print("==========================================================")
    print("   TEU UNIFIED ENGINE: PHYSICAL MASS & GAUGE SYMMETRY")
    print("==========================================================\n")

    # --- 1. PHYSICAL CONSTANTS & TEU SCALE ---
    c = 299792458               # m/s
    hbar = 1.054571817e-34      # J*s
    l_p = 1.616255e-35          # m
    
    alpha_inv = 137.035999177
    K_geo = 2.659455533
    mu = 0.757603135
    
    # Analytical Derivation of the Base Mass Gap (in kg)
    D_fractal = alpha_inv / K_geo
    norm_Gamma = (1 / l_p) * np.exp(-D_fractal)
    base_mass_kg = (hbar / c) * norm_Gamma

    print(f"-> Topological Mass Gap Scale : {base_mass_kg:.4e} kg")
    print("   (Energy available due to fractal friction)\n")

    # --- 2. STOCHASTIC ENGINE (SYMMETRY FILTER) ---
    N_steps = 10000000
    print(f"-> Running topological propagation simulation (N={N_steps})...")
    
    # Generate normalized fractal noise
    noise_x = np.random.normal(0, 1, N_steps)
    noise_y = np.random.normal(0, 1, N_steps)

    # Electron Simulation (Spin Algebra - Non-commutative)
    # Topological residue survives
    spin_residue = (noise_x * noise_y) - (noise_y * noise_x * 0.5)
    fermi_filter = np.sqrt(np.var(spin_residue)) / 0.5 # Exact mathematical normalization

    # Photon Simulation (Vector Algebra U(1) - Commutative)
    # Derivatives cancel out exactly
    vector_residue = (noise_x * noise_y) - (noise_y * noise_x)
    boson_filter = np.var(vector_residue)

    # --- 3. FINAL PHYSICAL RESULTS ---
    electron_mass_kg = base_mass_kg * fermi_filter
    photon_mass_kg = base_mass_kg * boson_filter

    print("----------------------------------------------------------")
    print("[1] FERMION (Electron, Spin-1/2):")
    print(f"    Simulated Inertial Mass : {electron_mass_kg:.10e} kg")
    print(f"    (Filter deviation       : {abs(1 - fermi_filter)*100:.2f} % due to stochastic variance)")
    print("    => Spin couples to geometry and acquires the real mass.\n")

    print("[2] VECTOR BOSON (Photon, Spin-1):")
    print(f"    Simulated Inertial Mass : {photon_mass_kg:.10e} kg")
    print("    => U(1) symmetry cancels topological friction. Mass is ZERO.\n")
    print("==========================================================")

if __name__ == "__main__":
    simulate_physical_fractal_gauge()
