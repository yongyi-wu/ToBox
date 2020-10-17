# ToBox: a toolbox for HoltLab@CMU

This program is developed for the HoltLab@CMU to manage data in the Box cloud storage. It enables command-line-style interactions on local machine with cloud files and folders. Current features are outlined in **Basic Commands** section. 


## File Structure

```shell
.
├── app
│   ├── __init__.py
│   ├── auth.py
│   ├── data.py
│   ├── parse.py
│   └── utils.py
├── help
│   ├── images
│   └── get_tokens.pdf
├── README.md
├── config.py
├── main.py
└── requirements.txt
```


## Preliminaries

### Setup Account

1. Activate your Box Developer Console using your Box account. 
2. Copy your Client ID and Client Secret to `config.py`

Please refer to `help/get_tokens.pdf` for instructions.

### Install Dependencies

1. Download and install Python 3. Remember to add Python to your PATH during installation. Optionally, you can use miniconda/anaconda for better management of Python packages. 
2. Install required Python packages. (This step may overwrite some previously packages)
    ```shell
    pip install -r requirements.txt
    ```


## Basic Commands

1. 
2. 


## Contact

Please do not hesitate to contact me if you encounter any bugs or difficulties while using this program. Also, I am looking forward to your feedback to improve this program. 

Author: Ethan Wu

Email: yongyiw@andrew.cmu.edu
