max_depth=$(find . -type d | awk -F/ '{print NF-1}' | sort -n | tail -1)
for ((i=$max_depth; i>=1; i--)); do
    find . -mindepth $i -type f -exec mv -n -t . {} +
done
