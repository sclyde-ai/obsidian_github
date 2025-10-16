1. 報酬関数/誤差関数を決める
2. 使う関数を決める
3. 報酬関数/誤差関数を最大化するパラメータを探す(学習)
- 模型評価 model assessment/evaluation
    - 汎用性/汎化性能 generalization
        未知の新しいデータに対しても正確な予測や分類を行える能力
    - 過学習 overfitting
        機械学習モデルが訓練データに過剰に適合し、その結果として未知のデータ（検証データ）に対する予測精度が低下してしまう現象
- problem
    - 勾配消失 vanishing gradient
    - no free lunch theorem
        汎用性と最適性は両立不可能
    - 幻覚 hallucination
        事実でない情報や存在しない情報を本物のように出力すること
    - Potemkin understanding
- prompt engineering
    生成AIに期待通りの正確な回答やコンテンツを生成させるために、prompt (AIへの指示文) を設計・最適化する技術や手法
- model tuning/hyper-parameters tuning 模型調整
    - hyper-parameter
    - fine tuning
    - grid search
    - random search
- swarm AI 群集合人口知能
- pre-training
- post-training