---
alias:
    ['hypervisor virtual machine monitor']
---
物理的なcomputer上で複数の仮想機械（VM）を同時に実行・管理し、resourceを効率的に配分するsoftware
software that allows multiple virtual machines (VMs) to run on a single physical machine by abstracting and managing the hardware resources.
- type1/native
    installed directly on physical hardware
    - characteristic
        - Direct hardware control
        - No host OS required
        - high performance
            there is no intermediary layer
        - security
            Strong isolation between virtual machines
    - Hyper-V
        windowsに標準搭載
- type2/hosted
    runs on top of an existing host operating system like application
    - characteristic
        - host OS dependency
        - easy installation
        - performance limitation
            Due to the host OS acting as an intermediary
    - VirtualBox