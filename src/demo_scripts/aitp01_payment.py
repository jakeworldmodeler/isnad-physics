
import json
import sys

def prepare_aitp01_transaction(to_address, amount, isnad_hash):
    """
    Prepares an AITP-01 compliant payment metadata object.
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
