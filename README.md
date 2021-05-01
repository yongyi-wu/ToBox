# ToBox: a toolbox for HoltLab@CMU

This program is developed for the HoltLab@CMU to manage data in the Box cloud storage. It enables command-line-style interactions on local machine with cloud files and folders. Current features are outlined in **Basic Commands** section. 


## File Structure

```shell
.
├── app
│   ├── __init__.py
│   ├── auth.py
│   ├── data.py
│   ├── parse.py
│   └── utils.py
├── help
│   ├── example
│   └── get_tokens.pdf
├── README.md
├── ToBox.py
├── main.py
└── requirements.txt
```


## Preliminaries

### Setup Account

1. Activate your Box Developer Console using your Box account
2. Copy your Client ID and Client Secret to `ToBox.py`

Please refer to `help/get_tokens.pdf` for more instructions. 

### Install Dependencies

1. Download and install Python 3. Remember to add Python to your PATH during installation
2. Install required Python packages. This step may overwrite some previously installed packages
    * Open Windows Command Prompt / Mac Terminal / Linux Terminal
    * Navigate to the directory of ToBox program
    * Type in the following command
        ```shell
        pip install -r requirements.txt
        ```
        > To paste into command line, you may need `Ctrl+Shift+v` instead of `Ctrl+v`

### Run Program
1. Obtain a Developer Token from the Box Developer Console
    > Developer Token is valid for only 60 minutes
2. Execute the Python script
    ```shell
    python ToBox.py <Developer Token>
    ```
3. Type in supported commands after `>>>`


## Supported Commands

Overall, the syntax is aligned with the convention: 
```shell
<command name> [option(s)] <required argument(s)>
```
For example, `upload --folder help/example ~`

So far, there are six basic commands implemented. 
* `quit`: exit the program
* `help`: print the general instruction
* `cd`: change the working directory
* `ls`: print the directory and file structure
* `upload`: upload files or folders from local computer to cloud
* `download`: download files or folders from cloud to local computer

To view available arguments and explanation, you can type in 
```
<command name> --help
```


## Contact

Please do not hesitate to contact me if you encounter any bugs or difficulties while using this program. Your feedback is greatly appreciated. 

Author: Yongyi (Ethan) Wu

Email: wyy@cmu.edu
