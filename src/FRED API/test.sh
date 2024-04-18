#!/bin/bash
# IFS=$'\n'
cd fred_api_files
lines=$(ls -la)
echo $(pwd)
echo $(python --version)    
for line in ${lines}; do
#     line = '0_1_fredCall.py'
    echo "hello ${line}"
#     echo "$(python 0_1_fredCall.py)"
#     python ${line}
#     vim a.txt
done
# IFS=""
exit 0
