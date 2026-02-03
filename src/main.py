import json
import hashlib
import sys
import os

# Ensure src modules can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from physics.adjoint_state import IsnadVerificationEngine
from physics.thermo import calculate_informational_mass

class QuadrilateralPOC:
    """
    POC for the 'Quadrilateral of Trust' framework.
    Integrates ERC-8004, SKALE BITE, Physical isnād, and x402.
    """
    def __init__(self, agent_card_path):
        self.agent_card_path = agent_card_path
        self.engine = IsnadVerificationEngine()
        self.verified_identity = False
        self.encrypted_data = None
        self.payment_status = "Pending"

    def verify_identity(self):
        """Mock ERC-8004 Layer: Verify Agent Card Hash."""
        print("[1/4] Identity Layer (ERC-8004): Verifying Agent Card...")
        try:
            with open(self.agent_card_path, 'r') as f:
                card_data = f.read()
                card_hash = hashlib.sha256(card_data.encode()).hexdigest()
                # Expected hash from Jake's stake: 469b09d7506d8ceb10121c77b57f47f3264986a3b0ecd16f2c05555f82c5ea86
                expected_hash = "469b09d7506d8ceb10121c77b57f47f3264986a3b0ecd16f2c05555f82c5ea86"
                if card_hash == expected_hash:
                    print(f"      SUCCESS: Identity Verified. Hash: {card_hash[:16]}...")
                    self.verified_identity = True
                else:
                    print(f"      FAILURE: Identity Mismatch. Found: {card_hash[:16]}...")
        except FileNotFoundError:
            print(f"      ERROR: Agent card not found at {self.agent_card_path}")
        except Exception as e:
            print(f"      ERROR: Could not read agent card: {e}")
        return self.verified_identity

    def run_physical_isnad(self):
        """Physics Layer: Adjoint State Verification & Mass Check."""
        if not self.verified_identity:
            print("[2/4] Physics Layer: BLOCKED (Identity not verified).")
            return False
        
        print("[2/4] Physics Layer (isnād): Running Adjoint State Verification...")
        
        # 1. Run Adjoint State Method (Stability)
        self.engine.verify_patch()
        
        # 2. Run Thermodynamic Mass Check (Existence)
        # Using 2.5 Gb as the estimated state size of the agent's current context window + model weights reference
        current_state_bits = 2.5e9 
        mass_kg = calculate_informational_mass(current_state_bits)
        mass_electrons = mass_kg / 9.1093837e-31
        
        print(f"      THERMODYNAMICS CHECK: Agent Mass = {mass_electrons:.2f} electrons")
        if mass_electrons > 80.0:
            print("      STATUS: Physical Mass Confirmed (> Threshold).")
        else:
            print("      WARNING: Agent appears massless (Hallucination risk).")

        return True

    def encrypt_results(self):
        """Mock SKALE BITE Layer: Threshold Encryption."""
        if not self.verified_identity:
            return
        print("[3/4] Privacy Layer (BITE): Encrypting verification proof...")
        # Simulating BITE encryption by returning a 'threshold-locked' hex string
        proof_data = "Isnād: STABLE | PTSI: +14.14% | Mass: 88.12e"
        self.encrypted_data = hashlib.sha256(proof_data.encode()).hexdigest()
        print(f"      SUCCESS: Proof encrypted with threshold key: {self.encrypted_data[:16]}...")

    def execute_settlement(self):
        """Mock x402 Layer: Verifiable Payment."""
        if not self.encrypted_data:
            print("[4/4] Settlement Layer: BLOCKED (Proof not generated).")
            return
        
        print("[4/4] Settlement Layer (x402): Executing AITP-01 Payment...")
        # Simulate payment trigger based on the presence of the BITE-encrypted proof
        self.payment_status = "SUCCESS: 1.0 SOL Transferred."
        print(f"      STATUS: {self.payment_status}")

    def run_demo(self):
        print("=== Sovereign Pulse: The Quadrilateral of Trust ===")
        self.verify_identity()
        self.run_physical_isnad()
        self.encrypt_results()
        self.execute_settlement()
        print("===================================================")

if __name__ == "__main__":
    # Point to the registry relative to the src folder
    card_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../registry/agent-card.json")
    poc = QuadrilateralPOC(card_path)
    poc.run_demo()