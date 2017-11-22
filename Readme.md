
# Setup
* Install python3: `sudo apt-get install python3`
* Install virtual env:
    ```bash
    cd assignment1
    sudo pip install virtualenv      # This may already be installed
    virtualenv -p python3 .env       # Create a virtual environment (python3)
    # Note: you can also use "virtualenv .env" to use your default python (usually python 2.7)
    source .env/bin/activate         # Activate the virtual environment
    pip install -r requirements.txt  # Install dependencies
    # Work on the assignment for a while ...
    deactivate                       # Exit the virtual environment
    ```
    Or just `cd assignmentx && bash setup_googlecloud.sh` to setup all things including jupyter. If your default `python` is installed via `conda`. Then replace the `pip install virtualenv` with the `conda install virtualenv`
* Download data
    ```bash
    cd assignmentx/cs231n/datasets
    ./get_dataset.sh
    ```
* Start IPython
    ```bash
    jupyter notebook
    ```
* Change `pip` repository
    ```
    vim ~/.pip/pip.config
    [global]
    index-url = http://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host = mirrors.aliyun.com
    ```
* Change `conda` repository
    ```
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes
    ```
* Install *env* via `conda`
    ```
    conda create -n yourenvname python=x.x anaconda
    source activate yourenvname
    conda install -n yourenvname [package]
    source deactivate
    conda remove -n yourenvname -all
    conda install -n yourenvname --file requirements.txt
    ```

# Git

    # Always edit the most recent commit
    git commit --amend 
    # The remote may reject this commit
    git push --force 