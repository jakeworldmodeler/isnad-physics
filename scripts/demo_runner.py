
import sys
import os
import time

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from main import QuadrilateralPOC

def run_isnad_demo():
    print("\n" + "="*50)
    print("  ISNĀD PHYSICS: SOVEREIGN PULSE DEMO (v1.0)")
    print("="*50)
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    card_path = os.path.join(os.path.dirname(__file__), "../registry/agent-card.json")
    config_path = os.path.join(os.path.dirname(__file__), "../src/config.json")
    poc = QuadrilateralPOC(card_path, config_path, mock_mode=True)
    
    steps = [
        ("Identity Verification", poc.verify_identity),
        ("Physics Verification", poc.run_physical_isnad),
        ("Privacy Encryption", poc.encrypt_results),
        ("Verifiable Settlement", poc.execute_settlement)
    ]
    
    for name, func in steps:
        print(f"\n[RUNNING] {name}...")
        time.sleep(1) # Simulation delay
        func()
        
    print("\n" + "="*50)
    print("  DEMO COMPLETE: AGENT IS STABLE AND VERIFIED")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_isnad_demo()
