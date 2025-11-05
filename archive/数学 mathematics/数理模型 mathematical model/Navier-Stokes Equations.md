---
alias:
    ['Navier-Stokes Equations']
---
- 非圧縮性
- 等質
$$
\rho(\frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla)\vec v) = -\nabla p + \mu \nabla^2 \vec v + \rho\vec f
$$
$$
\frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla)\vec v = -\frac{1}{\rho}\nabla p + \nu \nabla^2 \vec v + \vec f
$$
- variable
    - $\rho$  流体密度
    - v  流体速度
    - p  流体にかかる圧力
    - $\mu$  粘性係数
    - $\nu = \frac{\mu}{\rho}$  動粘性係数
- term
    - $\frac{\partial \vec v}{\partial t}$  時間微分項
        流れが急に加速したり減速したりする場合
    - $(\vec v \cdot \nabla)\vec v$  移流項、対流項
        速い部分と遅い部分が相互作用する効果
    - $\nabla p$  圧力項
        圧力が高い領域から低い領域へ流体が移動する
    - $\mu \nabla^2 \vec v$  粘性項
    - $\rho\vec f$  外力項