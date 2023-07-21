# webtest/authdown_freepik.py

![](https://c4.wallpaperflare.com/wallpaper/814/599/816/kono-subarashii-sekai-ni-shukufuku-wo-aqua-konosuba-minimalism-simple-background-wallpaper-preview.jpg)

This repository is my path in learning parsing. There are a lot of files here, there may be several months between some. I'd rather tell you what I came to, because everything else here is shit code
This repo contains code that downloads images from Freepik. The code first logs in to the Freepik website using the specified login email and password. Then, it downloads the image from the specified URL.

## Requirements

* Python 3.11
* The Selenium4 library

## Installation

To install the Selenium library, you can run the following command:

```bash
pip install requests;
pip install selenium;
pip install webdriver-manager;
```

## Usage

To use the code, you first need to import the `authdown_freepik` library. Then, you can use the `sing_in()` and `download_url()` functions to log in to Freepik and download the image, respectively.
Although it's better not to hardcode important data like that.
Here is an example of how to use the code:


```python
import authdown_freepik


email = "example@email.com"
password = "python~test_auth~down"
url = "https://ru.freepik.com/free-photo/view-of-city-with-apartment-buildings-and-green-vegetation_43468051.htm#&position=7&from_view=collections"

# Log in to Freepik
authdown_freepik.sing_in(email, password)

# Download the image
authdown_freepik.download_url(url)
```

The `sing_in()` function takes two arguments: the login email and password. The `download_url()` function takes one argument: the URL of the image you want to download.

The `sing_in()` function will log in to Freepik using your login email and password. The `download_url()` function will download the image from the URL you specified.

The image will be saved in the current working directory.
