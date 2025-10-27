---
alias:
    ['approve(address spender uint _value)', '→', 'bool']
---
spenderに対しvalue分まで自分のtokenの引き出しを許可する
```solidity
function approve(address _spender, uint256 _value) public returns (bool success);
```