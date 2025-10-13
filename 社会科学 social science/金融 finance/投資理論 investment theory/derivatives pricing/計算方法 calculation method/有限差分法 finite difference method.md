時間と空間を一定区間で区切り離散化
- 差分
    - 前進差分
        $$
        \frac{\partial V}{\partial t} \approx \frac{V_{i, j+1} - V_{i, j}}{\Delta t}
        $$
    - 後退差分
        $$
        \frac{\partial V}{\partial t} \approx \frac{V_{i, j} - V_{i, j-1}}{\Delta t}
        $$
    - 中心差分
        $$
        \frac{\partial V}{\partial t} \approx \frac{V_{i, j+1} - V_{i, j-1}}{2\Delta t}
        $$
- 方法
    - 陽的差分法 explicit
        $$
        V_{i,j+1} = V_{i,j} + \Delta t \left( r S_i \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{\Delta S^2} - r V_{i,j} \right)
        $$
    - 陰的差分法 implicit
        $$
        \frac{V_{i,j+1} - V_{i,j}}{\Delta t} + r S_i \frac{V_{i+1,j+1} - V_{i-1,j+1}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j+1} - 2V_{i,j+1} + V_{i-1,j+1}}{\Delta S^2} - r V_{i,j+1} = 0
        $$
    - 半陽的差分法 Crank-Nicolson
        $$
        \frac{V_{i,j+1} - V_{i,j}}{\Delta t} = \frac{1}{2} \left[ r S_i \frac{V_{i+1,j+1} - V_{i-1,j+1}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j+1} - 2V_{i,j+1} + V_{i-1,j+1}}{\Delta S^2} - r V_{i,j+1} \right] + \frac{1}{2} \left[ r S_i \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S} + \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{\Delta S^2} - r V_{i,j} \right]
        $$