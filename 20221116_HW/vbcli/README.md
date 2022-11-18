To install on Arch based Linux

1. Install VirtualBox SDK

   ```
   sudo pamac virtualbox-sdk
   ```

2. Install Python

   ```
   sudo pamac python
   ```

3. Be sure there is a VBOX_INSTALL_PATH defined or define it using

   ```
   export VBOX_INSTALL_PATH=$(which virtualbox)
   ```

4. Install VBox API for python. Go to VirtualBox’s downloads page (https://www.virtualbox.org/wiki/Downloads) and download the VirtualBox SDK. Within the extracted ZIP file there is a directory called “installer”. Open a console within the installer directory and run

   ```
   python vboxapisetup.py install
   ```

5. Install PIP for python

    ```
    sudo pamac python-pip
    ```

6. To get the latest released version of virtualbox from PyPI run the following

    ```
    python -m pip install virtualbox
    ```

