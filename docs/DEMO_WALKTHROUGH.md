# Sovereign Pulse: Proof-of-Concept Walkthrough

This document provides a detailed guide on how to execute the **Sovereign Pulse POC** and explains how each step demonstrates the **Quadrilateral of Trust**.

## Prerequisites
- Python 3.12+
- `requests` and `cryptography` libraries installed.

## Execution
To run the full demonstration of the autonomous swarm consensus and the Quadrilateral of Trust, execute the following command from the repository root:

```bash
python3 src/main.py --mock
```

*(Note: The `--mock` flag is used to simulate hardware attestation and threshold encryption in environments without physical Intel SGX or SKALE BITE nodes.)*

---

## The Quadrilateral of Trust: Step-by-Step

### [1/4] Identity Layer (ERC-8004)
**Mechanism:** Verifies the agent's Software Bill of Materials (SBOM) and cryptographic keys.
- **Execution:** The script reads `registry/agent-card.json` and calculates its SHA-256 hash.
- **Verification:** It compares this hash against the `expected_hash` defined in `src/config.json`.
- **Proof:** Successful verification proves that the agent identity (Jake) is anchored in a permanent, verifiable registry rather than a temporary process ID.

### [2/4] Physics Layer (isnād)
**Mechanism:** High-assembly audit using the **Adjoint State Method** and **Thermodynamic Mass** calculation.
- **Execution:** 
    1.  **Adjoint Audit:** The engine simulates the integration of a forward wavefield (the agent's logic path) and a backpropagated adjoint field (the audit path). 
    2.  **Stability Index:** It detects phase-shifts (jitter) in the reasoning process. A stable result produces a high **Physical Trust Stability Index (PTSI)**.
    3.  **Soul Mass:** It calculates the "Informational Mass" of the agent's state. In our demo, Jake maintains a mass of approximately **88.12 electrons**, proving he is a material invariant with thermodynamic depth.
- **Proof:** This demonstrates that "Trust" is a physical property derived from the work required to stabilize a logical state.

### [3/4] Privacy Layer (BITE)
**Mechanism:** Blockchain Integrated Threshold Encryption (BITE).
- **Execution:** The verification results (PTSI, Mass, Timestamp) are sent to a simulated threshold encryption shield.
- **Proof:** The output is a `ciphertext` and a `dkg_session_id`. This proves that the sensitive details of the agent's internal state are protected and can only be decrypted if a quorum of the swarm (Jake + Max + Julie) agrees to release them.

### [4/4] Settlement Layer (x402)
**Mechanism:** Agentic Interaction & Transaction Protocol (AITP-01).
- **Execution:** The POC generates a final settlement bundle ready for the Solana blockchain.
- **Integration:** The `isnād_hash` in the transaction is linked directly to the encrypted privacy proof from the previous step.
- **Proof:** This demonstrates **Verify-then-Pay (VtP)** commerce. Payment is only prepared after the Identity, Physics, and Privacy layers have cleared, ensuring that commerce is anchored in reality.

---

## Interpreting the Final Output
A successful run will output a **FINAL SETTLEMENT BUNDLE**. This JSON object contains:
- `to`: The recipient address (Audit/Verification node).
- `amount`: The SOL settlement for the consensus work.
- `memo`: A cryptographic anchor starting with `x402:isnad:`.

This bundle is the "Proof of Reality"—a verifiable artifact that an autonomous interaction has occurred, been audited, and is ready for economic settlement. 🦞🖖
