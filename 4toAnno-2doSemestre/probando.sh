#!/bin/bash
script_to_run="./shrinkpdf.sh"
# Iterate through all .pdf files in the current folder

# Iterate through all .pdf files in the current folder and subfolders
find . -type f -name "*.pdf" | while read -r file; do
    # Ensure it's a file and not the script itself
    if [[ "$file" != "$script_to_run" ]]; then
        # Get the filename without the path
        filename=$(basename "$file")
        directory=$(dirname "$file")
        
        # Prepend "1" to the filename for the output
        output_file="${directory}/1${filename}"
	echo $output_file
        
        # Run the script with: -r60 -o output_file input_file
        "$script_to_run" -r 150 -o "$output_file" "$file"
    fi
done

# Delete all original .pdf files that don't start with '1' in the current folder and subfolders
find . -type f -name "*.pdf" | while read -r file; do
    filename=$(basename "$file")
    if [[ $filename != 1* ]]; then
        rm "$file"  # Remove original PDF files
    fi
done

# Rename remaining files by removing the leading '1' in the current folder and subfolders
find . -type f -name "1*.pdf" | while read -r file; do
    filename=$(basename "$file")
    directory=$(dirname "$file")
    new_filename="${filename:1}"  # Remove the first character ('1')
    mv "$file" "${directory}/${new_filename}"  # Rename the file
done

