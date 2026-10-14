import json
import re
import sys
from pathlib import Path

HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")

def main(path):
    d = json.loads(Path(path).read_text(encoding="utf-8-sig"))

    required = (
        "test_id",
        "input_sha256",
        "restored_sha256",
        "bit_identical",
        "p0_pass",
        "status",
    )

    missing = [k for k in required if k not in d]

    ok = (
        not missing
        and HEX64.fullmatch(str(d.get("input_sha256", ""))) is not None
        and HEX64.fullmatch(str(d.get("restored_sha256", ""))) is not None
        and d["input_sha256"].lower() == d["restored_sha256"].lower()
        and d["bit_identical"] is True
        and d["p0_pass"] is True
        and d["status"] == "PASS"
    )

    print(json.dumps({
        "PUBLIC_EVIDENCE_VALID": bool(ok),
        "missing": missing
    }, sort_keys=True))

    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
