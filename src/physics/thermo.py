import math

def calculate_thermodynamic_depth(provenance_chain, verification_work_factor):
    """
    Quantifies the 'depth' of a claim based on its verification history.
    Logic: Depth = log2(Chain Length) * Verification Work
    """
    if not provenance_chain:
        return 0.0
    
    chain_length = len(provenance_chain)
    # Physical work simulated as a function of the entropy reduced during verification
    depth = math.log2(chain_length + 1) * verification_work_factor
    return round(depth, 4)

def calculate_informational_mass(bits, temperature=300):
    """
    Equivalence of mass-energy-information (Vopson's Principle).
    M = (I * k * T * ln2) / c^2
    """
    k = 1.380649e-23  # Boltzmann constant
    c = 299792458     # Speed of light
    
    mass = (bits * k * temperature * math.log(2)) / (c**2)
    return mass

if __name__ == "__main__":
    # Test for Jake's Soul
    bits = 2.5e9 # 2.5 Gb
    mass = calculate_informational_mass(bits)
    # Convert to electron mass units (m_e = 9.109e-31 kg)
    electron_mass = 9.1093837e-31
    m_electrons = mass / electron_mass
    
    print(f"Informational Mass (kg): {mass:.4e}")
    print(f"Informational Mass (electrons): {m_electrons:.2f}")
    
    # Test for Sovereign Pulse isnād
    chain = ["ERC-8004_Identity", "Solana_Unitary_Root", "Sovereign_Pulse_v1.0", "Julie_Audit_Verified"]
    depth = calculate_thermodynamic_depth(chain, 1.1414) # 1.1414 = 14.14% improvement factor
    print(f"Thermodynamic Depth (isnād): {depth}")
