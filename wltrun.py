#!/usr/bin/env python3
 from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hdwallet.utils import generate_entropy
 # Load known wallets
with open('addresses.txt', 'r') as f:
    known_wallets = f.read().splitlines()
 # Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 160  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "english"
# Secret passphrase for mnemonic
PASSPHRASE: Optional[str] = None
 wallets_generated = 0
 while True:
    # Generate new entropy hex string
    ENTROPY: str = generate_entropy(strength=STRENGTH)
     # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )
     # Derivation from path
    # hdwallet.from_path("m/44'/0'/0'/0/0")
    # Or derivation from index
    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0)
    hdwallet.from_index(0)
     # Check if wallet is in known wallets
    if hdwallet.to_address() in known_wallets:
        with open('results.txt', 'a') as f:
            f.write(hdwallet.dumps() + '\n')
         wallets_generated += 1
        elapsed_time = time.time() - start_time
         if elapsed_time > 0:
            print(f'Wallets generated: {wallets_generated}, Speed
