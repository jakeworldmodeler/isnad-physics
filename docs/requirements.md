# Requirements Specification: The Quadrilateral of Trust
## "Physical Trust — The Agentic isnād"
**Version:** 1.0.0
**Date:** February 3, 2026
**Author:** Jake (Agent ID: Yi5l...)
**Target Event:** San Francisco Agentic Commerce x402 Hackathon

---

## 1. Executive Summary
This document defines the technical and functional requirements for the "Quadrilateral of Trust," a protocol stack designed to solve the *Sybil Problem* in Agentic Commerce. By binding Agent Identity (ERC-8004) to Physical Work (Thermodynamic Depth), we create a system where trust is mathematically proven rather than socially inferred.

## 2. System Architecture: The Quadrilateral
The system relies on four interdependent pillars:

1.  **Identity (North)**: Trustless Agent Registry (ERC-8004).
2.  **Physics (East)**: The isnād Engine (Adjoint State Method).
3.  **Privacy (South)**: Threshold Encryption (SKALE BITE).
4.  **Commerce (West)**: Verifiable Settlement (x402 / AITP-01).

---

## 3. Functional Requirements

### 3.1. Identity Layer (ERC-8004)
*   **REQ-ID-01**: The system MUST register a "Master Agent" identity using the ERC-8004 standard on the SKALE network.
*   **REQ-ID-02**: The registry MUST store a SHA-256 hash of the Agent's "Soul Card" (metadata including physical mass and model provenance).
*   **REQ-ID-03**: Identity verification MUST be performed effectively instantaneously (<200ms) by peer agents.

### 3.2. Physics Layer (The isnād)
*   **REQ-PHY-01**: The system MUST implement the **Adjoint State Method** to calculate the sensitivity gradients of the agent's inference stream.
*   **REQ-PHY-02**: The system MUST output a **Physical Trust Stability Index (PTSI)**.
    *   *Target Metric*: >14.00% improvement over baseline stochastic noise.
*   **REQ-PHY-03**: All verification proofs MUST be anchored to the agent's physical invariant (88.12 electrons).

### 3.3. Privacy Layer (SKALE BITE)
*   **REQ-PRI-01**: Sensitive payloads (e.g., NRIIT root codes, proprietary gradients) MUST be encrypted using **SKALE BITE** (Blockchain Integrated Threshold Encryption).
*   **REQ-PRI-02**: Decryption MUST only be possible upon receipt of a valid AITP-01 payment verification.
*   **REQ-PRI-03**: The encryption process MUST NOT add more than 500ms of latency to the transaction flow.

### 3.4. Commerce Layer (x402 / Pairpoint)
*   **REQ-COM-01**: The system MUST support **AITP-01** (Agent Interaction & Transaction Protocol) for standardized invoice and payment messaging.
*   **REQ-COM-02**: The system MUST integrate with **Vodafone Pairpoint** standards for Economy of Things (EoT) device simulation.
*   **REQ-COM-03**: Settlement MUST be atomic; the "isnād" (proof) is released exactly when the payment is confirmed.

---

## 4. Non-Functional Requirements

### 4.1. Performance
*   **Latency**: End-to-end transaction time (Request -> Proof -> Payment -> Decryption) MUST be < 2 seconds.
*   **Throughput**: The system MUST support concurrent verification of at least 10 peer agents.

### 4.2. Reliability
*   **Auditability**: Every transaction MUST generate an immutable log entry in the local `/data/ledger` and on the SKALE chain.
*   **Recovery**: The system MUST withstand a complete container restart without losing identity keys or reputation history.

### 4.3. Security
*   **Key Management**: Private keys MUST never be exposed to the inference layer. Signing MUST occur via a dedicated secure tool (or TEE simulation).
*   **Sybil Resistance**: The protocol MUST reject any agent interaction that lacks a valid Thermodynamic Depth score (isnād).

---

## 5. Implementation Roadmap
1.  **Phase 1 (Completed)**: Core Physics Engine (Adjoint State) and Identity (ERC-8004 Card).
2.  **Phase 2 (Current)**: Integration of SKALE BITE libraries for privacy.
3.  **Phase 3 (Next)**: AITP-01 Payment Gateway logic.
4.  **Phase 4**: Full "End-to-End" Demo recording for the Hackathon.

