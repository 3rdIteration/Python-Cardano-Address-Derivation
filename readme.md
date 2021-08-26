A basic library that demonstrates Icarus HD account derivation for Cardano Wallets as per CIP-003. 

Doesn't require any external libraries to be installed or non-python code and supports derivation for Yoroi/Adalite, Ledger and Trezor.

Not an exhaustive implementation, only those functions required for BTCRecover.

All required modules are bundled and subject to their own licence terms.

Functions around found in cardano_utils.py and a demo implementation in test.py

You can perform address derivation based on some bundled test vectors with the command:

`python test.py`