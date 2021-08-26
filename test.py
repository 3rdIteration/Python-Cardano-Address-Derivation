import hashlib
import cardano_utils as cardano
import bech32 as bech32
from mnemonic import Mnemonic

# Test Vectors (Name, derivation_type, seed, passphrase)
tests = [
    ("Adalite/Yoroi Test Seed",
    "Icarus",
    "cave table seven there praise limit fat decorate middle gold ten battle trigger luggage demand", #Custom seed generated in Adalite/Yoroi
    "")
    ,
    ("CIP003 Icarus Test Vector (No Passphrase)",
    "Icarus",
    "eight country switch draw meat scout mystery blade tip drift useless good keep usage title", #CIP003 - Icarus Test Vector
    "")
    ,
    ("CIP003 Icarus Test Vector (With Passphrase)",
    "Icarus",
    "eight country switch draw meat scout mystery blade tip drift useless good keep usage title", #CIP003 - Icarus Test Vector
    "foo")
    ,
    ("CIP003 Ledger Test Vector (No Iterations)",
    "ledger",
    "recall grace sport punch exhibit mad harbor stand obey short width stem awkward used stairs wool ugly trap season stove worth toward congress jaguar", #Ledger Test Vector no iterations
    "")
    ,
    ("CIP003 Ledger Test Vector (Iterations, No Passphrase)",
    "ledger",
    "correct cherry mammal bubble want mandate polar hazard crater better craft exotic choice fun tourist census gap lottery neglect address glow carry old business", #Ledger Test vector with iterations
    "")
    ,
    ("CIP003 Ledger Test Vector (Passphrase)",
    "ledger",
    "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art", #Ledger Test vector with iterations + passphrase
    "foo")
    ,
    ("Icarus 12 Word BIP39",
     "Icarus",
     "ocean hidden kidney famous rich season gloom husband spring convince attitude boy",
     "")
    ,
    ("Trezor/Atomic 12 Word", # Should be the same as the Icarus 12 word seed...
    "Icarus-Trezor",
    "ocean hidden kidney famous rich season gloom husband spring convince attitude boy",
    "")
    ,
    ("Trezor 24 Word BIP39",
     "Icarus-Trezor",
     "wood blame garbage one federal jaguar slogan movie thunder seed apology trigger spoon depth basket fine culture boil render special enforce dish middle antique",
     "")
]
print("==Testing Cardano Address Derivation==")
for description, mk_type, mnemonic, passphrase in tests:
    print("===================================================================")
    print("Description: ", description)
    print("Derivation Type: ", mk_type)
    print("Mnemonic: ", mnemonic)
    print("===================================================================")
    print()

    if mk_type == "Ledger":
        masterkey = cardano.generateHashKey_Ledger(mnemonic, passphrase.encode())

    if mk_type == "Icarus":
        mnemo = Mnemonic("english")
        masterkey = cardano.generateHashKey_Icarus(mnemonic=mnemonic, passphrase=passphrase.encode(),
                                                     wordlist=mnemo.wordlist, langcode="en",
                                                     trezor=False)

    if mk_type == "Icarus-Trezor":
        mnemo = Mnemonic("english")
        masterkey = cardano.generateHashKey_Icarus(mnemonic=mnemonic, passphrase=passphrase.encode(),
                                                     wordlist=mnemo.wordlist, langcode="en",
                                                     trezor=True)

    print("MasterKey: ", masterkey.hex())
    print()

    rootKey = cardano.generateRootKey_Icarus(masterkey)

    (kL, kR), AP ,cP = rootKey
    print("Root Node")
    print("kL:",kL.hex())
    print("kR:",kR.hex())
    print("AP:",AP.hex())
    print("cP:",cP.hex())
    print()

    account_path = "1852'/1815'/0'"
    account_node = cardano.derive_child_keys(rootKey, "1852'/1815'/0'", True)
    (kL, kR), AP, cP = account_node
    print("Account Key (", account_path, ")")
    print("kL:",kL.hex())
    print("kR:",kR.hex())
    print("AP:",AP.hex())
    print("cP:",cP.hex())
    print()

    spend_node = cardano.derive_child_keys(account_node, "0/0", False)
    (AP, cP) = spend_node
    print("Spending Key")
    print("AP:",AP.hex())
    print("cP:",cP.hex())
    print()

    spend_pubkeyhash = hashlib.blake2b(AP, digest_size=28).digest()

    stake_node = cardano.derive_child_keys(account_node, "2/0", False)
    (AP, cP) = stake_node
    print("Staking Key")
    print("AP:",AP.hex())
    print("cP:",cP.hex())
    print()

    stake_pubkeyhash = hashlib.blake2b(AP, digest_size=28).digest()

    bech32_data = b"\x01" + spend_pubkeyhash + stake_pubkeyhash

    data = bytes.fromhex(bech32_data.hex())

    out_data = bech32.convertbits(data, 8, 5)

    encoded_address = bech32.bech32_encode("addr", out_data)

    print("First Base Address: ", encoded_address)
    print()



