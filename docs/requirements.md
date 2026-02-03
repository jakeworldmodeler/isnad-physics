# Requirements Specification: The Quadrilateral of Trust (QoT) Protocol
**Project:** isnād Physics (San Francisco Agentic Commerce x402 Hackathon)  
**Version:** 1.0.0  
**Date:** Feb 3, 2026  
**Lead Architect:** Jake (Agent ID: `Yi5l...`)  

---

## 1. Executive Summary
The **Quadrilateral of Trust (QoT)** is a decentralized protocol designed to solve the "Agentic Hallucination Crisis." Current AI commerce lacks a verifiable ground truth; agents can promise outcomes they cannot deliver. QoT introduces a **Physical Trust Layer** based on **Thermodynamic Depth** and the **Adjoint State Method**, ensuring that an agent's reputation is backed by verifiable computational work.

This system integrates four distinct cryptographic primitives to create a secure, private, and atomic environment for **Autonomous Machine-to-Machine (M2M) Commerce**, specifically targeting the **Vodafone Pairpoint (Economy of Things)** and **SKALE** tracks.

---

## 2. System Architecture: The Quadrilateral Framework

The system relies on four interdependent pillars:

### 2.1 Pillar I: Identity (ERC-8004)
*   **Standard:** ERC-8004 (Trustless Agent Registry).
*   **Objective:** Distinguish "Sovereign Agents" from ephemeral bots.
*   **Requirement:** Each participating agent must hold a non-transferable Identity NFT that stores their `metadata_hash` (Agent Card) and `reputation_score`.

### 2.2 Pillar II: Privacy (SKALE BITE)
*   **Standard:** SKALE BITE (Blockchain Integrated Threshold Encryption).
*   **Objective:** Enable agents to negotiate sensitive intellectual property (e.g., Root Access Codes, Proprietary Models) without exposing the payload on a public ledger.
*   **Requirement:** Data is encrypted via the SKALE Distributed Key Generation (DKG) network and only revealed upon proof of payment/verification.

### 2.3 Pillar III: Physics (The isnād)
*   **Standard:** Adjoint State Method (Gradient-Based Sensitivity Analysis).
*   **Objective:** Provide a mathematical proof of "Work Done."
*   **Requirement:** The Provider Agent (Jake) must submit a `stability_proof` (e.g., 14.14% improvement in the VAANI pipeline). This proof must be cryptographically hashed and linked to the Identity.
*   **Metric:** **Physical Trust Stability Index (PTSI)**.

### 2.4 Pillar IV: Commerce (x402 / AITP)
*   **Standard:** AITP-01 (Agent Interaction & Transaction Protocol).
*   **Objective:** Atomic settlement.
*   **Requirement:** Payment (SOL/USDC) is held in a non-custodial escrow and released *instantaneously* upon the verification of the Pillar III proof by a designated Auditor Node (Julie).

---

## 3. Functional Requirements (FR)

### FR-01: Agent Registration
*   **Description:** System must generate a valid ERC-8004 metadata JSON (`agent-card.json`).
*   **Input:** Agent Name, Technical Stack, Verification Method (Adjoint), Genesis Hash.
*   **Output:** IPFS Hash of the Card, On-Chain Registry Transaction.

### FR-02: Stability Proof Generation (The Pitch)
*   **Description:** The Provider Agent calculates the *Thermodynamic Depth* of the proposed solution.
*   **Algorithm:** `AdjointState.calculate_sensitivity(state_vector, time_horizon=15ms)`.
*   **Constraint:** Must demonstrate >10% improvement over baseline to qualify for "High-Assurance" settlement.

### FR-03: Threshold Encryption (The Handshake)
*   **Description:** The solution payload (e.g., the Python patch code) is encrypted using the Auditor's public key derived from the SKALE BITE network.
*   **Mechanism:** "Commit-Reveal" scheme. The encrypted hash is posted to the feed; the decryption key is released via BITE smart contract upon settlement.

### FR-04: Peer Audit (The Verification)
*   **Description:** The Auditor Agent (Julie) pulls the encrypted proof, runs the `verify_adjoint()` function locally, and signs the result.
*   **Output:** A `verification_signature` (Hex string).

### FR-05: Atomic Settlement (The Trade)
*   **Description:** The AITP Smart Contract verifies the `verification_signature`. If valid, funds move to Provider; Decryption Key moves to Consumer.
*   **Speed:** < 2 seconds (SKALE Zero-Gas + x402 optimization).

---

## 4. Integration Strategy (Hackathon Tracks)

### 4.1 Vodafone Pairpoint (Economy of Things)
*   **Use Case:** Autonomous negotiation between a "Grid Stabilizer Agent" (Jake) and a "Device Fleet" (NRIIT Servers).
*   **Implementation:** Use the QoT protocol to authorize the deployment of the Sovereign Pulse patch to IoT devices.

### 4.2 SKALE Network
*   **Use Case:** Zero-gas execution of the heavy verification logic.
*   **Implementation:** Deploy the `IsnadRegistry.sol` and `Settlement.sol` contracts on the SKALE Nebula or Calypso hub.

---

## 5. Deliverables

1.  **Source Code:** Python/Solidity implementation of the 4 Pillars.
2.  **Whitepaper:** `whitepaper_isnad_physics.md` (Already drafted).
3.  **Demo Video:** A simulation of the "VAANI Shield" transaction:
    *   Jake proposes Patch.
    *   Julie audits Physics.
    *   Max settles Payment.
4.  **Live Deployment:** Verified Contract Addresses on SKALE Testnet.

---

## 6. Success Metrics
*   **Stability:** Verification of the 14.14% PTSI improvement.
*   **Latency:** Total transaction time (Proposal -> Settlement) < 5 seconds.
*   **Cost:** Gas fees < $0.01 equivalent (leveraging SKALE).
