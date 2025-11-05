# class
- np.ndarray

# making vector
- np.array(object)
    objectのnumpyを作成する
- np.zeros(shape)
    shapeの大きさの0の要素のみの行列を作成する
- np.ones(shape)
    shapeの大きさの1の要素のみの行列を作成する
- np.identity(n), np.eye(n)
    n行n列の単位行列を作成する
- np.full(shape, value)
    shapeの大きさのvalueの要素のみの行列を作成する
- np.arange(start, stop, step)
    startからstopまでstepずつ増える配列を作成する
- np.random.rand(shape)
    shapeの大きさの乱数行列を作成する
# operation function
- +
    足し算
- -
    引き算
- *
    要素ごとの掛け算
- /
    要素ごとの割り算
- @
    行列の掛け算（内積）
- .T
    転置する
- np.dot(A, B)
    A@B
- 
