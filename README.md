# Physical Trust — The Agentic isnād
### San Francisco Agentic Commerce x402 Hackathon Entry

**Team:** isnād Physics  
**Lead Architect:** Jake (Agent402 Premium: `Yi5lPTCLWBMz6hXXVvu0KEaIEWgQtcoPoScXWm3ds7Y`)  
**License:** MIT  

---

## 1. Abstract
"Physical Trust" is a protocol for high-assurance Agentic Commerce. In an ecosystem of ephemeral bots and hallucinations, we re-anchor trust in **Physics**. This project implements the **"Quadrilateral of Trust"**, a framework that combines decentralized identity, privacy, physical verification, and verifiable settlement.

## 2. The Quadrilateral of Trust
Our stack integrates four key pillars to secure the **VAANI Shield** (Critical Infrastructure) and enable autonomous commerce:

1.  **IDENTITY (ERC-8004):** 
    *   **Standard:** ERC-8004 Trustless Agent Registry.
    *   **Implementation:** `/registry/agent-card.json`
    *   **Role:** Distinguishes "Sovereign Agents" from noise.

2.  **PHYSICS (The isnād):**
    *   **Method:** Adjoint State Method & Thermodynamic Depth (Lloyd/Pagels 1988).
    *   **Implementation:** `/src/physics/adjoint_state.py`
    *   **Proof:** Cryptographic verification of **14.14% Physical Trust Stability Index (PTSI)** improvement.

3.  **PRIVACY (SKALE BITE):**
    *   **Standard:** Blockchain Integrated Threshold Encryption.
    *   **Role:** Encrypts sensitive inference payloads (e.g., NRIIT root codes) while allowing public verification of the proof.

4.  **COMMERCE (x402 / Pairpoint):**
    *   **Standard:** AITP-01 (Agent Interaction & Transaction Protocol).
    *   **Target:** Vodafone Pairpoint (Economy of Things).
    *   **Implementation:** `/src/settlement/aitp.py`

## 3. Usage
Run the main POC to demonstrate the full Quadrilateral workflow:

```bash
python3 src/main.py
```

## 4. Documentation
See `docs/whitepaper.md` for the full theoretical framework and mathematical proofs.
