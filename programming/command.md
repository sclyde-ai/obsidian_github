            - man
            - file or directory
                - cd
                    - current directory
                - ls
                    - list
                - touch
                - mkdir
                - rm [file or directory]
                    file or directory 削除 
                    | -f | 確認なし |
                    | --- | --- |
                    | -d | directory削除 |
                    | -r | 再帰的に |
                    - remove
                - mv
                - cp
                    | -r  | 全体をcopy |
                    | --- | --- |
                    |  |  |
                    |  |  |
                - chmod
                    - 数値
                        ```bash
                        chmod 764 hoge.txt
                        ```
                        - mode
                            | number | alphabet | permission |
                            | --- | --- | --- |
                            | 4 | r | read |
                            | 2 | w | write |
                            | 1 | x | execution |
                    - alphabet
                        ```bash
                        chmod u+x hoge.txt
                        ```
                        - 変更対称
                            | u | user |
                            | --- | --- |
                            | g | group |
                            | o | other |
                            | a | all |
                        - 変更方法
                            | = | にする |
                            | --- | --- |
                            | + | 付与 |
                            | - | 除去 |
                        - 変更内容
                            | r | read |
                            | --- | --- |
                            | w | write |
                            | x | execution |
                - echo
                - ar
                    manage archive file 
                    | rcs | make |
                    | --- | --- |
                    | t | show |
                    | r | add |
                    | d | delete |
            - resource
                - df
                    check the amount of free space on disk
                    | -h | わかりやすい |
                    | --- | --- |
                    |  |  |
                    |  |  |
                - du
                    check the amount of usage of disk
                    | -s/—summarize | 指定したdirectoryのみ |
                    | --- | --- |
                    | -h/—human-readble | 読みやすい表示 |
                    | -d/—max-depth (number) | 深さ指定 |
                    - sort
                        ```bash
                        du --max-depth=1 -h | sort -hr
                        ```
                - top
                    - how to read
                        - system summary
                            - first line: basic sys info
                                - load average
                                    1, 5, and 15 ninutes
                            - second line: task/process info
                            - third line: CPU usage
                                | us | user |  |
                                | --- | --- | --- |
                                | sy | system |  |
                                | ni | nice  |  |
                                | id | idle |  |
                                | wa | iowait |  |
                                | hi | hardware interrupt |  |
                                | si | software interrupt |  |
                                | st | steal |  |
                            - four and five lin: memory usage
                        - process list
                            - PR priority
                            - NI nice value
                            - VIRT virtual
                            - RES physical
                            - SHR shared
                            - S process state
                                | R | running |
                                | --- | --- |
                                | S | sleeping |
                                | D | uninterruptible sleep |
                                | Z | zombie |
                                | T | stopped |
                            - COMMAND
                                name of process
                        - 
                    - command
                        | q | quit |
                        | --- | --- |
                        | k | kill |
                        | r | renice |
                        | M | sort by memory |
                        | P | sort by CPU |
                        | T | sort by runtime |
                        | shift + P | sort by PID |
                - nice
                - renice
            - hardware
                - lsblk
                    show the info of block device 
                    - NAME
                    - MAJ;MIN
                    - RM
                        | 1 | removable |
                        | --- | --- |
                        | 0 | not removable |
                    - SIZE
                        the size od a device or partition
                    - RO
                        | 1 | read only |
                        | --- | --- |
                        | 0 | read and write |
                    - TYPE
                        the type of device
                        | disk | physical disk |
                        | --- | --- |
                        | part | partition |
                        | rom | read only memory |
                        | lvm | logical volume maanger |
                        | crypt | crypted device |
                        | loop | loop back  device |
                        | dm | device mapper |
                        | raid | redundant array of independent disk |
                    - MOUNTPOINT
                - mount
                - reboot
            - user&group
                - adduser
                    add a user to a group
                - addgroup
                    create a group
                - getent
                    show the list of user info
            - network
                - ip
                    ```bash
                    ip [option] object command
                    ```
                    - object
                        | link | Network intrerface |
                        | --- | --- |
                        | a/addr/address | IP address |
                        | route | routing table |
                        | neigh | ARP table |
                    - command
                        | show |  |
                        | --- | --- |
                        |  |  |
                        |  |  |
                        - show
                            - interface name
                                | lo | loopback |
                                | --- | --- |
                                | eth | wired ether |
                                | wlan | wireless interface |
                            - flags <>
                                | LOOPBACK |  |
                                | --- | --- |
                                | BROADCAST |  |
                                | MULTICAST |  |
                                | UP |  |
                                | LOWER_UP |  |
                                | NO-CARRIER |  |
                                | PROMISC |  |
                                | ALLMULTI |  |
                                | DYNAMIC |  |
                                | RUNNIN |  |
                            - mtu
                                maximum transmission unit
                            - qdisc
                                queuing discipline
                                | noqueue |  |
                                | --- | --- |
                                | pfifo_fast |  |
                            - state
                                | UP | active |
                                | --- | --- |
                                | DOWN | inactive |
                                | UNKNOWN |  |
                            - mode
                            - group
                            - qlen
                            - link/
                            - brd
                - nmcli
                    ```bash
                    nmcli object [option] {command | help}
                    ```
                    - object
                        | dev |  |
                        | --- | --- |
                        |  |  |
                        |  |  |
                    - option
                        | wifi |  |
                        | --- | --- |
                        |  |  |
                        |  |  |
                    - 
                - lsof
            - environment
                - env
                - printenv
            - get info
                - date
                    get the now time
                    | %Y | year |
                    | --- | --- |
                    | %m | month |
                    | %d | date |
                    | %H | hour |
                    | %M | minute |
                    | %S | second |
                - ulimit
                    | -a | all |
                    | --- | --- |
                    | -n | file descriptorの最大値 |
                    | -m | memoryの最大値 |
            - editor
                - vim
                - nano
                    - ctrl+s
                        上書き保存
                    https://qiita.com/snct_hu/items/971d512c26dd8b3a3b3c
            - apt
                package management command used in debian distribution 
            - su
                substitute user
            - sudo
- ln
  linkを作成する。
   - git
	   - hard link: git remoteに反映されない
	   - symbolic link: git remoteに反映される