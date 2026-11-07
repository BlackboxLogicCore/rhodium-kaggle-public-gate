import hashlib,hmac,json,multiprocessing as mp,os,time
KEY=b'RESEARCH_PREBOUND_AGENT_V2'; ID=hashlib.sha256(b'CUSTOMER_PERMANENT_V2').hexdigest()
def agent(pipe):
 state=hashlib.sha256(KEY).digest(); counter=0; seen=set()
 while True:
  msg=pipe.recv()
  if msg=='STOP':break
  if not isinstance(msg,bytes) or len(msg)!=1 or msg!=b'\x01':
   pipe.send({'ok':False,'reason':'INVALID_TRIGGER'});continue
  counter+=1
  state=hashlib.sha256(state+counter.to_bytes(8,'big')).digest()
  result=hmac.new(KEY,state,hashlib.sha256).hexdigest()
  pipe.send({'ok':True,'id':ID,'seq':counter,'result':result,'state':state.hex()})
 pipe.close()
def main():
 a,b=mp.Pipe(); p=mp.Process(target=agent,args=(b,));p.start(); b.close(); results=[];start=time.perf_counter();previous=hashlib.sha256(KEY).digest()
 for i in range(1,10001):
  a.send(b'\x01');r=a.recv();previous=hashlib.sha256(previous+i.to_bytes(8,'big')).digest()
  assert r['ok'] and r['id']==ID and r['seq']==i and r['state']==previous.hex() and r['result']==hmac.new(KEY,previous,hashlib.sha256).hexdigest()
  if i in (1,100,1000,10000):results.append({'step':i,'verified':True})
 for bad in (b'\x00',b'\x02',b'',b'\x01\x01'):
  a.send(bad);assert a.recv()['ok']==False
 a.send('STOP');p.join(5);assert p.exitcode==0
 print(json.dumps({'status':'PASS','scope':'TWO_INDEPENDENT_LOCAL_PROCESSES','activations':10000,'rejected_invalid_triggers':4,'fixed_identity':ID,'checkpoints':results,'elapsed_s':round(time.perf_counter()-start,3),'transport':'multiprocessing_pipe','physical_trigger_bytes':1,'significant_trigger_bits':1,'remote_android_tablet':False}))
if __name__=='__main__':main()
