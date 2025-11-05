---
alias:
    ['docker_compose']
---
# docker compose
    -f : docker-compose.ymlの名前を指定する
## docker compose up
    build + run
    --build : imageを構築する（編集後に使う）
    -d/--detached : container起動後にterminalが解放されて利用できる
## docker compose down 
    -v/--volumes : volumeも削除する（database初期化）
## docker compose build
## docker compose run
## docker compose logs
## docker compose exec
# useful command 
    docker compose exec -T db psql -U user -l
    docker compose exec db psql -U user -d <database>