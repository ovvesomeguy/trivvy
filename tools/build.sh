if [ -L '/usr/local/bin/trivvy' ]; then rm /usr/local/bin/trivvy; echo 'the symbilic link was deleted'; fi
if [ -d '/usr/local/lib/python3.6/dist-packages/trivvy' ]; then rm -rf /usr/local/lib/python3.6/dist-packages/trivvy/; echo 'the folder was deleted'; fi

cp -r ~/trivvy/ /usr/local/lib/python3.6/dist-packages/
ln -s /usr/local/lib/python3.6/dist-packages/trivvy/src/__main__.py /usr/local/bin/trivvy
chmod 777 /usr/local/bin/trivvy

echo 'Build was complete'
