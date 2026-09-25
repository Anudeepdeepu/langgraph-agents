1. STATE
   ↓
What information does my workflow carry?

application
comments
retry_count
approved


2. NODES
   ↓
What work can happen?

A → application()
B → process()
C → approval()


3. EDGES
   ↓
What order should things happen?

START → A → B
             ↓
          decision
          ↙      ↘
         A        C → END


4. INVOKE
   ↓
Actually start the workflow

retry_count = 0
approved = False
        ↓
       ...
        ↓
retry_count = 3
approved = True