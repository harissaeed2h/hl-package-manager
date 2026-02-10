# hl-package-manager
This is a local package manager, haris local package manager (hlpm), this package can install packages from a local server, its goal is to replace apt for locally run package managers as apt repositories entirely are massive, it  assumes the packages downloaded are safe to run, BUILT FOR LOCAL INTRANETS in case of blackouts.

This package manager is built to install packages when apt demands hashes, it can be used instead if you want to build an intra net at a low budget.

**HOW TO USE**
1) **Go to the server folder and execute the setup.sh file on the server**, this will setup the repository by downloading the main branch of noble, you may change the Packages file to contain whatever packages you may want. You can also remove the python server from the file and use another service like apache or nginx as well.
2) **Execute the main.py file on the client side, change variables in config.py as required** default server address is localhost:80

**This is all, the server is up and running and you can install packages using hlpm locally**

**<span style="color: #F39C12;">WARNING, USE THIS PROGRAM IF YOU ARE SURE THE SERVER HOLDS LEGITEMATE PACKAGES AS THIS PROGRAM IS BUILT FOR CLOSED INTRANETS WITH LIMITED STORAGE AND RESOURCES HENCE THIS PROGRAM IS NOT A PERFECTIONIS AND MEANT FOR PURE PERFORMANCE AND EASE OF USE</span>**