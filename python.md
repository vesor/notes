## Profiling
https://ymichael.com/2014/03/08/profiling-python-with-cprofile.html

## PyCharm
Avoid indexing by right click the file and exclude it from source.
It seems has bug if fold is recognized as lib, for example in facebook detectron code it will try to index lib/datasets even that fold has been set as excluded.
The workaround is in File->Settings->Editor->File Types. Add "\*.jpg;\*.png;\*.pkl;..." to "Ignore files and folders" 
