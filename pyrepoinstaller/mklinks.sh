sed -n 's|^Filename: |https://archive.ubuntu.com/ubuntu/|p' Packages > links.txt

# THEN RUN THE downloader.py

echo "press enter to start downloading the repository"
read a

python3 downloader.py # defaults download to ~/local_repo/

#!!!CHANGE THIS IF you changed the download directory in downloader.py!!!
downloadDirectory="~/local_repo/"
cd downloadDirectory

#comment this if you want to host using another service
sudo python3 -m http.server 80