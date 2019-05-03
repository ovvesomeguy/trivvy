#!/bin/bash

# delete symbolic link
if [ -L '/usr/local/bin/trivvy' ]; then rm /usr/local/bin/trivvy; echo 'the symbilic link was deleted'; fi
# delete the project
if [ -d '/usr/local/lib/python3.6/dist-packages/trivvy' ]; then rm -rf /usr/local/lib/python3.6/dist-packages/trivvy/; echo 'the folder was deleted'; fi
# write in log file update news
# exec 1> 
echo '| I`ve been updated |'>$HOME/.trivvy/logger/logger.log

cp -r ~/trivvy/ /usr/local/lib/python3.6/dist-packages/
ln -s /usr/local/lib/python3.6/dist-packages/trivvy/src/core/entry.py /usr/local/bin/trivvy
chmod 777 /usr/local/bin/trivvy

echo 'Build was complete'
