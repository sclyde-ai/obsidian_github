---
alias:
    ['docker_file']
---
# template
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
# instructions
FROM : imageを指定する <- 最低限必要なのはこれだけ
LABEL : metadataを追加する
RUN : image構築時にcommandを実行する
WORKDIR : 作業directoryを設定する
COPY : hostのfileやdirectoyをcopyする
CMD : container起動時にcommandを実行する
EXPOSE : containerがlistenするportを指定する
ENV : 環境変数を設定する
VOLUME : 永続化directoryを設定する
# tips
- 詳細なerror確認
    environment:
        - PYTHONUNBUFFERED=1
- docker-entrypoint-initdb.d
    初回起動時のみ実行される