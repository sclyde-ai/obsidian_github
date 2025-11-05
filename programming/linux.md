---
alias:
    ['linux']
---
- /
    root file system
    - /bin
    - /boot
    - /dev
        - /sda
            disk
        - /tty
            terminal
    - /etc
        - /passwd
        - /hosts
    - /home
        home directory
    - /lib
    - /media
        mount point for removable media
        - example
            - USB drives
    - /mnt
    - /opt
    - /root
    - /run
    - /sbin
    - /srv
    - /tmp
    - /proc
        - /self
            - /maps
                a detailed view of the memory mappings for the current process.
                - how to read
                    ```bash
                    address-range  permissions  offset  dev  inode  pathname
                    ```
                    - address range
                        ```bash
                        start-end
                        ```
                    - permissions
                        | r | read |
                        | --- | --- |
                        | w | write |
                        | x | execute |
                        | p | private |
                        | s | shared |
                    - offset
                        the distance (displacement) between the beginning of the file or device and the place of memory
                    - device
                        ```bash
                        major:minor
                        ```
                        - major
                            type of the device
                            | 0 |  |
                            | --- | --- |
                            | 8 | sd |
                            |  |  |
                        - minor
                            instance of the device
                    - inode
                    - pathname
                        | [heap] | heap memory |
                        | --- | --- |
                        | [stack] | stack memory |
                        | [vdso] | virtual dynamic shared object |
                        | [vvar] | virtual variable |
                        | [anon] | anonymous memory |
        - 
- /usr
    unix system resources
    - /bin
        most user commands
    - /include
    - /lib
    - /libexec
    - /local
    - /sbin
        system administration binaries
    - /share
    - /src
- /var
    - /log
[Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- linux distribution/distro
    a packaged version of the Linux operating system, including the Linux kernel, supporting utilities, libraries, and application software, tailored for specific use cases
    - Ubuntu
    - Debian
- files
    - .Xresources
        applicationの見た目の設定file
    - .xsettings
        デスクトップ環境全体で一貫したlook&feelの設定file