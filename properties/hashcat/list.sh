#!/bin/bash

# Define hash type (mode) - e.g., 0 for MD5
HASH_TYPE=0

# Define your hash file and wordlist
HASH_FILE=hashes.txt
WORDLIST=/usr/share/wordlists/rockyou.txt

# Run Hashcat
hashcat -m $HASH_TYPE $HASH_FILE $WORDLIST

echo "Hashcat run complete."
