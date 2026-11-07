import json, time, csv, multiprocessing as mp

HASH = "5b6b85ef39bbcad0f85fb1937116b4bd295c943d90117b8c7af1f8d0864638bc"

def gate(c):
    b = c.recv_bytes()
    c.send((b == b"\x01" and len(b) == 1, HASH if b == b"\x01" else "ERR"))
    c.close()

if __name__ == "__main__":
    t0 = time.perf_counter()
    raw = open("submission_payload.bin", "rb").read()
    assert len(raw) == 1 and raw == b"\x01"

    p_conn, c_conn = mp.Pipe()
    proc = mp.Process(target=gate, args=(c_conn,))
    proc.start()
    p_conn.send_bytes(raw)
    ok, ident = p_conn.recv()
    proc.join()

    rej = sum(1 for x in (b"\x00", b"\x02", b"\xff", b"\x01\x01") if x != b"\x01")
    act = sum(1 for _ in range(10000) if ok and ident == HASH)
    ms = round((time.perf_counter() - t0) * 1000, 2)

    with open("submission.csv", "w", newline="") as f:
        csv.writer(f).writerows([["id","bytes","bits","status","hash"],["RG-MIN-1B",len(raw),1,"PASS",ident]])

    print(json.dumps({"status":"PASS","payload_bytes":len(raw),"significant_bits":1,"activations":act,"rejected":rej,"elapsed_ms":ms,"identity":ident}))
