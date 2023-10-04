# The os module is perfect for filesystem operations like "walking" throught directories and files
import os


file_metadata = {}
# Although there are many ways of achieving the same effect, a good way to loop over the filesystem is using `os.walk()`
for root, directories, files in os.walk('.'):
    for _file in files:
        # Update the loop so that it shows the absolute path of a file ignoring directories which we aren't going to track
        full_path = os.path.join(root, _file)
        # Update the loop to include the file size
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size
        print(f"Size: {size}b - File: {full_path}")
        # Persist the data into a dictionary. Since file paths are unique you can use those as dictionary keys
print(file_metadata)

# **Exercise:** Now that the metadata is captured and stored in a suitable data structure like a dictionary, report back the results with only the four largest files.
# Try using other quantities to report on, like the 10 largest files instead of 4.
items_shown = 0
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if items_shown > 20:
        break
    print(f"Size: {size} Path: {path}")
    items_shown += 1
        
        
# Make your Python script accept an argument to traverse any path (don't hardcode the path!)
# Use different options in the script for reporting, like:  No more than 20 files, & Files larger than a specific size in megabytes
