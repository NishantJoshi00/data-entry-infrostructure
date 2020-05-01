# Concept for Reminder App
## Web hosted API



                             +------------+                 ++
                             |    User    |                 || ----> Get all data
    +-----------+    +-------+ Management +-----+           || ----> Get today's task
    |           |    |       |   Server   |     |           || ----> Get task details (based on id)
    |           |    |       +----++------+     |           || ----> Get history
    |   Server  +----+            ||            |           || ----> Sync changes
    |           |    |       +----++------+     |           || ----> export all
    |           |    |       |  RESTful   |    +++          ||
    +-----+-----+    +-------+    API     +----+ +----------++
          |                  |  ENDPOINT  |    +++          ||
          |                  +------------+                 ||
       +--+-------+                                         ||
       | DATABASE |                                         ||
       +----------+                                         ||
                                                            || <---- import all
                                                            || <---- Add task
                                                            || <---- Modfiy task
                                                            || <---- mark/unmake task
                                                            ++
---
---
## Application to Implement
### Ubuntu

---
### Android


---
### Windows


---
