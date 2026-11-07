import json,subprocess,time,multiprocessing as mp
tests=["test_kaggle_1_compression.py","test_kaggle_2_resilience.py","test_kaggle_3_streaming.py","test_kaggle_4_gate.py"]
if __name__=="__main__":
 t0=time.time();results={};ok_all=True
 for t in tests:
  st=time.time();res=subprocess.run(["python3",t],capture_output=True,text=True)
  elapsed=round((time.time()-st)*1000,2)
  passed=(res.returncode==0)
  results[t]={"passed":passed,"elapsed_ms":elapsed,"stdout":res.stdout.strip()}
  if not passed: ok_all=False
 tot_ms=round((time.time()-t0)*1000,2)
 print(json.dumps({"overall_status":"PASS" if ok_all else "FAIL","total_elapsed_ms":tot_ms,"details":results},indent=2))