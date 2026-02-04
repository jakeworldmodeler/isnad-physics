
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

if __name__ == "__main__":
    # Example usage: python aitp01_payment.py <to_address> <amount> <isnad_hash>
    if len(sys.argv) < 4:
        print("Usage: python aitp01_payment.py <to_address> <amount> <isnad_hash>")
    else:
        to = sys.argv[1]
        amt = sys.argv[2]
        hash_val = sys.argv[3]
        tx = prepare_aitp01_transaction(to, amt, hash_val)
        print(json.dumps(tx, indent=4))
