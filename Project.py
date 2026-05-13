import os
import hashlib

# === Utility Functions ===

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def get_all_file_hashes(path):
    file_hashes = []
    for root, _, files in os.walk(path):
        for file in sorted(files):
            full_path = os.path.join(root, file)
            file_hashes.append(hash_file(full_path))
    return file_hashes

def build_merkle_tree(hashes):
    if len(hashes) == 0:
        return sha256("")
    if len(hashes) == 1:
        return hashes[0]

    mid = len(hashes) // 2
    left = build_merkle_tree(hashes[:mid])
    right = build_merkle_tree(hashes[mid:])
    return sha256(left + right)

def generate_merkle_root(directory_path):
    file_hashes = get_all_file_hashes(directory_path)
    return build_merkle_tree(file_hashes)

def is_tampered(original_root, current_root):
    return original_root != current_root

# === File Persistence ===

def save_root_hash(file_path, root_hash):
    with open(file_path, "w") as f:
        f.write(root_hash)

def load_root_hash(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        return f.read().strip()

# === Main Logic ===

def verify_integrity(target_dir, hash_store_path):
    current_root = generate_merkle_root(target_dir)
    original_root = load_root_hash(hash_store_path)

    if original_root is None:
        print("[INFO] Saving initial Merkle root.")
        save_root_hash(hash_store_path, current_root)
        print(f"Original Root: {current_root}")
        return

    print(f"Original Root: {original_root}")
    print(f"Current  Root: {current_root}")

    if is_tampered(original_root, current_root):
        print("⚠️ Tampering Detected!")
    else:
        print("✅ No Tampering Detected.")

# === Run Section ===

if __name__ == "__main__":
    # Replace this with your actual directory path
    directory_to_check = r"C:\Users\patri\OneDrive\Desktop\ADSA"  # Changed from example.txt to directory
    hash_storage_file = os.path.join(directory_to_check, "root_hash.txt")

    verify_integrity(directory_to_check, hash_storage_file)
