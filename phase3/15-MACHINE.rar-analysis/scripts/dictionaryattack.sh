#!/bin/sh

BASE_WORDLIST="wordlists/base_wordlist.txt"
WORDLIST="wordlists/permuted_wordlist.txt"

sort -u "$BASE_WORDLIST" > wordlists/wordlist_no_dupes.txt
mv wordlists/wordlist_no_dupes.txt "$BASE_WORDLIST"
python3 scripts/create_new_wordlist.py > "$WORDLIST"
cat "$BASE_WORDLIST" "$WORDLIST" > wordlists/wordlist_no_dupes.txt
mv wordlists/wordlist_no_dupes.txt "$WORDLIST"
hashcat -m 12500 -o cracked.txt MACHINE.hashcat wordlists/permuted_wordlist.txt
