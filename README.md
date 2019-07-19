# sonarr-importer

This is a really simple script that 'fixes' sonarr's terrible automatic importer thingy. This script gets a list of files in a folder (In my case /media/downloads_completed), and then submits a manual import request to sonarr.

I have deluge setup to automatically move my downloads to the downloads_completed folder when downloading is finsihed, then it executes this script, which imports it into sonarr and moves/renames it and puts it in my correct TV show folder.

Anyways, hopefully this helps someone not be as frustrated with the stupid Completed Download Handling never, ever working. And it also is better than the drone folder, because it actually moves the files, and no just creates a hardlink.
