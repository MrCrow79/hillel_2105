from pathlib import Path


cur_dirt = Path(Path.cwd())  # Path('D:\hillel\pythonProject\hillel_2105\lessons\lesson_12')

parent_dir = cur_dirt.parent
print(parent_dir.name)
print(parent_dir.absolute())

sibling_folders = [k.absolute() for k in parent_dir.iterdir() if k.is_dir()]
sibling_files = [k.absolute() for k in parent_dir.iterdir() if k.is_file()]

for k in sibling_folders:
    print(k)
for k in sibling_files:
    print(k)


# create dir
new_folder_2 = Path(parent_dir / 'new_folder' / 'new_folder_2')
new_folder_3 = Path(parent_dir / 'new_folder' / 'new_folder_3')
print(new_folder_2.absolute())
new_folder_2.mkdir(exist_ok=True, parents=True)
new_folder_3.mkdir(exist_ok=True, parents=True)

file_path = new_folder_2 / 'some_file.txt'

with open(file_path.absolute(), 'a') as f:  # for..:, while..:, def some():
    pass  # create file


new_folder_3.rmdir()  # delete folder
file_path.unlink(missing_ok=True)  # delete file
