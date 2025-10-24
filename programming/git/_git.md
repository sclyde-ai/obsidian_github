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
- notice 注意事項
	- gitコマンドはgitからcloneしたものにしか効果がない
	- git repositoryに反映されないファイル
		1. 未追跡file
		2. 変更されたがstageされてないfile
		3. stageされたがcommitされてないfile
# useful command
- git push by time to push 
    git add . && git commit -m "$(date '+%Y/%m/%d %H:%M:%S')" && git push
- branchを作成して切り替える
    git checkout -b $1 
- remoteのbranchを削除する
    git push origin --delete [name]
-  もとから存在するfileをgitignoreする
	git rm --cached