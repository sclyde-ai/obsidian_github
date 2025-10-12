- shell
    - 環境変数 global variable
        - errno
    - 記号 symbol
        - $ variable
            変数の参照
            - 例 echo $NAME
        - $(command)
            commandの埋め込み
            - 例 echo "now: $(date)”
        - ;
            前の成功・失敗に関係なく次を実行
            - semicolon
        - &
            前のと同時に次を実行(back ground実行)
            - ampersand
        - &&
            前が成功したときのみ次を実行
        - ||
        - *
            任意の文字列
            - wildcard
        - ?
            任意の一文字
    - windows command
        - wsl
    - 禁忌の呪文 Avada Kedavra
        [【危険シェル芸】禁じられた闇の魔術とその防衛術💥 - Qiita](https://qiita.com/_-_-_-_-_/items/214d537aae2c1488692c)
- package
    - package installer
        - pip
            - install
                | -r  | Install from a requirements file |
                | --- | --- |
                |  |  |
                |  |  |
            - uninstall
            - list
            - show
            - download
            - freeze
        - conda
    - openssh-server
    - UFW
        - ufw enable
        - ufw allow
        - ufw status
    - libpam-pwquality
- package manager
    - pip
    - npm
    - apt
    - yum
    - Homebrew
- filename extension
    - c
    - py
    - ipynb
    - stl
    - T
- ngrok