import os
import datetime

size_in_bytes = os.path.getsize("novel_new.txt")
print(size_in_bytes)
last_modified = os.path.getmtime("novel_new.txt")
print(last_modified)

timestamp = last_modified
new_time = datetime.datetime.fromtimestamp(timestamp)
print(new_time)

absolute_path = os.path.abspath("guest.txt")
print(absolute_path)

