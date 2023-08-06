kkpof - KeepKey Proof of funds
==============================
A simple utility that provides a proof of funds for the bitcoins secured
by a KeepKey. It simple utility that finds all bitcoin addresses on a
KeepKey that have an unspent balance and signs a message with the key
associated with each of those addresses.

This utility relies on the dataservices supplied by BlockCypher, so
your accounts need to be set up in the KeepKey Chrome Wallet.

Order of operations
-------------------
1. Find the KeepKey attached to the system
1. Get the data needed to compute the API token from the KeepKey
2. Query the wallet list from BlockCypher
3. For each wallet, query the wallet metadata
4. Decrypt the encrypted-node-path for each wallet
5. Quert the UTXOs from BlockCypher
6. For each unique address with a UTXO, lookup up the path of the
   address relative to the root of the wallet
7. Request a signature of the message for each address node path with a
   UTXO. User confirmation on the KeepKey is required.
8. Output the address and the signature

Example of use
--------------
````
> kkpof "Stellar.org Bitcoin Giveaway Round 2: GCE6KHQL4PXCOUFV27JQ2OXMP2LY4RB3E63RUT7DOENR7YUJ3ALFYX7W"
````

Your KeepKey will ask you to confirm the message once for each address
that has a UTXO. The screen will be similar to this:

````
SIGN MESSAGE
Stellar.org Bitcoin Giveaway Round 2:
GCE6KHQL4PXCOUFV27JQ2OXMP2LY4RB3E63RU
T7DOENR7YUJ3ALFYX7W
````

When this is confirmed on the device for each address, a list of
addresses and corresponding signatures will be output in the console:

Output
````
1Ca3HHUpfwkhyM2BFVQTaETaoobDQB5KpK IBNyA+WjHqEOWiG+B7+iU1mrKF4HGxZQGnwv0kAkWThIbxOvHOX98w74oHpuF4pM/8ncy4a3tWBDVCk8E2GggyU=
19R25QpxKJs26PGYTrapurg5u2DadRCMw HyjukdO0xGPaiPL0YcQe6coDDy+SpOzCHkjoMd1JhlETRiipWU7VbjDBChb1jqKwXANjMV3rlIRmEEtzG87w/8w=
15TxGsqDjhh5SYMb1K25xQbu6h3vFncgQE IBwKb3VKlwxmZAcDeI6SK3Kf9vrvIin16aOAp1BYN/AmeOxJtdb2MpvFK6xRl5b7SXjAy+QqTQP+uh0y/QvzrLg=
````

Entering a PIN
--------------

When you are asked for PIN, you have to enter scrambled PIN. Following
the numbers shown on KeepKey display, enter the their positions using the
numeric keyboard mapping:

````
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
````

For example: If your PIN is **1234** and KeepKey displays the following:

````
+---+---+---+
| 2 | 8 | 3 |
+---+---+---+
| 5 | 4 | 6 |
+---+---+---+
| 7 | 9 | 1 |
+---+---+---+
````

You will type: **3795**

Installation (Windows)
----------------------
* Install Python 2.7 (https://www.python.org/downloads/)
* Run C:\\python27\\scripts\\pip.exe install cython
* Install Microsoft Visual C++ Compiler for Python 2.7
* Clone this repository (using TortoiseGit) to local directory
* Run C:\\python27\\python.exe setup.py install (or develop)

Installation (Mac)
------------------


Installation (Debian-Ubuntu)
----------------------------
* sudo apt-get install python-dev python-setuptools cython libusb-1.0-0-dev libudev-dev git
* git clone https://github.com/keepkey/python-keepkey.git
* cd python-keepkey
* python setup.py install (or develop)
