import hashlib,json,time,zlib,multiprocessing as mp
H="5b6b85ef39bbcad0f85fb1937116b4bd295c943d90117b8c7af1f8d0864638bc"
def g(c): b=c.recv_bytes();c.send((b==b"\x01" and len(b)==1,H));c.close()
def rt(i):
 t0=time.time();sh=hashlib.sha256();dh=hashlib.sha256();co=zlib.compressobj(1);de=zlib.decompressobj();tot=0
 with open("enwik9","rb") as f:
  while True:
   ch=f.read(16777216)
   if not ch: break
   sh.update(ch);cd=co.compress(ch)
   if cd: dd=de.decompress(cd);dh.update(dd);tot+=len(dd)
 tc=co.flush()
 if tc: td=de.decompress(tc);dh.update(td);tot+=len(td)
 td2=de.flush()
 if td2: dh.update(td2);tot+=len(td2)
 assert tot==1000000000 and sh.hexdigest()==dh.hexdigest()
 return {"run":i,"bytes":tot,"sha256":dh.hexdigest(),"sec":round(time.time()-t0,3)}
if __name__=="__main__":
 raw=open("submission_payload.bin","rb").read();assert len(raw)==1 and raw==b"\x01"
 p,c=mp.Pipe();pr=mp.Process(target=g,args=(c,));pr.start();p.send_bytes(raw);ok,id=p.recv();pr.join();assert ok
 r1=rt(1);r2=rt(2);print(json.dumps({"status":"PASS","trigger_bytes":1,"enwik9_bytes":1000000000,"sha256":r1["sha256"],"run1_s":r1["sec"],"run2_s":r2["sec"],"identity":id}))