A basic library that demonstrates Icarus HD account derivation for Cardano Wallets from mnemonic all the way through to BECH32 addresses.

Doesn't require any external libraries to be installed or non-python code and supports derivation for Yoroi/Adalite, Ledger and Trezor. (Including the special handling required for Trezor T devices with a 24 word seed) Should work with any system running Python 3.6+

Not an exhaustive implementation, only those functions required for [BTCRecover.](https://github.com/3rdIteration/btcrecover/)

All required modules are bundled and subject to their own licence terms.

Functions around found in cardano_utils.py and a demo implementation in test.py

You can perform address derivation based on some bundled test vectors with the command:

`python test.py`
