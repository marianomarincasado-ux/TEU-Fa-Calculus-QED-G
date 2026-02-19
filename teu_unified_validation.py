import numpy as np

def validation_teu_unified():
    """
    TEU MODEL VALIDATION SCRIPT
    -----------------------------------
    Objective: Simultaneously calculate:
    1. The Rydberg Constant and the Lyman-Alpha line (Quantum Scale)
    2. The Gravitational Redshift in GPS satellites (Macroscopic Scale)
    
    Uses a single master equation based on the fractal density (D).
    """

    print("=== 1. FUNDAMENTAL CONSTANTS (CODATA 2022) ===")
    c = 299792458           # Speed of light (m/s)
    h = 6.62607015e-34      # Planck Constant (J s)
    hbar = h / (2 * np.pi)
    me = 9.10938356e-31     # Electron mass (kg)
    G = 6.67430e-11         # Gravitational Constant (N m^2/kg^2)
    
    # Earth Parameters
    M_earth = 5.972e24      # Earth Mass (kg)
    R_earth = 6371000       # Surface Radius (m)
    R_gps = 26560000        # GPS Orbit Radius (m)

    print("=== 2. TEU GEOMETRIC PARAMETERS (INPUTS) ===")
    # These values derive from the g-2 optimization (Section 4 of the paper)
    alpha_inv = 137.035999177
    K_geo = 2.659455533
    
    # Vacuum Fractal Depth (D)
    D_teu = alpha_inv / K_geo
    
    # Derived Planck Length (l_P)
    # l_P is the fundamental vacuum oscillation scale
    l_P = hbar / (me * c * np.exp(D_teu))
    
    print(f"Tortuosity (K_geo): {K_geo:.5f}")
    print(f"Fractal Depth (D): {D_teu:.5f}")
    print(f"TEU Planck Scale: {l_P:.3e} m")
    print("-" * 60)

    # =================================================================
    # PART A: MICRO-SCALE (HYDROGEN ATOM)
    # =================================================================
    print("\n[PART A] QUANTUM VALIDATION: LYMAN SERIES")
    
    # TEU Rydberg Formula (Eq. 9.1 of the Paper)
    # The atom acts as a geometric resonant filter
    R_teu = (1 / (4 * np.pi * l_P)) * (np.exp(-D_teu) / (D_teu * K_geo)**2)
    
    # Lyman-Alpha line calculation (Transition n=2 -> n=1)
    # 1/lambda = R * (1/1^2 - 1/2^2) = R * 0.75
    lambda_lyman = 1 / (R_teu * 0.75)
    
    print(f"Rydberg Constant (TEU): {R_teu:.5e} m^-1")
    print(f"Lyman-Alpha Line Prediction: {lambda_lyman * 1e9:.4f} nm")
    print(f"Experimental Value (Ref):    121.5670 nm")
    print(f"Model Accuracy:              {100*(1 - abs(121.567e-9 - lambda_lyman)/121.567e-9):.4f}%")

    # =================================================================
    # PART B: MACRO-SCALE (GPS SYSTEM)
    # =================================================================
    print("\n[PART B] RELATIVISTIC VALIDATION: GPS EFFECT")
    
    # TEU Hypothesis: Gravitational potential increases fractal density (D)
    # Delta_D = GM / (r c^2)
    delta_D_surf = (G * M_earth) / (R_earth * c**2)
    delta_D_orbit = (G * M_earth) / (R_gps * c**2)
    
    print(f"Vacuum Densification (Surface): +{delta_D_surf:.4e}")
    print(f"Vacuum Densification (GPS Orbit): +{delta_D_orbit:.4e}")
    
    # Time shift calculation (Clock advance in orbit)
    # Clocks on the surface run slower because the vacuum is denser.
    # Relative shift = D_surf - D_orbit
    relative_shift = delta_D_surf - delta_D_orbit
    
    # Convert to microseconds per day
    us_day = relative_shift * 86400 * 1e6
    
    print(f"Relative Shift (Z): {relative_shift:.4e}")
    print(f"GPS Clock Advance (TEU Prediction): {us_day:.2f} us/day")
    print(f"Einstein Prediction (General Rel.): 45.90 us/day")
    print(f"TEU vs GR Match: {100 * (1 - abs(45.9 - us_day)/45.9):.2f}%")

if __name__ == "__main__":
    validation_teu_unified()
