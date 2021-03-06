# python-thaibulksms

A small number of tiny wrapper functions to help you get started sending SMSs using Thailand's http://www.thaibulksms.com/. These functions work in plain python plus there's a couple of extra functions specifically designed to work with django and django+celery.

ThaiBulkSMS.com also offer OTP sending and retrieving functionality but that is currently not included in this package. It would be trivial to add.

### Sending SMS:

```
from pythonthaibulksms.thaibulksms import thaibulksms_sms

thaibulksms_sms(
    'YOUR_USERNAME',
    'YOUR_PASSWORD',
    '0899999999', # recipient phone number
    'Hello! How are you?', # message
    True,  # True = corporate, False = standard
    sender='MY COMPANY', # optional, needs to be set up in advance with thaibulksms.com
    schedule='2009301116', # optional, format YYMMDDhhmm
)
```


### Using Django

First, add the following config to your project `settings.py` file
```
THAIBULKSMS = {
    'default': {
        'username': 'YOUR_USERNAME',
        'password': 'YOUR_PASSWORD',
        'corporate': True,  # True = corporate, False = standard
        'sender': 'MY COMPANY' # optional, needs to be set up in advance with thaibulksms.com
    },
}
```

Then call the following function as required:
```
from pythonthaibulksms.django import django_thaibulksms_sms

django_thaibulksms_sms(
    '0899999999', # recipient phone number
    'Hello! How are you?', # message
    'default', # optional, which config to use from your settings.py, defaults to 'default'
    schedule='2009301116', # optional, format YYMMDDhhmm
)
```

### Using Celery within Django

Add `pythonthaibulksms` to the `INSTALLED_APPS` section of your project `settings.py` file

```
INSTALLED_APPS = [
    ...
    'pythonthaibulksms',
    ...
]
```

To send call the thaibulksms API via a task queue, use:
```
from pythonthaibulksms.tasks import django_thaibulksms_sms_celery

django_thaibulksms_sms_celery.delay(
    '0899999999', # recipient phone number
    'Hello! How are you?', # message
    'default', # optional, which config to use from your settings.py, defaults to 'default'
    schedule='2009301116', # optional, format YYMMDDhhmm
)
```