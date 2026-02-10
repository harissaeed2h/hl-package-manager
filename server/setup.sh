cd pyrepoinstaller

sed -n 's|^Filename: |https://archive.ubuntu.com/ubuntu/|p' Packages > links.txt

# THEN RUN THE downloader.py

echo "press enter to start downloading the repository"
read a

python3 downloader.py # defaults download to ~/local_repo/

#!!!CHANGE THIS IF you changed the download directory in downloader.py!!! NOT RECOMMENDED TO CHANGE
#-->INSTEAD PUT A LINK TO THE DESTINATION FOLDER INTO HOME AND NAME IT local_repo<--#
cd ../local_repo
downloadDirectory="$HOME/local_repo/"
cp repolist_gen.py $downloadDirectory
cd $downloadDirectory
python3 repolist_gen.py

#comment this if you want to host using another service
sudo python3 -m http.server 80