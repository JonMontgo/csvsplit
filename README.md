# CSV Split

## Install
Run `pip install .` or `pip3 install .`. Make sure you use the pip associated 
with python3.

## Usage
simply type in `csvsplit -h` to see all of the options that csvsplit supports.

#### Example Usage
```bash
csvsplit -c 100 foo.csv
```
This will split `foo.csv` into parts with 100 lines each. The chunked files
will follow naming conventions of 
`{full_path_wo_ext}_chunk_{chunk_num}{extension}`
So if `foo.csv` was 198 lines long... 
```
./foo_chunk_1.csv
./foo_chunk_2.csv
``` 
