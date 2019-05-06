#!/bin/bash

# delete symbolic link
if [ -L '/usr/local/bin/trivvy' ]; then rm /usr/local/bin/trivvy; echo 'The symbilic link was deleted>'; fi
# delete the project
if [ -d '/usr/local/lib/python3.6/dist-packages/trivvy' ]; then rm -rf /usr/local/lib/python3.6/dist-packages/trivvy/; echo 'The folder was deleted>'; fi
# write in log file update news
# (date +%F_%H-%M-%S)
echo `date +%T:%D` "
 |---------------------|
 | I have been updated |
 |---------------------|">$HOME/.trivvy/logger/logger.log

cp -r ~/trivvy/ /usr/local/lib/python3.6/dist-packages/
ln -s /usr/local/lib/python3.6/dist-packages/trivvy/src/core/__main__.py /usr/local/bin/trivvy
chmod 777 /usr/local/bin/trivvy

echo '\033[32mBuild was complete\033[0M'
