# Merkle Tree File Integrity Checker

A Python-based file integrity monitoring system using SHA-256 hashing and Merkle Trees.

## Features
- Recursive directory scanning
- SHA-256 file hashing
- Merkle Tree generation
- Tampering detection
- Persistent root hash storage

## Tech Stack
- Python
- hashlib
- os

## How It Works
1. Hashes all files in a directory
2. Builds a Merkle Tree
3. Stores the Merkle Root
4. Detects any file modification by comparing roots

## Run

```bash
python integrity_checker.py
```

## Future Improvements
- Real-time monitoring
- GUI dashboard
- Digital signature verification
- Parallel hashing
