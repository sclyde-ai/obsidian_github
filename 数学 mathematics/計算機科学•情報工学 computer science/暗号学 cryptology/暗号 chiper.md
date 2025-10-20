$$ (P, C, K, E, D) $$
- meaning
    - P 平文 plaintext
    - C 暗号文 cipher text
    - K 鍵 key
        - 暗号化鍵 encryption key
        - 復号鍵 decryption key
        - Diffie-Hellman key
    - E 暗号化 encryption
        $$ E_k : P \to E, k \in K $$
    - D 復号 decryption
        $$ D_k : C \to P, k \in K $$
- 古典暗号 classical cipher
    - 換字式暗号 substitution cipher
        文字の入れ替え
    - 転置式暗号 transposition cipher
        順番の入れ替え
    - stream cipher
        $$ x_i, y_i, s_i \in \{0, 1\} $$
        - encryption
            $$ y_i = e(x_i) = x_i + s_i \mod 2
            $$
            Xor gate
        - decryption
            $$ x_i = d(y_i) = y_i + s_i \mod 2
            $$
            Xor gate
    - Caesar cipher
        alphabet を数文字分 shift
    - Vigenere cipher
    - Enigma cipher
- 現代暗号 modern cipher
    - RSA cipher
    - DSA cipher
    - 楕円曲線暗号
    - Elgamal cipher
    - Rabin cipher
- 安全性 security
    - 情報理論的安全性 information theoretic security
    - 計算量的安全性 computational security