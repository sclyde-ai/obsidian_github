- kernel
    - process management
        - CPU central processing unit
            processing and controlling
            - clock rate
                an indicator of the processor's speed
                unit : Hz
        - process/task
            - nice value
                a way to adjust the CPU scheduling priority of a process, ranging from -20 (highest priority) to +19 (lowest priority)
    - memory and storage management
        - memory/primary storage
            short term/temporary
            volatile
            - main memory
            - cache memory
                holds copies of data from RAM for fasterCPU access
            - register memory
                very fast memory in CPU
            - heap memory
                dynamic memory allocation
            - stack memory
                local variable
                function parameter
            - static memory
                global variable
            - buffer
        - storage/secondary storage
            long term/permanent
            non-volatile 
            - partition
                a logical division of storage
        - virtual memory
            - paging
                mapping data from page to frame
                ![image.png](学問%20academics/notion/IT/ExportBlock-2d668fb2-00bc-4ec6-9092-d6ebd07875b4-Part-1/image%201.png)
                ![image.png](学問%20academics/notion/IT/ExportBlock-2d668fb2-00bc-4ec6-9092-d6ebd07875b4-Part-1/image%202.png)
                - page
                    virtual memory divided into equal size blocks
                - frame
                    physical memory divided into equal size blocks
            - swapping
                temporarily moving data from its main memory to a storage device 
                to free up main memory for active processes
                - swap in
                    from a storage to a memory
                - swap out
                    from a memory to a storage
            - FIFO first in first out
                removing the oldest item
            - LRU least recently used
                removing the item not accessed in the longest time 
            - LFU least frequently used
                removing the item not accessed the least number of times
    - device management
        - disk
            physical device
            - command
                [df](https://www.notion.so/df-216ec42dd04b81b792eccf4ebaa9170a?pvs=21) 
                [du ](https://www.notion.so/du-216ec42dd04b812fb1aaf904d2269d64?pvs=21) 
        - block device
            - command
                [lsblk](https://www.notion.so/lsblk-216ec42dd04b81ce8820c47f715e3b08?pvs=21) 
        - mount
            the process by which the operating system makes files and directories on a storage device or accessible to the user through the system's directory tree.
            - mount point
                外部のdeviceを操作するdirectory
            - command
                [mount ](https://www.notion.so/mount-216ec42dd04b813bb40ed4e80b01304f?pvs=21) 
    - network management
        - interface
            allow systems to communicate and exchange information 
            - loopback interface
                - self-communication
                - always active
                - IP address
                    IPv4 127.0.0.1
                    IPv6 ::1
            - ethernet interface
            - bridge interface
            - virtual ethernet interface
        - ethernet
            networking technology that enables devices to communicate over a wired local area network (LAN)
    - security
- device driver
- multi thread