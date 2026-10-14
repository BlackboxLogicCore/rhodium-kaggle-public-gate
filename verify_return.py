import csv, hashlib, json, sys
from pathlib import Path

EXPECTED_BYTES = 698914
EXPECTED_SHA256 = "2C6C60142C3FD99BF25B324994D6EDD837CA6DA7326213253399BF99AC5C46BA"

def verify(path):
    p = Path(path)
    size = p.stat().st_size
    sha = hashlib.sha256(p.read_bytes()).hexdigest().upper()
    result = {
        "file": p.name,
        "bytes": size,
        "sha256": sha,
        "expected_bytes": EXPECTED_BYTES,
        "expected_sha256": EXPECTED_SHA256,
        "bit_identical": size == EXPECTED_BYTES and sha == EXPECTED_SHA256,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["bit_identical"] else 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_return.py <returned RHODIUM-KAGGLE-ROUNDTRIP.csv>")
        raise SystemExit(2)
    raise SystemExit(verify(sys.argv[1]))
