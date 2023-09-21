import shutil

# Specify the file or directory path
file_or_dir_path = '/path/to/your/file_or_directory'

# Specify the user and group you want to assign ownership to
user = 'username'  # Replace 'username' with the actual username
group = 'groupname'  # Replace 'groupname' with the actual groupname

# Use shutil.chown to change ownership
shutil.chown(file_or_dir_path, user=user, group=group)


