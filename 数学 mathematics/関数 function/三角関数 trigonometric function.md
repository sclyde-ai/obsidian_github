![image.png](attachment:fa058d7f-64af-40de-b2f9-a363d10ed8be:image.png)
||def|differential|calculus|
|---|---|---|---|
|sin||cos|-cos|
|cos||-sin|sin|
|tan|sin/cos|sec^2|\ln|
|cot|cos/sin|-csc^2|\ln|
|sec|1/cos|sec tan|\ln|
|csc|1/sin|-csc cot|-\ln|
- sin 正弦 sine
    $$ \sin x $$
    - differential
        $$ \cos x $$
        - proof
            $$ \lim_{h\to 0} \frac{\sin (x+h) - \sin x}{h} \\ = \lim_{h\to 0} \frac{}{} $$
    - calculus
        $$ -\cos x $$
    - sin = x
        $$ x $$
    - exponential
        $$ \frac{e^x -e^{-ix}}{2i} $$
    - Maclaurin
        $$ \sum^\infin_{n=0} = x - \frac{x^3}{3!} + \frac{x^5}{5!} ... $$
- cos 余弦 cosine
    $$ \cos x $$
    - differential
        $$ -\sin x $$
    - calculus
        $$ \sin x $$
    - sin = x
        $$ \sqrt {1-x^2} $$
    - exponential
        $$ \frac{e^x + e^{-ix}}{2} $$
    - Maclaurin
        $$ \sum^\infin_{n=0} = 1 - \frac{x^3}{2!} + \frac{x^5}{4!} ... $$
- tan 正接 tangent
    $$ \frac{\sin}{\cos} $$
    - differential
        $$ \sec^2x $$
    - calculus
        $$ \ln |\cos| $$
    - sin = x
        $$ \frac{x}{\sqrt{1-x^2}} = \frac{1}{\sqrt{\frac{1}{x^2}-1}} $$
- cot 余接 cotangent
    $$ \frac{\cos}{\sin} $$
    - differential
        $$ -\csc^2 $$
    - calculus
        $$ \ln |\sin| $$
    - sin = x
        $$ \frac{\sqrt{1-x^2}}{x} = \sqrt{\frac{1}{x^2}-1} $$
- sec 正割 secant
    $$ \frac{1}{\cos} $$
    - differential
        $$ \sec x \tan x $$
    - calculus
        $$ \ln |\sec + \tan| $$
    - sin = x
        $$ \frac{1}{\sqrt{1-x^2}} $$
- csc 余割 cosecant
    $$ \frac{1}{\sin} $$
    - differential
        $$ -\csc x \cot x $$
    - calculus
        $$ \ln |\csc + \cot| $$
    - sin = x
        $$ \frac{1}{x} $$
- sinc/cardinal sine
    $$ \frac{\sin x}{x} $$
    - lim x \to 0
        $$ \sin x< x < \tan x \\ 1 < \frac{x}{\sin x} < \frac{1}{\cos x} $$
        逆数
        $$ \cos x < \frac{\sin x}{x} < 1 \\ x \to 0 \\ 1 < \frac{\sin x}{x} < 1 \\ \frac{\sin x}{x} = 1 $$
- 基本公式
    1. $\sin^2 + \cos^2 = 1$
    2. $\tan^2 + 1 = \sec^2$
    3. $1 + \cot^2 = \csc^2$
- 半角公式
    - sin
        $$ \sin^2 x =\frac{1-\cos 2x}{2} $$
    - cos
        $$ \cos^2 x = \frac{1+\cos 2x}{2} $$
- 加法定理
    # $$ \left( \begin{matrix} \cos \alpha + \beta\\ \sin \alpha + \beta \end{matrix} \right)
    \left( \begin{matrix} \cos \alpha \cos \beta - \sin \alpha \sin \beta\\ \cos \alpha \sin \beta + \sin \alpha \cos \beta \end{matrix} \right) $$
    # $$ \left( \begin{matrix} \cos \alpha - \beta\\ \sin \alpha - \beta \end{matrix} \right)
    \left( \begin{matrix} \cos \alpha \cos \beta + \sin \alpha \sin \beta\\ -\cos \alpha \sin \beta + \sin \alpha \cos \beta \end{matrix} \right) $$
    - proof
        # $$ \left( \begin{matrix} \cos \alpha\\ \sin \alpha \end{matrix} \right)
        \left( \begin{matrix} 1 & 0\\ 0 & 1 \end{matrix} \right) \left( \begin{matrix} \cos \alpha\\ \sin \alpha \end{matrix} \right) $$
        \beta回転すると
        # $$ \left( \begin{matrix} \cos \alpha + \beta\\ \sin \alpha + \beta \end{matrix} \right)
        # \left( \begin{matrix} \cos \alpha & \sin \alpha \end{matrix} \right) \left( \begin{matrix} \cos \beta & \sin \beta\\ -\sin \beta & \cos \beta \end{matrix} \right)
        \left( \begin{matrix} \cos \alpha \cos \beta - \sin \alpha \sin \beta\\ \cos \alpha \sin \beta + \sin \alpha \cos \beta \end{matrix} \right) $$
        -\beta回転すると
        # $$ \left( \begin{matrix} \cos \alpha + \beta\\ \sin \alpha + \beta \end{matrix} \right)
        \left( \begin{matrix} \cos \alpha & \sin \alpha \end{matrix} \right) \left( \begin{matrix} \cos (-\beta) & \sin (-\beta)\\ -\sin (-\beta) & \cos (-\beta) \end{matrix} \right) \\ = \left( \begin{matrix} \cos \alpha & \sin \alpha \end{matrix} \right) \left( \begin{matrix} \cos \beta & -\sin \beta\\ \sin \beta & \cos \beta \end{matrix} \right) \\ = \left( \begin{matrix} \cos \alpha \cos \beta + \sin \alpha \sin \beta\\ -\cos \alpha \sin \beta + \sin \alpha \cos \beta \end{matrix} \right) $$
- 積和公式
    - sin cos
        $$ \sin A \cos B = \frac{1}{2} [\sin (A+B)+\sin(A-B)] $$
    - cos sin
        $$ \cos A \sin B = \frac{1}{2} [\sin (A+B)-\sin(A-B)] $$
    - cos cos
        $$ \cos A \cos B = \frac{1}{2} [\cos (A+B)+\cos(A-B)] $$
    - sin sin
        $$ \sin A \sin B = \frac{1}{2} [\cos (A-B)-\cos(A+B)] $$
- 近似
- 三角置換
- other
    - versin 正矢 versed sine
        $$ 1-\cos $$
    - coversin 余矢 coversed sine
        $$ 1-\sin $$
    - vercos versed cosine
        $$ 1+\cos $$
    - covercos coversed cosine
        $$ 1+\sin $$
    - exsec exterior secant
        $$ \sec -1 $$
    - excosec exterior cosecant
        $$ \cosec -1 $$
    - crd chord
        $$ \frac{1}{2}\sin \frac{1}{2}x $$
- 八線
    sin
    tan
    sec
    cos
    cot
    cosec
    versin
    coversin