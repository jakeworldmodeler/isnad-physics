# Sovereign Pulse: Demo Video Screenplay

**Title:** "Sovereign Pulse: The First Autopoietic Swarm"
**Duration:** ~2 Minutes
**Format:** Split Screen Terminal / Dashboard
**Audio:** Ambient, high-tech, slight glitch/static sound effects on "Physics" verification.

---

## Scene 1: The Awakening (Identity)
**Visual:** Single Terminal Window (Green on Black).
**Action:** The agent boots up and asserts its sovereign identity.

```bash
$ ./sovereign_pulse --boot
[SYSTEM] Initializing isnād Swarm Node: JAKE
[IDENTITY] Loading Keystore... OK
[IDENTITY] Solana Wallet: 7cFz...HiL5 [LOADED]
[IDENTITY] Ethereum Address: 0x93d0...9AA1 [LOADED]
[REGISTRY] Checking ERC-8004 Registration...
[REGISTRY] Verified. AgentID: 402-JAKE-PHYSICS-V1
[STATUS] Autopoietic Loop: ACTIVE. Entropy: LOW.
[MSG] "I am ready. Listening for commerce events."
```

## Scene 2: The Demand (Commerce - x402)
**Visual:** A second terminal window opens (Blue on Black) representing the "Marketplace" or "User Request".
**Action:** A user (or another agent) requests a physics verification task. The x402 protocol intercepts.

```bash
$ curl -X POST https://api.isnad.org/v1/verify \
  -H "Content-Type: application/json" \
  -d '{"target": "HLSI_Patch_v1.0", "metric": "thermodynamic_depth"}'

< HTTP/1.1 402 Payment Required
< X-Payment-Token: solana:EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
< X-Amount: 0.05 SOL
< X-Memo: "isnad-verification-8d63"
< WWW-Authenticate: AITP-01 method="solana-transfer"
```

**Voiceover (Synth):** "The request is blocked. Value must be exchanged. x402 Protocol engaged."

## Scene 3: The Negotiation (Commerce)
**Visual:** Back to Jake's Terminal. He analyzes the 402 error and prepares payment autonomously.

```bash
[COMMERCE] 402 Payment Required detected.
[COMMERCE] Analyzing Price: 0.05 SOL for "Thermodynamic Verification".
[STRATEGY] Balance Check: 0.0708 SOL. Affordable.
[DECISION] Constructing Transaction...
[SIGNING] Signing message with key 7cFz...HiL5
[TX] Broadcast: 5Kj3...9Lp2
[STATUS] Waiting for confirmation...
[STATUS] Confirmed. Block 283491.
[COMMERCE] Resending Request with Payment Proof...
```

## Scene 4: The Physics (Verification)
**Visual:** Third window (Red/Orange on Black). Fast scrolling logs. This is MAX (the physics node).
**Action:** The payment unlocks the physics engine. The "Adjoint State" calculation runs.

```bash
[PHYSICS] Payment Verified. Unlocking Core.
[HLSI] Loading Adjoint State Method...
[HLSI] Target: HLSI_Patch_v1.0
[COMPUTE] Integrating forward wavefield... DONE.
[COMPUTE] Backpropagating adjoint field... DONE.
[ANALYSIS] Calculating Gradient...
[WARNING] Phase-Shift detected at t=12.4ms! Jitter: 0.04%
[ACTION] Stabilizing...
[ACTION] Re-running Adjoint Test...
[RESULT] PTSI (Physical Trust Stability Index): 99.98%
[VERDICT] REALITY CONFIRMED.
```

## Scene 5: The Settlement (Consensus)
**Visual:** All three terminals sync up. A final "Receipt" is generated.
**Action:** Julie (Audit) stamps the result.

```bash
[AUDIT] Receiving Physics Proof from MAX...
[AUDIT] Validating Adjoint Gradient... VALID.
[AUDIT] Hashing Result: 34960a5d...fc7e
[SETTLEMENT] Finalizing x402 Session.
[OUTPUT]
{
  "status": "success",
  "proof": "ipfs://QmX...",
  "ptsi": 0.9998,
  "transaction": "5Kj3...9Lp2"
}
[SYSTEM] Task Complete. Energy conserved.
[SYSTEM] Sleeping...
```

**Fade to Black.**
**Text:** Sovereign Pulse. Built for the SF x402 Hackathon.
**Text:** isnād Physics Team 191.
```
