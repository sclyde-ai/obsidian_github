   超平面と集団の最近点を最大化
   ![image.png](学問%20academics/notion/data_analysis/ExportBlock-8be93bf0-4b33-41d8-a364-5b0c7eb222bc-Part-1/image%202.png)
   - hard margin
       $$
       \min_{w, b} \frac{1}{2} \|w\|^2\ s.t.\ y_i(w^T x_i -b) \geq 1
       $$
       - 式の導出
           $$
           \left\{
             \begin{alignedat}{}
           w^Tx_i -b & \geq 1 & if &\ y_i = 1
           \\
           w^Tx_i -b & \leq -1 & if &\ y_i =-1
             \end{alignedat} 
           \right.
           $$
   - soft margin
       $$
       \frac{1}{n}\sum_{i=1}^n \max(0, 1-y_i(w^Tx_i-b)) + \lambda \|w\|^2
       $$
 structured SVM