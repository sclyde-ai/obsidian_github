if [ $# -eq 0 ]; then
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open "obsidian://open"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        xdg-open "obsidian://open"
    elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
        cmd.exe /C "start obsidian://open"
    else
        echo "error: this OS is not supported"
    fi
else
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open "obsidian://open?vault=obsidian_github"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        xdg-open "obsidian://open?vault=obsidian_github"
    elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
        cmd.exe /C "start obsidian://open?vault=obsidian_github"
    else
        echo "error: this OS is not supported"
    fi
fi