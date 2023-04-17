``` python
import os

# specify the path to the vault's folder
root_dir = "D:/Obsidian vaults/Master's thesis/Literature"

# reads in all documents and their content, searches for an expression and
# replaces with a different one
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r") as f:
                contents = f.read()
            updated_contents = contents.replace("\\Master's%20thesis\\", "\\Masters%20thesis\\")
            with open(filepath, 'w') as f:
                f.write(updated_contents)
```
