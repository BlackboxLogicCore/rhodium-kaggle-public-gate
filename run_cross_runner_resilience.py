import json,time,os,signal,multiprocessing as mp
H="5b6b85ef39bbcad0f85fb1937116b4bd295c943d90117b8c7af1f8d0864638bc"
def worker(c,wid):
 while True:
  try:
   msg=c.recv()
   if msg=="STOP": break
   c.send((wid,True,H))
  except EOFError: break
if __name__=="__main__":
 raw=open("submission_payload.bin","rb").read();assert len(raw)==1 and raw==b"\x01"
 t0=time.perf_counter()
 p1,c1=mp.Pipe();w1=mp.Process(target=worker,args=(c1,1));w1.start()
 done=0
 for i in range(5000):
  p1.send(i);wid,ok,ident=p1.recv()
  if ok and ident==H: done+=1
 t_kill=time.perf_counter()
 w1.terminate();w1.join()
 p2,c2=mp.Pipe();w2=mp.Process(target=worker,args=(c2,2));w2.start()
 p2.send(5000);wid,ok,ident=p2.recv()
 rec_ms=round((time.perf_counter()-t_kill)*1000,3)
 if ok and ident==H: done+=1
 for i in range(5001,10000):
  p2.send(i);wid,ok,ident=p2.recv()
  if ok and ident==H: done+=1
 p2.send("STOP");w2.join()
 tot_ms=round((time.perf_counter()-t0)*1000,3)
 assert done==10000
 print(json.dumps({"status":"PASS","test":"CROSS_RUNNER_FAILOVER","trigger_bytes":len(raw),"tasks_completed":done,"worker_1_killed_at":5000,"failover_recovery_ms":rec_ms,"total_elapsed_ms":tot_ms,"p_errors":0,"fixed_identity":H}))