---
alias:
    ['Ethereum']
---
- component
    - Eth
        計算資源の利用料
    - transaction
        Ethの送金を行う取引data
    - gas
        smart contractを実行するために消費する燃料
    - address
        - EOA
            人間が利用する口座
        - contract address
            smart contractのための口座
    - smart contract
        - token contract
            所有者のaddressとtoken情報を紐付けてtokenを管理するsmart contract
- ERC Ethereum request for comment
    - ERC-20
        代替性tokenの規格
        [[totalSupply() → uint256]]
        [[balanceOf(address _owner) → uint256]]
        [[transfer(address _to, uint _value) → bool]]
        [[approve(address spender, uint  _value) → bool]]
        [[transferFrom(address _from, address _to, uint _value) → bool]]
        [[allowance(address _owner, address _spender) → bool]]
    - ERC-223
        誤送信時のtoken消失を解決
    - ERC-721
        NFTの規格
        - balanceOf(address _owner) → uint256
            ownerの所有するNFTの数を返す
        - ownerOf(uint256 _tokenId) → address
            uint256_tokenIdを指定してNFTの所有者を返す
        - safeTransferFrom(address _from, address _to, uint256 _tokenId)
        - tokenURL(uint256 _tokenId)
            metadataが記録されたfileの場所を返す
    - ERC-777
    - ERC-1155
        multi tokenの規格
    - ERC-4337
        accountの抽象化
    - ERC-4626
        金庫(vault)の規格
    - ERC-6551
    [ERC | Ethereum Improvement Proposals](https://eips.ethereum.org/erc)
- EIP Ethereum improvement proposal
- EVM Ethereum virtual machine