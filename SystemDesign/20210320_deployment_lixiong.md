The bare minimal design

- Start with:
    - single machine
    - small data
    
- Scenarios, allow svc owners to:
    - upload the to-be-deployed binary to deployment system
    - describe what machines the binary should deploy to
    - have a simple interface to track what machines are running whatever and progress of deployment

- Assume:
    - We have 100 machines, m1,m2,...,m100

- Software components:
    1. Svc1: Accept customer upload request. Assume:
        - binary is small, stored in local disk of 1 machine
        - specs:
            - UploadNewPayloads(svcName, svcVer, byte[] svcBin)
            - used by payload owners 
    2. Svc2: Accept config of what machines to deploy to. 
        - a file with all machine names on an appended line. 
        - specs:
            - RequestDeployPayloadToTargets(svcName, svcVer, targetMachines)
            - used by payload owners 
    3. Svc3: Collect what ver is actively running on each machine. 
        - data in memory, let end user to query
        - specs:
            - ReportRunningVersion(machineName, runningSvcName, runningSvcVer)
            - used by Svc4
        - Build Svc4 to run on all 100 machines to collect data and talk w/ Svc3
            - Expose an interface on Svc4 to accept a new version and run it
            - specs:
                - 
    4. Svc5: Orchestrate and push new versions. 
                
 
 