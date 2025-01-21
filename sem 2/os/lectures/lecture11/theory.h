Operating Systems Structure
----------------------------
KERNAL
                                                                                                                                Tech book keeping

           interrupts
         /  (talk to the hardware)
hardware - process manager          -> memory management  -> phisical I/O  -> File System  -> Job planning & resource allocation
         \  (chosses processes)
           CPU dispathcer
            (?)

                                                                                                                                Book keeping


    Compiler + Assemblying + Linkers + Loaders
    Interpreters + Macro processors + Editor + Debuggers     -> IDEs
    Utils + Libraries + DataBases + Other


Processes
-----------
   states

        HOLD
         |
  ----> READY <---
 |      | |       |
WAIT <- RUN  -> SWAP
         |
        FINISH

Scheduling
-----------
    - FCFS (FIFO order)
    - SJF (Small Jobs First)
    - Priorities
    - Deadline scheduling

DeadLock
---------
