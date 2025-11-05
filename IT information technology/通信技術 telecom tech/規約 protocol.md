---
alias:
    ['規約', 'protocol']
---
- 応用層 application layer
    - HTTP hypertext transfer protocol
        web browserとweb serverの間で情報を交換するための通信規則
        ```
        Client       Server
          |            |
          |--Request-->|
          |            |
          |<--Response-|
          |            |
        ```
        - resource
            web上で識別可能なあらゆる情報やservices
            - 具体例 examples
                - HTML文書 .html
                - 画像file .jpg
                - 動画file .mp4
            - URI uniform resource identifier
                resourceを一意に識別するための文字列
                - URL uniform resource locator
                    場所を指定するURI
                    - scheme
                        - http://
                        - https://
                        - ftp://
                        - mailto:
                    - host
                        - www.
                        - ip address
                    - port
                        - :(number)
                        - default 443
                    - path
                        - /(string)
                    - query
                        parameterを渡す
                    - fragment
                    - 具体例 example
                        ```
                        https://www.example.com:443/search?q=hello&page=1#results
                        ```
                - URN uniform resource name
                    名前を指定するURI
                    - resourceが移動しても同じURNで識別できる
                    ```
                    urn:<名前空間識別子>:<名前空間固有文字列>
                    ```
                    - 種類
                        - ISBN 書籍
                        - ISSN 雑誌
                        - UUID
        - client
            servicesやresourceを要求する側
        - server
            servicesやresourceを提供する側
        - request
            clientからserverへの要求
            ```
            request_line
            header
            body(option)
            ```
            - request_line
                ```
                method target http_version
                GET /index.html HTTP/1.1
                POST /api/users HTTP/2
                DELETE /products/123 HTTP/1.1
                ```
                - http method
                    - GET
                    - POST
                    - PUT
                    - DELETE
                    - PATCH
            - header
            - body
        - response
            serverからclientへの応答
            ```
            status_line
            header
            body(option)
            ```
            - status_line
                ```
                http_version status_code message
                HTTP/1.1 200 OK
                HTTP/2 404 Not Found
                HTTP/1.1 500 Internal Server Error
                ```
                - status code
                    | code | 意味 |
                    | --- | --- |
                    | 1xx | 情報 |
                    | 2xx | 成功 |
                    | 3xx | redirect |
                    | 4xx | client error |
                    | 5xx | server error |
            - header
            - body
        - HTTPS hypertext transposer protocol secure
    - FTP file transfer protocol
        file
        - SFTP secure file transfer protocol
    - SMTP simple mail transfer protocol
        sending mail
    - POP post office protocol
        mail
    - IMAP internet message protocol
        mail server
        users can access by any device
- 通信層 transport layer
    - TCP transmission control protocol 伝送制御規約
        信頼性重視
        情報を確実に受信するためのprotocol
    - UDP user datagram protocol
        速度重視
- internet layer
    network間のdata転送
    - IP internet protocol
    - ICMP
    - ARP
- network interface layer
- TELNET telecommunication network
    operating a computer remotely
- MIME multipurpose internet mail protocol