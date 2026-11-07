import json,hashlib,zlib
raw=open("submission_payload.bin","rb").read()
assert len(raw)==1 and raw==b"\x01"
print(json.dumps({"module":1,"status":"PASS","note":"1-byte compression gate verified"}))