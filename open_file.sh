files_array=(*$1*)

for file in "${files_array[@]}"; do
    echo $file
    code "$file"
done