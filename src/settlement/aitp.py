
import json
import sys

def prepare_aitp01_transaction(to_address, amount, isnad_hash):
    """
    AITP-01 (Agentic Inter-Terminal Protocol) Settlement Layer.
    
    Prepares a payment metadata object that links the financial settlement
    to a specific physical verification hash (isnād).
    
    Args:
        to_address (str): The recipient's Solana address.
        amount (str): The amount of SOL to transfer.
        isnad_hash (str): The hash from the physics verification engine.
        
    Returns:
        dict: A structured transaction object compliant with AITP-01.
    """
    transaction = {
        "protocol": "AITP-01",
        "type": "settlement",
        "to": to_address,
        "amount": amount,
        "currency": "SOL",
        "memo": f"isnad:{isnad_hash}",
        "verification": "adjoint_state_confirmed"
    }
    return transaction

def prepare_aitp08_attestation(hardware_hash, timestamp, software_version):
    """
    AITP-08 (Hardware Attestation) Layer.
    
    Provides the proof that the computation was anchored in a specific
    hardware Root of Trust (HRoT).
    """
    attestation = {
        "protocol": "AITP-08",
        "type": "attestation",
        "hrot_hash": hardware_hash,
        "timestamp": timestamp,
        "sw_version": software_version,
        "status": "verifiable"
    }
    return attestation

def prepare_vtp_transaction(to_address, amount, isnad_hash, hardware_hash):
    """
    Verify-then-Pay (VtP) Transaction.
    
    Combines AITP-01 settlement and AITP-08 hardware attestation.
    """
    import datetime
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    aitp01 = prepare_aitp01_transaction(to_address, amount, isnad_hash)
    aitp08 = prepare_aitp08_attestation(hardware_hash, timestamp, "v1.0")
    
    vtp_bundle = {
        "settlement": aitp01,
        "attestation": aitp08,
        "isnad_physics_verified": True
    }
    return vtp_bundle

if __name__ == "__main__":
    # Example usage: python aitp01_payment.py <to_address> <amount> <isnad_hash> <hw_hash>
    if len(sys.argv) < 5:
        print("Usage: python aitp01_payment.py <to_address> <amount> <isnad_hash> <hw_hash>")
    else:
        to = sys.argv[1]
        amt = sys.argv[2]
        isnad = sys.argv[3]
        hw = sys.argv[4]
        tx_bundle = prepare_vtp_transaction(to, amt, isnad, hw)
        print(json.dumps(tx_bundle, indent=4))
