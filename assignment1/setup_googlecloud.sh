#!/usr/bin/env bash

# This is the set-up script for Google Cloud.
# This script sets up python3 on Ubuntu
sudo apt-get update
sudo apt-get install libncurses5-dev
sudo apt-get install python3-dev
sudo apt-get install python3-pip
sudo apt-get install libjpeg8-dev
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo pip3 install --upgrade pip
sudo pip3 install pillow
sudo apt-get build-dep python3-imaging
sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
sudo pip3 install virtualenv  
# Working for conda python
# conda install virtualenv 
virtualenv --python=python3 .env                  # Create a virtual environment
source .env/bin/activate         # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies
pip install --upgrade jupyterthemes # Cooler jupyter
deactivate
echo "**************************************************"
echo "*****  End of Google Cloud Set-up Script  ********"
echo "**************************************************"
echo ""
echo "If you had no errors, You can proceed to work with your virtualenv as normal."
echo "(run 'source .env/bin/activate' in your assignment directory to load the venv,"
echo " and run 'deactivate' to exit the venv. See assignment handout for details.)"
