A basic library that demonstrates "Shelly Era" Icarus HD account derivation for Cardano Wallets from mnemonic all the way through to Bech32 addresses.

Pure Python... Doesn't require any external libraries to be installed or non-python code and supports derivation for Yoroi/Adalite/Daedalus/Atomic, (Not Exodus) Ledger and Trezor (Not Ellipal). (Including the special handling required for Trezor T devices with a 24 word seed) Should work with any system running Python 3.6+

Not an exhaustive implementation, only those functions required for [BTCRecover.](https://github.com/3rdIteration/btcrecover/)

All required modules are bundled and subject to their own licence terms.

Functions around found in cardano_utils.py and a demo implementation in test.py

You can perform address derivation based on some bundled test vectors with the command:

`python test.py`
