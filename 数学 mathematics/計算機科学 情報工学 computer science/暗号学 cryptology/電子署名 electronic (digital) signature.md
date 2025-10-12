- 
        - parameter
            - m 平文 plaintext
            - s 署名 signature
            - k 安全母数 security parameter
            - pk 公開鍵 public key
            - sk 秘密鍵 private/secret key
        $$ (G, S, V) $$
        - G 鍵生成算法 key generation algorithm
            $$ G: 1^k \to (pk, sk) $$
        - S 署名算法 signing algorithm
            $$ S: (m, sk) \to s $$
        - V 検証算法 verification algorithm
            $$ V: (m, s, pk) \to \{1, 0\} $$