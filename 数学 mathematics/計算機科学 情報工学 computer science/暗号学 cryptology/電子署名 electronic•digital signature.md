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
公開鍵暗号方式 PKC public key cryptography
| 送信者 |  | 受信者 |
| --- | --- | --- |
|  |  | 秘密鍵を使い公開鍵を作成 |
| 公開鍵を取得 | ← | 公開鍵を送信 |
| 公開鍵を使い平文を暗号化 |  |  |
| 暗号文を送信 | → | 暗号文を取得 |
|  |  | 秘密鍵を使い暗号文を復号 |
- rsa暗号
- 手順
	- 鍵生成
		大きな素数p, q
		$$
		n=pq
		$$
		- 公開鍵
			$$
			k_{pub}\in \N := \lnot (\exist m \in \N/1, ma=k_{pub} \land mb = (p-1)(q-1), \forall a, b \in \N)
			$$
			を公開鍵という
		- 秘密鍵
			$$
			k_{pri} \in \N := k_{pub} k_{pri}\equiv 1 \mod (p-1)(q-1)
			$$
			を秘密鍵という
	nと公開鍵を公開
	秘密鍵を秘匿
	- 暗号化
		送信文m less than n
		$$
		C := m^{k_{pub}} \mod n
		$$
		Cを暗号文とする
	暗号文を送信
	- 復号
		$$
		C^{k_2} \mod n
		$$
		はmと一致する

- 公開鍵基盤 PKI public key infrastructure
    internet上で安全な情報交換を支えるためのsecurity基盤
    a system that uses digital certificates to authenticate and encrypt data, ensuring secure communication and transactions by verifying the identities of users, devices, and services
    - 電子証明書
    - 認証局 CA
- eIDAS **e**lectronic **Id**entification, **A**uthentication and trust **S**ervices
    EU reguration
- AES advanced electronic signature
- QES qualified electronic signature
- e-seal