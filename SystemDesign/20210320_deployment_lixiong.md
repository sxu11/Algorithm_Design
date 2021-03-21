The bare minimal design
- Start with:
    - single machine
    - small data
    
- Scenarios, allow svc owners to:
    - upload the to-be-deployed binary to deployment system
    - describe what machines the binary should deploy to
    - have a simple interface to track what machines are running whatever and progress of deployment

- Assume:
    - We have 100 machines (Data Planes), m1,m2,...,m100

- Software components:
    1. Svc1: Accept customer upload request. Assume:
        - binary is small, stored in local disk of 1 machine (Control Plane)
        - specs:
            - UploadNewPayloads(svcName, svcVer, byte[] svcBin)
                - e.g. save & name the file as svcName_svcVer
            - used by payload owners 
    2. Svc2: Accept config of what machines to deploy to. 
        - a file with all machine names on an appended line. 
        - specs:
            - RequestDeployPayloadToTargets(svcName, svcVer, targetMachines)
                - e.g. save & name the file as target_svcName_svcVer
            - used by payload owners 
    3. Svc3: Collect what ver is actively running on each machine. 
        - data in memory, let end user to query
        - specs:
            - ReportRunningVersion(machineName, runningSvcName, runningSvcVer)
                - runningVer[machineName] = string.Format(“{0}_{1}”, machineName, runningServiceName);
            - used by Svc4
        - Build Svc4 to run on all 100 machines to collect data and talk w/ Svc3
            - Expose an interface on Svc4 to accept a new version and run it
            - specs:
                - RunIt(svcNameToRun, svcNameToRun, byte[] payload)
                    - String filename = string.Format(“{0}_{1}”, machineName, runningServiceName) 
                    - File.SaveToExecutablePath(payload, filename); 
                    - Kill(serviceNameToRun); // step2: kill current running version
                    - Run(filename);  // step3: run the new version
                - used by Svc4?
                - void Main():
                    - e.g. while(true):
                        - gather running ver in this machine
                        - svc3.ReportRunningVersion(thisMachineName, runningSvcName, runningSvcVer)
    4. Svc5: Orchestrate Svc 1~3 and push new versions. 
        - void Main()
            - While(true) 
                - Foreach(string machineName in targetMachines) 
                    - If(runningVersion[machineName] != expectedVersion)
                        - ClientInterface svc4 = new client(machineName); 
                        - svc4.RunIt(serviceName, serviceVersion, payload); 

                
- Enrich the functionalities
    - M svc, N ver 
    - Each 10 GB, too large
        - DynamicStorage (key-value), for high
            - availability
            - durability
            - read throughput
        - Mesh/peer-to-peer. Client svc breaks down into: 
            - SvcMgr
            - GetAndRunSvc
            - SAD (?)
    - Machine name list inconvenient; group into:
        - Environment
        - Machine Function
    - Deploy simul-ly?
        - gradually, due to some policy (e.g. FDbyFD)
    - send config to Orch?
        - checkin ini to git/SourceDepot (PFGold is a SD repo)
            - history track
            - permission
            - enforce tests (VLAD ?)
        - a Builder svc import ini into Orch
    
- More functionalities:
    - customized policy:
        
        
        
        
