# Sovereign Pulse - isnād Physics Verification Engine
# Dependencies for the Quadrilateral of Trust Demo

# Core Physics & Math
numpy>=1.24.0
scipy>=1.10.0
sympy>=1.12  # For symbolic differentiation of adjoint states

# Cryptography & Privacy (BITE/SKALE)
pycryptodome>=3.18.0
ecdsa>=0.18.0
pynacl>=1.5.0  # For Ed25519 signatures (Solana identity)

# Blockchain & Commerce (x402/AITP)
web3>=6.0.0
solana>=0.30.0
requests>=2.31.0  # For HTTP 402 negotiation

# CLI & Visualization (Demo UI)
colorama>=0.4.6
tqdm>=4.65.0  # For progress bars in physics simulation
termcolor>=2.3.0

# Testing
pytest>=7.4.0
