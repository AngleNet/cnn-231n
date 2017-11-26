
# Setup
* Install python3: `sudo apt-get install python3`
* Install virtual env:
    ```bash
    cd assignment1
    bash setup_googlecloud.sh       # Setup python3 
    source .env/bin/activate        
    deactivate                      # Exit virtualenv
    ```
* Download data
    ```bash
    cd assignmentx/cs231n/datasets
    ./get_dataset.sh
    ```
* Start Jupyter 
    ```bash
    cd assignment1 && source .env/bin/activate
    touch jupyter_notebook_config.py    
    # Add the following to it:

    # The IP address the notebook server will listen on.
    c.NotebookApp.ip = ''  
    # Hashed password to use for web authentication.                                                                                  
    # To generate, type in a python/IPython shell:
    #   from notebook.auth import passwd; passwd()
    # The string should be of the form type:salt:hashed-password.
    c.NotebookApp.password = ''
    c.NotebookApp.open_browser = False

    jupyter notebook            # Start Jupyter from the same directory
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
* `pip` utilities
    ```
    pip3 install --upgrade pip
    pip3 install {package name}
    pip3 install pip-autoremove
    pip-autoremove {package name} -y  # Delete the package and all its dependencies
    ```

* **jupyter themes**
    ```
    pip install --upgrade jupyterthemes
    jt -t chesterish -T -N -dfonts -altout -nf 8 -lineh 130
    ```

* Debug jupyter
    ```
    import IPython.core.debugger as debugger
    def func():
        for i in range(3):
            debugger.set_trace()
    func() # Now we can step into func
    ```

# Git

    # Always edit the most recent commit
    git commit --amend 
    # The remote may reject this commit
    git push --force 
    # Generate patch from the changed file
    git diff knn.ipynb > knn.patch
    # Patch
    git apply knn.patch
    # Combine multiple commits
    git rebase -i COMMIT_ID

# Useful links
* [Latex symbols](https://www.sharelatex.com/learn)