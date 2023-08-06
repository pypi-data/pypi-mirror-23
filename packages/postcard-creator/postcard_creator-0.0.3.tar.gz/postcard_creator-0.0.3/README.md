# Postcard Creator [![PyPI version](https://img.shields.io/pypi/v/postcard_creator.svg)](https://badge.fury.io/py/postcard_creator) [![Build Status](https://travis-ci.org/abertschi/postcard_creator_wrapper.svg?branch=master)](https://travis-ci.org/abertschi/postcard_creator_wrapper) [![PyPI version](https://img.shields.io/pypi/pyversions/postcard_creator.svg)](https://pypi.python.org/pypi/postcard_creator) [![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

A python wrapper around the Rest API of the Swiss Postcard creator  
This project is still in early development. Feedback and support appreciated.

## Installation
```sh
$ pip install postcard-creator
```

## Setup / API Usage
```python
from postcard_creator.postcard_creator import PostcardCreator

w = PostcardCreator(token)
w.get_user_info()
w.get_billing_saldo()
w.get_quota()
w.has_free_postcard()
w.send_free_card(postcard=)
```

## Usage

```python
from postcard_creator.postcard_creator import PostcardCreator, Postcard, Token, Recipient, Sender

token = Token()
token.fetch_token(username='', password='')
token.has_valid_credentials(username='', password='')
recipient = Recipient(prename='', lastname='', street='', place='', zip_code=0000)
sender = Sender(prename='', lastname='', street='', place='', zip_code=0000)
card = Postcard(message='', recipient=recipient, sender=sender, picture_stream=open('./my-photo.jpg', 'rb'))

w = PostcardCreator(token)
w.send_free_card(postcard=card, mock_send=False)
```

### Advanced configuration
The following keyword arguments are available for advanced configuration (listed with corresponding defaults).

**PostcardCreator#send_free_card()**:
- `image_export = False`: Export postcard image to current directory (os.getcwd)
- `image_rotate = True`: Rotate image if image height > image width
- `image_quality_factor = 20`: Change picture quality, resulting image has 
`image_quality_factor x (image_target_width x image_target_height)` many pixels
- `image_target_width = 154`: Postcard image base width
- `image_target_height = 111`: Postcard image base height

### Logging
```python
import logging

logger = logging.getLogger('postcard_creator')

# log levels
# 5: trace
# 10: debug
# 20: info
# 30: warning
```

## Related
- [postcards](https://github.com/abertschi/postcards) - A CLI for the Swiss Postcard Creator
- [postcardcreator](https://github.com/gido/postcardcreator) - node.js API for the Swiss Post Postcard Creator

## Author

Andrin Bertschi

## License

[Apache License 2.0](LICENSE.md) © Andrin Bertschi
