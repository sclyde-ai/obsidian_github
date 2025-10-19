        - local
            - index(staging area)
            - working directory
            - local repository
                - master(main branch)
                - branch
        - remote
            - origin(remote repository)
                - master
                    main branchのdefault名
                - branch
        - command
            - git pull
                fetch+merge
            - git fetch
                remote master branchの状態をlocal origin/master branchへ適応
                | —all |  |
                | --- | --- |
                |  |  |
                |  |  |
            - git merge
                local origin/masterの状態をlocal master branchへ適応
            - git push
                local repositoryの状態をremote repositoryに適応
                | —force | 強制的にpush |
                | --- | --- |
                | —force-with-lease | 予期しない変更が存在したら失敗 |
                |  |  |
            - git add
                indexに変更をstage
            - git commit
                indexの状態をlocal repositotyに適応
            - git clone
                remote repositoryの状態をlocal repositoryに適応
            - git init
                current directoryをgit repositoryとして設定
            - git remote
                | -v |  |
                | --- | --- |
                |  |  |
                |  |  |
            - git branch
                branch 一覧表示
                | -r/-remote | remote branch表示 |
                | --- | --- |
                | -a/-all |  |
                | —merged |  |
            - git checkout
                branch切り替え
            - git clean
                追跡されてないファイルを削除
            - git config
            - git log
                 過去ログ確認
            - git status
                状態確認 
            - git stash
            - git ls-files
                - -o/—others
                - -i/—ignored
                - —exclude-standard
            - git show
            - git reset
                | —hard |  |
                | --- | --- |
                |  |  |
                |  |  |
            - git revert
            - git log
                | —online |  |
                | --- | --- |
                | —graph |  |
                | —all |  |
        - notice 注意事項
            - gitコマンドはgitからcloneしたものにしか効果がない
            - git repositoryに反映されないファイル
                1. 未追跡file
                2. 変更されたがstageされてないfile
                3. stageされたがcommitされてないfile
        - shortcut
# command
- git revert
    -no-commit: 
# useful command
- git push by time to push 
    git add . && git commit -m "$(date '+%Y/%m/%d %H:%M:%S')" && git push
- branchを作成して切り替える
    git checkout -b $1 
- remoteのbranchを削除する
    git push origin --delete [name]
-  もとから存在するfileをgitignoreする
	git rm --cached