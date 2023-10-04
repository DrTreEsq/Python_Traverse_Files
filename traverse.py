# The os module is perfect for filesystem operations like "walking" throught directories and files
import os

# Although there are many ways of achieving the same effect, a good way to loop over the filesystem is using `os.walk()`
# Update the loop so that it shows the absolute path of a file ignoring directories which we aren't going to track
for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        print(f"File found: {full_path}")
        
# Make your Python script accept an argument to traverse any path (don't hardcode the path!)
# Use different options in the script for reporting, like:
# No more than 20 files, & Files larger than a specific size in megabytes
