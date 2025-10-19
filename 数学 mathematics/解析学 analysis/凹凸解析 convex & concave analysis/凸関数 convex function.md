$f : \R^n \to \R$ 
            $$
            \forall x \in \R^n, \forall \lambda \in[0, 1],\\ f(\lambda x + (1- \lambda)y) \leq \lambda f(x)+ (1-\lambda)f(y)
            $$
            - 準凸関数
                $$
                \forall x \in \R^n, \forall \lambda \in[0, 1],\\ f(\lambda x + (1- \lambda)y) \leq \max(f(x), f(y))
                $$
            - 凸包
                最小の凸集合
                - 凸集合全体の集合 \mathcal A
                $$
                \text{conv}(S) = \bigcap\{A \in \mathcal A| S \subset A \}
                $$
            - 命題(接超平面が下=凸関数)
                $$
                f(x) \geq f(y) + \nabla f(y)^\top(x-y)
                $$
                - 凸関数ならば接超平面は下
                    $$
                    f(\lambda x + (1- \lambda)y) \leq \lambda f(x)+ (1-\lambda)f(y) 
                    \\
                    f(y + \lambda (x - y)) \leq f(y)+ \lambda(f(x) - f(y)) \\
                    \frac{f(y + \lambda (x - y))-f(y)}{\lambda}
                    \leq f(x) - f(y)
                    \\
                    \frac{f(y + \lambda (x - y))-f(y)}{\lambda (x-y)}(x-y) 
                    \leq f(x) - f(y)
                    $$
                    $\lambda \to 0$ のとき
                    $$
                    \nabla f(y) (x-y) \leq f(x) - f(y)\\
                    f(y) + \nabla f(y) (x-y) \leq f(x)
                    $$
                - 接超平面は下ならば凸関数
                    $$
                    f(x) \geq f(z) + \nabla f(z)^\top(x-z) 
                    \\
                    f(y) \geq f(z) + \nabla f(z)^\top(y-z)
                    $$
                    内分点をとると
                    $$
                    \lambda f(x) + (1-\lambda) f(y) \geq\lambda(f(z) + \nabla f(z)^\top(x-z)) + (1-\lambda)f(z) + \nabla f(z)^\top(y-z)
                    $$
                    - term1
                        $$
                        \lambda f(z) + (1-\lambda) f(z) = f(z)
                        $$
                    - term2
                        $$
                        f'(z)(\lambda (x-z)+(1-\lambda)(y-z))
                        $$
                        $$
                        \lambda (x-z)+(1-\lambda)(y-z) \\
                        = \lambda x+(1-\lambda)y -z \\
                        = z - z \\
                        =0 
                        $$
                    $$
                    \lambda f(x) + (1-\lambda) f(y) \geq f(z)
                    $$
            - 命題(二階微分は正=凸関数)
                $$
                f(x)'' \geq 0
                $$
                - 凸関数ならば二階微分は正
                    $$
                    z = \lambda x + (1-\lambda)y
                    $$
                    xとyをTaylor展開して中点を求める
                    - f(x)
                        $$
                        \lambda f (x) = \lambda (f(z) + f'(z)(x - z) + \frac{1}{2} f''(z)(x - z)^2) + O(x^3)
                        $$
                    - f(y)
                        $$
                        (1-\lambda) f (y) = (1-\lambda)(f(z) + f'(z)(y - z) + \frac{1}{2} f''(z)(y - z)^2) + O(y^3)
                        $$
                    $$
                    \lambda f (x) + (1-\lambda) f (y)
                    $$
                    - term1
                        $$
                        \lambda f(z) + (1-\lambda) f(z) = f(z)
                        $$
                    - term2
                        $$
                        f'(z)(\lambda (x-z)+(1-\lambda)(y-z))
                        $$
                        $$
                        \lambda (x-z)+(1-\lambda)(y-z) \\
                        = \lambda x+(1-\lambda)y -z \\
                        = z - z \\
                        =0 
                        $$
                    $$
                    \lambda f (x) + (1-\lambda) f (y) = f(z) + \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2) \\
                    \lambda f (x) + (1-\lambda) f (y) - f(z) \geq \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2)
                    $$
                    凸関数なので
                    $$
                    \lambda f (x) + (1-\lambda) f (y)  \geq f(z) \\
                    \lambda f (x) + (1-\lambda) f (y)  - f(z) \geq 0
                    $$
                    よって
                    $$
                    \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2) \geq 0
                    $$
                    - $(\lambda (x - z)^2 + (1-\lambda)(y - z)^2)  > 0$
                    $$
                    f''(z) > 0
                    $$
                    - website
                        [凸関数とは？ ～性質と具体例～ (証明付) - 理数アラカルト -](https://risalc.info/src/convex-concave-function.html)
                - 二階微分は正ならば凸関数
                    $$
                    z = \lambda x + (1-\lambda)y
                    $$
                    xとyをTaylor展開して中点を求める
                    - f(x)
                        $$
                        \lambda f (x) = \lambda (f(z) + f'(z)(x - z) + \frac{1}{2} f''(z)(x - z)^2) + o(x^3)
                        $$
                    - f(y)
                        $$
                        (1-\lambda) f (y) = (1-\lambda)(f(z) + f'(z)(y - z) + \frac{1}{2} f''(z)(y - z)^2) + o(y^3)
                        $$
                    $$
                    \lambda f (x) + (1-\lambda) f (y)
                    $$
                    - term1
                        $$
                        \lambda f(z) + (1-\lambda) f(z) = f(z)
                        $$
                    - term2
                        $$
                        f'(z)(\lambda (x-z)+(1-\lambda)(y-z))
                        $$
                        $$
                        \lambda (x-z)+(1-\lambda)(y-z) \\
                        = \lambda x+(1-\lambda)y -z \\
                        = z - z \\
                        =0 
                        $$
                    $$
                    \lambda f (x) + (1-\lambda) f (y) = f(z) + \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2) \\
                    \lambda f (x) + (1-\lambda) f (y) - f(z) = \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2)
                    $$
                    二階微分が正なので
                    $$
                    f''(z) \geq 0
                    $$
                    - $(\lambda (x - z)^2 + (1-\lambda)(y - z)^2) \geq 0$
                    $$
                    \frac{1}{2} f''(z)(\lambda (x - z)^2 + (1-\lambda)(y - z)^2) \geq 0
                    $$
                    よって
                    $$
                    \lambda f (x) + (1-\lambda) f (y)  - f(z) \geq 0 \\
                    \lambda f (x) + (1-\lambda) f (y)  \geq f(z) 
                    $$
            - 命題(hessian行列が半正定値=凸関数)
                $$
                \nabla^2 f(x) \succeq 0
                $$
                - 凸関数ならばhessian行列が半正定値
                    凸関数の性質より
                    $$
                    f(x +th) \geq f(x) + t \nabla f(x)^\top h
                    \\
                    f(x +th) - f(x) - t \nabla f(x)^\top h \geq 0
                    $$
                    Taylor展開より
                    $$
                    f(x +th) = f(x) + t \nabla f(x)^\top h + \frac{t^2}{2} h^\top \nabla^2 f(x) h + o(t^3)
                    \\
                    f(x +th) - f(x) - t \nabla f(x)^\top h = \frac{t^2}{2} h^\top \nabla^2 f(x) h + o(t^3)
                    $$
                    よって
                    $$
                    \frac{t^2}{2} h\nabla f(x)^\top h + o(t^3) \geq 0 
                    \\
                    h\nabla f(x)^\top h + o(t) \geq 0
                    $$
                    t → 0のとき
                    $$
                    h\nabla f(x)^\top h \geq 0
                    $$
                - hessian行列が半正定値ならば凸関数
                    平均値の定理より
                    $$
                    f(y) = f(x) + \nabla f(x)^\top(y-x) + (y-x)^\top\nabla^2 f(\lambda x + (1-\lambda)y) (y-x)
                    $$
                    半正定値より
                    $$
                    (y-x)^\top\nabla^2 f(\lambda x + (1-\lambda)y) (y-x) \geq 0
                    $$
                    なので
                    $$
                    f(y) \geq f(x) + \nabla f(x)^\top (y-x)
                    $$
                    [命題(接超平面が下=凸関数)](https://www.notion.so/224ec42dd04b806198cde2e6cc876b66?pvs=21) 
                    上記の命題より凸関数である
            - 命題(局所最適解は大域最適)
                - $f: X \to \R$
                - xは局所最適解
                    $$
                    \existss x \in X, \forall y \in U(x,r), f(x) \leq f(y)
                    $$
                $$
                \forall y \in \R^n, \existss \lambda \in (0, 1), \\ 
                \lambda x + (1-\lambda)y \in O \\
                \lambda f(x) + (1-\lambda)f(y) \\ \geq f(\lambda x + (1-\lambda)y) \\\geq \lambda f(x) +(1 - \lambda)f(y) \\
                \geq f(x)
                $$