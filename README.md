## Ark-Hue-Delegates
Interaction between Ark and Philips Hue lights for Delegates.

Light will be green if the watched node is healthy, yellow if it one block and red for more than one.

## Usage

### Python installation

Python can be downloaded [here](https://www.python.org/downloads/).

For further informations on how to install Python on your operating system : 

[Windows guide](https://docs.python.org/3/using/windows.html)

[Unix guide](https://docs.python.org/3/using/unix.html)

[OSx guide](https://docs.python.org/3/using/mac.html)

### Pip installation

Pip come bundled with the most recent versions of Python, but in case it wouldn't be [get it here](https://pip.pypa.io/en/stable/installing/)

### Dependencies installation

As a last step it's required to install the `requests` library to be able to use this application, to do so :

```
$ pip install requests
```

That command will install the `requests` library globally on your system, to contain it a bit more [virtualenv](https://virtualenv.pypa.io/en/latest/) is here

### Running it

Once everything installed, you should edit the configuration file to suit your needs, the only parameter really necessary to update is the `bridge_ip` one and maybe the `light_id` one too.
If you want to look for a specific delegate you should edit the `delegate_name` inside the configuration file, by default it's set to "thegoldenhorde". 

After that, you should be able to execute the script like this : 

```
$ python main.py
```

And voilà, colors changing based on the state of your node !

### Configuration

You can edit any values present in the configuration file to match your preferences.