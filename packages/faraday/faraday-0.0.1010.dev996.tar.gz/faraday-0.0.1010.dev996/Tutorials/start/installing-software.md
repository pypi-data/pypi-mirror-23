# Installing Faraday Software
The open source software provided by FaradayRF is primarily written in Python. Any language capable of interfacing with a serial port could be used. However, we chose Python 2.7 due to it's ease of learning and cross-platform capabilities.

Please note that no testing has been performed with Python 3 at this time. If you do, please let us know!

## Installing Python 2.7
### Windows
 * The Hitchhiker's Guide To Python: [Installing Python on Windows](http://docs.python-guide.org/en/latest/starting/install/win/)
 
### Linux (Debian-based)
Most distributions come with Python preinstalled, however if not please read the [Python Documentation](https://docs.python.org/2/using/unix.html#getting-and-installing-the-latest-version-of-python)
 
#### Installing Pip
If you are using Debian 8 you will need to install pip.
 * ```sudo apt-get install python-pip```

#### Mac OS X
 * Follow The Hitchhiker's Guide to Python [Installing Python on Max OS X](http://docs.python-guide.org/en/latest/starting/install/osx/)
  * XCode
  * Homebrew
  * Python 2.7
  * Setuptools
  * Pip
  * Optional: Virtual Environments

 > A basic version of Git comes on OS X. Apple Git-50.3 was used to write this guide but consider upgrading it or installing the official Git for OS X.
 
##Cloning the Faraday-Software Repository
If you want to be able to develop with Faraday Software then we suggest cloning our Git Repository as described here. If you just want to run the latest sofware then downloading a zip of our repository will suffice.

###Windows
> Skip to "Zip File Installation" if you do not plan on forking/commiting new code to GitHub

The open-source software is provided on our GitHub repository. If you plan on developing software you should [install GIT](https://git-scm.com/) on your computer. This guide assumes Git is installed with Git Bash.

Using Git Bash (right-click|Git Bash here) this example will be relative to wherever you start bash:

 1. Create a suitable folder for Faraday software. I.e. `mkdir -p git/faradayrf`
 2. Navigate to the new folder `cd git/faradayrf`
 3. Clone the lastest master branch `git clone https://github.com/FaradayRF/Faraday-Software.git software`
 4. Navigate to the software `cd software`
 5. Now that you've downloaded Faraday Software, [Install Python packages](installing-software.md#installing-required-python-packages)

###Linux (Debian-Based)
> Skip to "Zip File Installation" if you do not plan on forking/commiting new code to GitHub

 1. Create suitable folder for Faraday software. I.e. ```mkdir -p git/faradayrf```
 2. Navigate to the new folder ```cd git/faradayrf```
 3. Clone latest master branch ```git clone https://github.com/FaradayRF/Faraday-Software.git software```
 4. Navigate to the software `cd software`
 5. Now that you've downloaded Faraday Software, [Install Python packages](installing-software.md#installing-required-python-packages)

Latest Master: https://github.com/FaradayRF/Faraday-Software.git

###Mac OS X
> Skip to "Zip File Installation" if you do not plan on forking/commiting new code to GitHub

 1. Create suitable folder for Faraday software. I.e. ```mkdir -p git/faradayrf```
 2. Navigate to the new folder ```cd git/faradayrf```
 3. Clone latest master branch ```git clone https://github.com/FaradayRF/Faraday-Software.git software```
 4. Navigate to the software `cd software`
 5. Now that you've downloaded Faraday Software, [Install Python packages](installing-software.md#installing-required-python-packages)

Latest Master: https://github.com/FaradayRF/Faraday-Software.git

###Zip File Installation
####Windows
> Unnecessary if Git repository was cloned

This method will download the latest stable software in a Zip archive. It is not able to push code back into GitHub.
 1. Download the [Faraday Software Zip](https://github.com/FaradayRF/Faraday-Software/archive/master.zip)
 3. Create two new folders `faradayrf/software` and extract the archive to this location
 4. Navigate to your unzipped file `C:\faradayrf\software`
 5. [Install Python packages](installing-software.md#installing-required-python-packages)
 
####Linux (Debian-Based)
> Unnecessary if Git repository was cloned

This method will download the latest stable software in a Zip archive. It is not able to push code back into GitHub.
 1. Download the [Faraday Software Zip](https://github.com/FaradayRF/Faraday-Software/archive/master.zip)
 2. Open zip with Archive Manager
 3. Create two new folders ```faradayrf/software``` and extract the archive to this location
 4. In terminal ```cd faradayrf/software```
 5. [Install Python packages](installing-software.md#installing-required-python-packages)
 
####Mac OS X
> Unnecessary if Git repository was cloned
***Not Verified, OS X zip files not native***
This method will download the latest stable software in a Zip archive. It is not able to push code back into GitHub.
 1. Download the [Faraday Software Zip](https://github.com/FaradayRF/Faraday-Software/archive/master.zip)
 2. Open zip with Archive Manager
 3. Create two new folders ```faradayrf/software``` and extract the archive to this location
 4. In terminal ```cd faradayrf/software```
 5. [Install Python packages](installing-software.md#installing-required-python-packages)

##Installing Required Python Packages
###Windows
Use the requirements.txt file to install all necessary packages in one command.

 ```pip install -r requirements.txt```
 
###Linux (Debian-based)
Use the requirements.txt file to install all necessary packages in one command.

```sudo pip install -r requirements.txt```

You must use sudo to ensure you have permission to install all necessary packages.

###Mac OS X
Use the requirements.txt file to install all necessary packages in one command.

```pip install -r requirements.txt```
 
You may need to have administrative privileges to install this. Likely you already do from installing Python 2.7

# Plugging Faraday in
Congratulations! Making it this far means that you're so close to using Faraday. However we need to [plug in the Faraday hardware](connecting-hardware.md) and complete configuration. Two quick steps.
