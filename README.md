# The Johnny Decimal File System

A set of Python scripts to assist with organising files into the Johnny Decimal system - <https://johnnydecimal.com/>

## Scripts

- [`01a-list-files.py`](01a-list-files.py)
- [`01b-list-dirs.py`](01b-list-dirs.py)
- [`02-make-jd-dirs.py`](02-make-jd-dirs.py)
- [`03-move-files.py`](03-move-files.py)
- [`04-delete-files.py`](04-delete-files.py)
- [`05-clean-up.py`](05-clean-up.py)

### `01a-list-files.py`

This script walks the tree of a provided dictionary and generates a list of all the files beneath it.
The script outputs a CSV file with the following columns:

- Filepath (str): The path to a given file
- Filename (str): The name of a given file
- Area (str): A placeholder for the Johnny Decimal area name
- Category: A placeholder for the Johnny Decimal category name
- Delete (bool): Whether or not the file should be deleted. Defaults to False.

After generating the CSV file, the user should inspect the CSV file and do the following tasks:

- Mark any files for deletion by changing the value of the Delete column to True
- Organise the remaining files by assigning them to areas and categories within each area

:sparkles: **Note:** The Johnny Decimal system recommends no more than 10 areas, and no more than 10 categories per area :sparkles:

**Command line usage:**

```bash
usage: python 01a-list-files.py [-h] [-o OUTPUT] target_path

List the files in a specified directory and generate a CSV file.

positional arguments:
  target_path           Path to the target directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output CSV file of filepaths
```

### `01b-list-dirs.py`

This script is functionally the same as [`01a-list-files.py`](#01a-list-filespy), but instead returns the lowest nested subdirectory instead of files.
This can be useful if a tree contains a large number of files or the files do not have helpful names.

**Command line usage:**

```bash
usage: python 01b-list-dirs.py [-h] [-o OUTPUT] target_path

List the lowest subdirectories in a specified directory and generate a CSV file.

positional arguments:
  target_path           Path to the target directory

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output CSV file of subdirectory filepaths
```

### `02-make-jd-dirs.py`

After organising the files according to the Johnny Decimal system and updating the CSV file accordingly, this script will make all the folders for your new Johnny Decimal organisation system under your chosen directory.
The area and category names will be pulled from the CSV file and they will be ordered alphabetically before their numbers are assigned.
Hence, sorting your folders numerically or alphabetically will yield the same sort.

**Command line usage:**

```bash
usage: python 02-make-jd-dirs.py [-h] [-i INPUT] target_path

Create Johnny Decimal folder structure from a list of categorised files

positional arguments:
  target_path           Path under which to create the Johnny Decimal structure

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input CSV file of categorised files
```

### `03-move-files.py`

Once your Johnny Decimal filesystem has been generated by [step 2](#02-make-jd-dirspy), this script will move any files not makred for deletion into the correct Johnny Decimal subfolder based on their assignment in the CSV file.

Note that this script will not rename files - that must be done manually.

**Command line usage:**

```bash
usage: python 03-move-files.py [-h] [-i INPUT] [--purge] target_path

Move files into a Johnny Decimal folder structure from a list of categorised files

positional arguments:
  target_path           Path under which the Johnny Decimal structure exists

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input CSV file of categorised files
  --purge               Delete files marked for removal
```

### `04-delete-files.py`

This script will delete any files marked for deletion as defined by having the value True in the delete column of the CSV file.

**Command line usage:**

```bash
usage: python 04-delete-files.py [-h] [-i INPUT]

Delete files from a list of categorised files

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input CSV file of categorised files
```

### `05-clean-up.py`

Once all of your files have been moved or deleted, there may be some orphan directories left over.
This script walks down your chosen directory tree and deletes any empty subdirectories it finds.

**Command line usage:**

```bash
usage: python 05-clean-up.py [-h] target_path

Remove empty directories from a path's tree

positional arguments:
  target_path  Path under which to delete empty folders

optional arguments:
  -h, --help   show this help message and exit
```
