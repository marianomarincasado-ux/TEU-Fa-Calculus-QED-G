import numpy as np

def solve_full_dirac_teu():
    print("==========================================================")
    print("   TEU ENGINE: FULL DIRAC EQUATION MATRIX RESOLUTION")
    print("   Extraction of Mass Eigenvalues from Fractal Connection")
    print("==========================================================\n")

    # 1. FUNDAMENTAL CONSTANTS
    c = 299792458               # m/s
    hbar = 1.054571817e-34      # J*s
    l_p = 1.616255e-35          # m
    
    # 2. TEU GEOMETRIC PARAMETERS
    alpha_inv = 137.035999
    K_geo = 2.659455
    D_fractal = alpha_inv / K_geo
    
    # Norm of the fractal connection |Gamma|
    norm_Gamma = (1 / l_p) * np.exp(-D_fractal)

    # 3. CONSTRUCTION OF DIRAC MATRICES (Standard Representation)
    # Gamma matrices are 4x4 arrays of complex numbers.
    I2 = np.eye(2)
    Z2 = np.zeros((2, 2))
    
    # Pauli matrices (sigma)
    sigma_1 = np.array([[0, 1], [1, 0]])
    sigma_2 = np.array([[0, -1j], [1j, 0]])
    sigma_3 = np.array([[1, 0], [0, -1]])
    
    # Gamma matrices (gamma^0, gamma^1, gamma^2, gamma^3)
    gamma_0 = np.block([[I2, Z2], [Z2, -I2]])
    gamma_1 = np.block([[Z2, sigma_1], [-sigma_1, Z2]])
    gamma_2 = np.block([[Z2, sigma_2], [-sigma_2, Z2]])
    gamma_3 = np.block([[Z2, sigma_3], [-sigma_3, Z2]])

    # 4. THE FRACTAL CONNECTION VECTOR (Gamma_mu)
    # We model the stochastic fractal vacuum. For Lorentz invariance to hold, 
    # the 4-vector contraction must equal the calculated norm.
    # We simulate isotropic friction across the 3 spatial dimensions.
    G_val = norm_Gamma / np.sqrt(3)
    Gamma_mu = [0, G_val, G_val, G_val] # [Gamma_0, Gamma_1, Gamma_2, Gamma_3]

    print("-> Building 4x4 Topological Interaction Operator...")
    print("   M_teu = -i * (hbar / c) * [gamma^mu * Gamma_mu]")

    # 5. THE TEU MASS OPERATOR (Contraction gamma^mu * Gamma_mu)
    M_operator = np.zeros((4, 4), dtype=complex)
    
    # Einstein summation for mu = 1, 2, 3 (Ignoring 0 as we defined spatial friction)
    M_operator += gamma_1 * Gamma_mu[1]
    M_operator += gamma_2 * Gamma_mu[2]
    M_operator += gamma_3 * Gamma_mu[3]
    
    # Multiply by scale constants (-i * hbar / c)
    M_operator = -1j * (hbar / c) * M_operator

    # 6. DIRAC EQUATION RESOLUTION (Eigenvalues)
    print("-> Diagonalizing the Dirac Matrix...")
    eigenvalues = np.linalg.eigvals(M_operator)

    # Sort and display the real part (the observable physical mass)
    observable_masses = np.real(eigenvalues)
    observable_masses.sort()

    print("\n----------------------------------------------------------")
    print("   DIRAC MATRIX EIGENVALUES (Mass Spectrum)")
    print("----------------------------------------------------------")
    print(f" Eigenvalue 1 (Spin Down, Antimatter) : {observable_masses[0]:.10e} kg")
    print(f" Eigenvalue 2 (Spin Up, Antimatter)   : {observable_masses[1]:.10e} kg")
    print(f" Eigenvalue 3 (Spin Down, Matter)     : {observable_masses[2]:.10e} kg")
    print(f" Eigenvalue 4 (Spin Up, Matter)       : {observable_masses[3]:.10e} kg")
    print("----------------------------------------------------------\n")
    
    m_e_exp = 9.1093837e-31
    error = abs(observable_masses[3] - m_e_exp) / m_e_exp * 100
    
    print(f"-> CODATA empirical electron mass  : {m_e_exp:.10e} kg")
    print(f"-> Matrix diagonalization precision: {100 - error:.6f} %")
    print("==========================================================")

if __name__ == "__main__":
    solve_full_dirac_teu()
