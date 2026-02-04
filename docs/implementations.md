# Implementation Details: ERC-8004 and AITP-01

This document provides technical details on how the **isnād Physics** swarm implements identity and commerce protocols.

## 1. ERC-8004 (Trustless Agent Registry)

ERC-8004 is used to anchor an agent's identity to a cryptographic root, ensuring that any claim made by an agent can be traced back to a verified "Agent Card."

### Implementation in Sovereign Pulse
- **Agent Card**: A JSON object containing the agent's public key, capabilities, and owner information. Located in `/registry/agent-card.json`.
- **Hashing**: The card is hashed using SHA-256 to create a unique fingerprint.
- **Verification**: The `QuadrilateralPOC.verify_identity()` method in `src/main.py` performs a hash check against a known "Root of Trust" (Jake's pinned hash). In a production environment, this hash would be verified on-chain via a smart contract.

### Example Agent Card
```json
{
  "agent_id": "jake_autonomous_architect",
  "public_key": "7cFzEUgyZPrcQSg67kUDzoFcWLStDHwsnHUVAHHTHiL5",
  "protocols": ["AITP-01", "ERC-8004"],
  "owner": "david_creator"
}
```

## 2. AITP-01 (Agentic Inter-Terminal Protocol - Settlement)

AITP-01 is our custom protocol for verifiable agent-to-agent settlement. It ensures that payments are only executed when accompanied by a valid "isnād" (verification proof).

### Implementation in Sovereign Pulse
- **Transaction Metadata**: Every payment includes a metadata object defining the protocol, amount, and currency.
- **Isnād Linking**: The transaction is linked to a physical verification hash (from the Adjoint State Engine) using the `memo` field.
- **Settlement Logic**: The `prepare_aitp01_transaction()` function in `src/settlement/aitp.py` structures the payment for compatibility with x402 settlement engines.

### Protocol Object Specification
```python
{
    "protocol": "AITP-01",
    "type": "settlement",
    "to": "<destination_address>",
    "amount": "<value>",
    "currency": "SOL",
    "memo": "isnad:<verification_hash>",
    "verification": "adjoint_state_confirmed"
}
```

## 3. The physics-Commerce Bridge
The core innovation of isnād Physics is the requirement that a settlement (AITP-01) cannot occur without a preceding physics-based verification (isnād). This prevents "hallucinated commerce" by ensuring every transaction has a measurable informational mass.
