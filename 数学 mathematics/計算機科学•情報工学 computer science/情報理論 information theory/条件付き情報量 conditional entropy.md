---
alias:
    ['条件付き情報量', 'conditional entropy']
---
$$ H(Y|X) = \sum_{x \in \mathcal{X}} p(x) H(Y|X=x) \\ = -\sum_{x \in \mathcal{X}} p(x) \sum_{y \in \mathcal{Y}} p(y|x) \log\ p(y|x) \\ = -\sum_{x \in \mathcal{X}}\sum_{y \in \mathcal{Y}} p(x, y) \log\ p(x, y) $$
- 連鎖律 chain law
  $$ H(X, Y) = H(X) - H(Y|X) $$
  $$ H(X, Y) = \sum p(x, y) \log p(x, y) $$