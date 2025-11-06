---
alias:
    ['git']
---
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

-  