---
alias:
    ['docker']
---
            アプリケーションを構築し、コンテナ化するためのクライアントサーバー型アプリケーション
            - docker daemon
            - docker engine REST api
            - docker CLI
        - docker image
            アプリケーションの実行に必要なソースコード、依存関係、ツールを含んだパッケージで、コンテナ作成時に指示を出す読み取り専用のテンプレートです
            - command
                - build
                    - option
                        | -t/—tag | name image |
                        | --- | --- |
                        |  |  |
                        |  |  |
                - run
                - images
                - search
                - pull
                - rmi
                    remove image
                - login
        - docker container
            システムの他の部分に影響を与えることなく、アプリケーションを実行できる隔離された領域
            - 標準化
            - 軽量
            - 安全性
            - command
                - ps
                - start
                - stop
                - restart
                - exec
                - rm
        - docker compose
            複数のコンテナを1つのサービスとして実行するために設計されたツール
            - command
                - build
                    execute the Dockerfile in the specified directory
                - image
                - network_mode
                - environment
                - volumes
        - docker network
            docker container が互いに通信したり、外部と通信したりするための仮想network環境
            - driver
                docker network の動作方法や接続方式を決定する部品
                - bridge
                - host
                - overlay
                - macvlan
                - none
            - scope
        - Dockerfile
            Dockerイメージを構築するための指示が記載されたテキスト文書
        - mount
            - bind mount
                ホストOSとストレージを共有する方式
            - volume mount
                Dockerが管理する共有ストレージを使用する方法
            - tmpfs
        - docker desktop
        - docker hub
        - docker host
        - docker client
        - docker object
        - docker documentation
        - command
        - website
            [Dockerとは（徹底解説）](https://kinsta.com/jp/knowledgebase/what-is-docker/)
# command
## docker pull
    imageをpullする
## docker build 
    dockerfileからimageを構築する
## docker run 
    imageからcontainerを起動する
## docker images 
    localのdocker imageの一覧を表示する
## docker stop
    containerを停止する
## docker rm
    停止しているcontainerを削除する
# words
# commonly used commnad