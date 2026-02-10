# hl-package-manager
This is a local package manager, haris local package manager (hlpm), this package can install packages from a local server, its goal is to replace apt for locally run package managers as apt repositories entirely are massive, it  assumes the packages downloaded are safe to run, BUILT FOR LOCAL INTRANETS in case of blackouts.

This package manager is built to install packages when apt demands hashes, it can be used instead if you want to build an intra net at a low budget.

**HOW TO USE**
1) Place the local_repo folder in your home directory, **if you want to put it elsewhere, please change localRoot in pyrepoinstaller/downloader.py and downloadDirectory in mklinks.sh**
2) Place hlpm at any location or used a compiled version and place it in /usr/bin/

**THIS PACKAGE IS STILL UNDER WORK, INSTALLERS MAY NOT WORK RIGHT, YOU MAY NEED TO SET IT UP MANUALLY**
