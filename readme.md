# Class Bot

Python script that uses selenium to automatically sign you up for ASU classes

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all packages using the following command.

```bash
pip install -r requirements.txt
```
## Installation

Clone the project

```bash
  git clone https://github.com/benbousquet/class-bot.git
```

Go to the project directory

```bash
  cd class-bot
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Install senenium web driver
- MacOS: https://medium.com/@mintholic1/installing-selenium-webdriver-on-your-mac-1ef5fec7efda
- Windows: https://youtu.be/Xjv1sY630Uc?t=255

**IMPORTANT:** If you are using Windows (ignore if using MacOS)
1. Comment out line 25 where it shows `driver = webdriver.Chrome()`
2. Uncomment line line 27 where it shows `# driver = webdriver.Chrome(executable_path="c:\webdrivers\chromedriver.exe")`
3. Ensure the executable_path is correct

## Usage

1. Update ".env sample" file with username and password then change name to ".env" 
2. Add class you want to your shopping cart
3. Run the following command 
```python 
python main.py
```

After a single class is signed up for, the program will crash (as intended) but due to slow page loading or bad requests it might crash after a few hours of running so make sure to check it often.
## Features

- Auto signs up for ASU classes
- Runs locally
- Stops running when successfully signed up for class
- Easy set up


## Authors

- [@benbousquet](https://www.github.com/benbousquet)


## License

[MIT](https://choosealicense.com/licenses/mit/)

