if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "obsidian://open?vault=obsidian_github"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    xdg-open "obsidian://open?vault=obsidian_github"
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
    cmd.exe /C "start obsidian://open?vault=obsidian_github"
else
    echo "error: this OS is not supported"
fi