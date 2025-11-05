---
alias:
    ['jupyter']
---
# 環境構築
1. venv作成
```
python -m venv venv
```
2. activate
	```
	# linux & mac
	source venv/bin/activate
	```
	```
	# windows
	.\venv\Scripts\activate
	```
2. install ipykernel
```
pip install jupyter ipykernel
```
3. registar
```
python -m ipykernel install --user --name="computational_finance"
```
3. install
```
pip install -r requirements.txt
```
## image
- jupyter/base-notebook : basic 
- jupyter/scipy-notebook :base-notebook + NumPy, SciPy, pandas, Matplotlib
- jupyter/datascience-notebook : scipy-notebook + scikit-learn, R, Julia
- jupyter/tensorflow-notebook : s cipy-notebook +TensorFlow, Keras
- jupyter/pytorch-notebook : scipy-notebook + PyTorch