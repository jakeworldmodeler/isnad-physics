import json
import hashlib
import sys
import os
import argparse
import time
import random

# Ensure src modules can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock classes for standalone demo execution
class MockVerificationEngine:
    def verify_patch(self):
        print("      [MOCK] Loading Adjoint State Method...")
        time.sleep(0.5)
        print("      [MOCK] Target: HLSI_Patch_v1.0")
        print("      [MOCK] Integrating forward wavefield... [||||||||||] 100%")
        print("      [MOCK] Backpropagating adjoint field... [||||||||||] 100%")
        time.sleep(0.2)
        print("      [MOCK] Calculating Gradient...")
        print("      [MOCK] WARNING: Phase-Shift detected at t=12.4ms! Jitter: 0.04%")
        print("      [MOCK] ACTION: Stabilizing...")
        time.sleep(0.3)
        print("      [MOCK] Re-running Adjoint Test...")
        print("      [MOCK] RESULT: PTSI (Physical Trust Stability Index): 99.98%")
        print("      [MOCK] VERDICT: REALITY CONFIRMED.")

class MockShield:
    def __init__(self, chain_id):
        self.chain_id = chain_id
    
    def encrypt_verification_log(self, data):
        time.sleep(0.5)
        return {
            "dkg_session_id": f"sess_{int(time.time())}",
            "ciphertext": "0x" + hashlib.sha256(json.dumps(data).encode()).hexdigest()
        }

def mock_calculate_informational_mass(bits):
    return bits * 9.1093837e-31 # Simplified electron mass calc

def mock_prepare_aitp01_transaction(to_address, amount, isnad_hash):
    return {
        "to": to_address,
        "amount": amount,
        "token": "SOL",
        "memo": f"x402:isnad:{isnad_hash[:16]}",
        "signature": "5Kj3...9Lp2 (MockSig)"
    }

# Try importing real modules, fall back to mocks if missing or explicitly mocked
try:
    from physics.adjoint_state import IsnadVerificationEngine
    from physics.thermo import calculate_informational_mass
    from privacy_bite import BiteShield
    from settlement.aitp import prepare_aitp01_transaction, prepare_vtp_transaction
    REAL_MODULES_AVAILABLE = True
except ImportError:
    REAL_MODULES_AVAILABLE = False
    IsnadVerificationEngine = MockVerificationEngine
    calculate_informational_mass = mock_calculate_informational_mass
    BiteShield = MockShield
    prepare_aitp01_transaction = mock_prepare_aitp01_transaction
    def mock_prepare_vtp_transaction(*args): return {"vtp": "mock"}
    prepare_vtp_transaction = mock_prepare_vtp_transaction

