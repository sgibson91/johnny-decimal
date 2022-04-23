# The Johnny Decimal File System

A set of Python scripts to assist with organising files into the Johnny Decimal system - https://johnnydecimal.com/

## Scripts

- [`01a-list-files.py`](01a-list-files.py)
- [`01b-list-dirs.py`](01b-list-dirs.py)
- [`02-make-jd-dirs.py`](02-make-jd-dirs.py)
- [`03-move-files.py`](03-move-files.py)
- [`04-delete-files.py`](04-delete-files.py)
- [`05-clean-up.py`](05-clean-up.py)

### `01a-list-files.py`

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

**Command line usage:**

```bash
usage: python 05-clean-up.py [-h] target_path

Remove empty directories from a path's tree

positional arguments:
  target_path  Path under which to delete empty folders

optional arguments:
  -h, --help   show this help message and exit
```
