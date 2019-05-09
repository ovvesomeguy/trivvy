#!/bin/bash

# delete symbolic link
if [ -L '/usr/bin/trivvy' ]
then 
    rm /usr/bin/trivvy; echo 'The symbilic link was deleted>' 
fi

# delete the project
if [ -d '/usr/lib/python3/dist-packages/trivvy' ]
then
    rm -rf /usr/lib/python3/dist-packages/trivvy/; echo 'The folder was deleted>' 
else
    mkdir /usr/lib/python3/dist-packages/trivvy/;
fi


cp -r $PWD /usr/lib/python3/dist-packages/
ln -s /usr/lib/python3/dist-packages/trivvy/src/core/__main__.py /usr/bin/trivvy
chmod 777 /usr/bin/trivvy

echo '\033[32m Build was complete \033[0M'
echo `date +%T:%D` "
 |---------------------|
 | I have been updated |
 |---------------------|">$HOME/.trivvy/logger/logger.log