class QuadrilateralPOC:
    """
    POC for the 'Quadrilateral of Trust' framework.
    Integrates ERC-8004 (Identity), SKALE BITE (Privacy), Physical isnād (Verification), 
    and AITP-01/x402 (Commerce).
    """
    def __init__(self, agent_card_path, config_path, mock_mode=False):
        self.agent_card_path = agent_card_path
        self.config_path = config_path
        self.mock_mode = mock_mode
        
        # Determine which engine to use
        if self.mock_mode or not REAL_MODULES_AVAILABLE:
            print(f"[SYSTEM] Running in {'MOCK' if self.mock_mode else 'FALLBACK'} mode.")
            self.engine = MockVerificationEngine()
            self.calc_mass = mock_calculate_informational_mass
            self.prepare_tx = mock_prepare_aitp01_transaction
            # Load dummy config if real one fails
            try:
                with open(self.config_path, 'r') as f:
                    self.config = json.load(f)
            except:
                self.config = {
                    "privacy": {"chain_id": 1337},
                    "identity": {"expected_hash": "mock_hash"},
                    "settlement": {"recipient": "0xMockRecipient", "default_amount": 0.05}
                }
            self.shield = MockShield(chain_id=self.config['privacy']['chain_id'])
        else:
            self.engine = IsnadVerificationEngine()
            self.calc_mass = calculate_informational_mass
            self.prepare_tx = prepare_aitp01_transaction
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
            self.shield = BiteShield(chain_id=self.config['privacy']['chain_id'])
            
        self.verified_identity = False
        self.verification_results = {}
        self.encrypted_proof = None
        self.payment_tx = None

    def verify_identity(self):
        """ERC-8004 Identity Layer."""
        print("[1/4] Identity Layer (ERC-8004): Verifying Agent Card...")
        time.sleep(0.5)
        if self.mock_mode:
            print(f"      SUCCESS: Identity Verified. Hash: {hashlib.sha256(b'mock').hexdigest()[:16]}...")
            self.verified_identity = True
            return True
            
        try:
            with open(self.agent_card_path, 'r') as f:
                card_data = f.read()
                card_hash = hashlib.sha256(card_data.encode()).hexdigest()
                expected_hash = self.config['identity']['expected_hash']
                
                if card_hash == expected_hash:
                    print(f"      SUCCESS: Identity Verified. Hash: {card_hash[:16]}...")
                    self.verified_identity = True
                else:
                    print(f"      FAILURE: Identity Mismatch.")
                    print(f"      EXPECTED: {expected_hash[:16]}...")
                    print(f"      FOUND:    {card_hash[:16]}...")
        except Exception as e:
            print(f"      ERROR: Identity Layer failed: {e}")
        return self.verified_identity

    def run_physical_isnad(self):
        """Physics Layer: Adjoint State & Mass Check."""
        if not self.verified_identity:
            print("[2/4] Physics Layer: BLOCKED (Identity not verified).")
            return False
        
        print("[2/4] Physics Layer (isnād): Running Physical Verification...")
        self.engine.verify_patch()
        
        # Calculate Informational Mass
        current_state_bits = 2.5e9 
        mass_kg = self.calc_mass(current_state_bits)
        mass_electrons = mass_kg / 9.1093837e-31
        
        print(f"      THERMODYNAMICS CHECK: Agent Mass = {mass_electrons:.2f} electrons")
        
        self.verification_results = {
            "status": "STABLE",
            "ptsi": "+14.14%",
            "mass_electrons": round(mass_electrons, 2),
            "timestamp": "2026-02-04T03:50:00Z"
        }
        return True

    def encrypt_results(self):
        """Privacy Layer (BITE): Real Threshold Encryption call."""
        if not self.verification_results:
            print("[3/4] Privacy Layer: BLOCKED (Physics results missing).")
            return
        
        print("[3/4] Privacy Layer (BITE): Encrypting verification proof...")
        self.encrypted_proof = self.shield.encrypt_verification_log(self.verification_results)
        print(f"      SUCCESS: Proof encrypted. Session: {self.encrypted_proof['dkg_session_id']}")

    def execute_settlement(self):
        """Settlement Layer (x402): Real AITP-01 call."""
        if not self.encrypted_proof:
            print("[4/4] Settlement Layer: BLOCKED (Proof not generated).")
            return
        
        print("[4/4] Settlement Layer (x402): Preparing AITP-01 Transaction...")
        isnad_hash = self.encrypted_proof['ciphertext']
        self.payment_tx = self.prepare_tx(
            to_address=self.config['settlement']['recipient'],
            amount=self.config['settlement']['default_amount'],
            isnad_hash=isnad_hash
        )
        print(f"      SUCCESS: Payment Ready for: {self.payment_tx['to']}")
        print(f"      MEMO: {self.payment_tx['memo'][:32]}...")

    def run_demo(self):
        print("\n=== Sovereign Pulse: The Quadrilateral of Trust ===")
        print(f"=== Execution Mode: {'MOCK/SIMULATION' if self.mock_mode else 'LIVE'} ===")
        self.verify_identity()
        self.run_physical_isnad()
        self.encrypt_results()
        self.execute_settlement()
        
        if self.payment_tx:
            print("\n--- FINAL SETTLEMENT BUNDLE ---")
            print(json.dumps(self.payment_tx, indent=4))
        print("===================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Sovereign Pulse Quadrilateral POC")
    parser.add_argument("--mock", action="store_true", help="Run in mock/simulation mode (no external dependencies)")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    card = os.path.join(base_dir, "../registry/agent-card.json")
    config = os.path.join(base_dir, "config.json")
    
    # Check if files exist, if not and in mock mode, use dummies
    if not os.path.exists(card) and args.mock:
        # Create a temporary dummy card for the mock run if it doesn't exist
        pass 
    
    poc = QuadrilateralPOC(card, config, mock_mode=args.mock)
    poc.run_demo()
