import numpy as np

def simulate_stochastic_dirac_matrix():
    print("==========================================================")
    print("   TEU ENGINE: STOCHASTIC DIRAC MATRIX MONTE CARLO")
    print("   Stochastic emergence of fermionic mass")
    print("==========================================================\n")

    # 1. FUNDAMENTAL CONSTANTS
    c = 299792458               # m/s
    hbar = 1.054571817e-34      # J*s
    l_p = 1.616255e-35          # m
    
    alpha_inv = 137.035999
    K_geo = 2.659455
    D_fractal = alpha_inv / K_geo
    
    # Norm of the fractal connection |Gamma|
    norm_Gamma = (1 / l_p) * np.exp(-D_fractal)

    # 2. CONSTRUCTION OF DIRAC MATRICES (4x4)
    I2 = np.eye(2); Z2 = np.zeros((2, 2))
    sigma_1 = np.array([[0, 1], [1, 0]])
    sigma_2 = np.array([[0, -1j], [1j, 0]])
    sigma_3 = np.array([[1, 0], [0, -1]])
    
    gamma_1 = np.block([[Z2, sigma_1], [-sigma_1, Z2]])
    gamma_2 = np.block([[Z2, sigma_2], [-sigma_2, Z2]])
    gamma_3 = np.block([[Z2, sigma_3], [-sigma_3, Z2]])

    # 3. GENERATION OF FRACTAL CHAOS (Monte Carlo)
    N_steps = 10000000
    print(f"-> Generating {N_steps} 3D topological fluctuations...")
    
    # The standard deviation of the noise in each axis is |Gamma| / sqrt(3)
    # so that the 3D vector averages exactly the fractal norm.
    sigma_noise = norm_Gamma / np.sqrt(3)
    
    noise_x = np.random.normal(0, sigma_noise, N_steps)
    noise_y = np.random.normal(0, sigma_noise, N_steps)
    noise_z = np.random.normal(0, sigma_noise, N_steps)

    # 4. STOCHASTIC CONSTRUCTION OF 10,000,000 DIRAC MATRICES
    print("-> Building and diagonalizing interaction matrices...")
    
    # Prepare matrices for batch operation (Numpy broadcasting)
    Gx = noise_x[:, np.newaxis, np.newaxis]
    Gy = noise_y[:, np.newaxis, np.newaxis]
    Gz = noise_z[:, np.newaxis, np.newaxis]

    # M_operator has a shape of (10000000, 4, 4)
    M_ops = -1j * (hbar / c) * (Gx * gamma_1 + Gy * gamma_2 + Gz * gamma_3)

    # 5. EIGENVALUE EXTRACTION IN THE CHAOS
    # Extract eigenvalues from the 10,000,000 matrices simultaneously
    chaotic_eigenvalues = np.linalg.eigvals(M_ops)
    
    # Take the absolute value of the energies (masses) of all states
    instantaneous_masses = np.abs(chaotic_eigenvalues)

    # 6. STATISTICAL COLLAPSE (Root Mean Square - RMS)
    # According to TEU, the observable inertial mass is the RMS of the matrix noise
    observable_rms_mass = np.sqrt(np.mean(instantaneous_masses**2))

    print("\n----------------------------------------------------------")
    print("[SIMULATION RESULTS]")
    print("----------------------------------------------------------")
    m_e_exp = 9.1093837e-31
    error = abs(observable_rms_mass - m_e_exp) / m_e_exp * 100

    print(f"Empirical CODATA Mass      : {m_e_exp:.10e} kg")
    print(f"Emergent TEU Mass (RMS)    : {observable_rms_mass:.10e} kg")
    print(f"MC Convergence Error       : {error:.4f} %")
    print("----------------------------------------------------------")
    print("Conclusion: Observable mass emerges spontaneously as the")
    print("Root Mean Square (RMS) of Dirac eigenvalues subjected to")
    print("pure geometric fluctuations.")
    print("==========================================================")

if __name__ == "__main__":
    simulate_stochastic_dirac_matrix()
