# whatsapp-auto-message
Send automated messages via Selenium / WhatsApp Web to your friends.<br>
This is just a little personal project with a lot to do. There are many better tools out there in GitHub to use! :) <br>
<br>
...yes the code is a mess. It was not so planned, but my first idea was not compatible with my programming skills with selenium and the understanding how WhatsApp Web works 😅 <br>

But hey it works, for now ¯\\\_(ツ)\_/¯ <br>
_For now it is just a bad version of the bulk function from whatsapp itself with an optinal timestamp_

## Usage
Install the `requirements.txt` or use poetry.<br>

Run main with -h for the help message
```console
usage: WhatsApp Bot [-h] -n NAMES [NAMES ...] -m MESSAGE [-y] [-t TIME] [-g TOKEN]      

Send messages to your friends

optional arguments:
  -h, --help            show this help message and exit
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        The Name of the Users to send the message. At least one required
  -m MESSAGE, --message MESSAGE
                        The message to send
  -y, --silent          Skip the confirm of the values
  -t TIME, --timestamp TIME
                        Add a timestamp when to send the message: dd.mm.yyyy hh:mm
  -g TOKEN, --token TOKEN
                        Set the GH_TOKEN or use the EVN
```

If you download the chrome driver a lot, you need to set the env "GH_TOKEN" with your personal token. See [GH_TOKEN](https://github.com/SergeyPirogov/webdriver_manager#gh_token) or use `--token` <br>

At each start of the programm you need to connect whatsapp again with your phone. After that all given names will recive the message.

## Docker
Now you can use it with docker! 🚀🥳<br>
But you still have to create you local Docker-Image (for now) <br>

## Build the container:
```console
# From GitHub
DOCKER_BUILDKIT=1 docker build -t whatsapp-messanger https://github.com/Floskinner/whatsapp-auto-message.git#main

# or without docker-buildkit
docker build -t whatsapp-messanger https://github.com/Floskinner/whatsapp-auto-message.git#main
```
```console
# From code
git clone https://github.com/Floskinner/whatsapp-auto-message.git
cd whatsapp-auto-message
DOCKER_BUILDKIT=1 docker build -t whatsapp-messanger .

# or without docker-buildkit
docker build -t whatsapp-messanger .
```

## Use the container
Use it just like the normal programm with the parameters at the end.<br>
❗ **Always use -y!** ❗<br>
❗ **Don`t forget to scan the QR-Code** ❗ ...in the console. So if you want detached mode, make sure to scan the code.
```console
docker run --name my-whatsapp-messanger whatsapp-messanger -h
usage: WhatsApp Bot [-h] -n NAMES [NAMES ...] -m MESSAGE [-y] [-t TIME]
                    [-g TOKEN]

Send messages to your friends

optional arguments:
  -h, --help            show this help message and exit
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        The Name of the Users to send the message. At least
                        one required
  -m MESSAGE, --message MESSAGE
                        The message to send
  -y, --silent          Skip the confirm of the values
  -t TIME, --timestamp TIME
                        Add a timestamp when to send the message: dd.mm.yyyy
                        hh:mm
  -g TOKEN, --token TOKEN
                        Set the GH_TOKEN or use the EVN
```

Here some examples:
```console
# Wake one Friend at given time
docker run whatsapp-messanger -n "My Friend" -m "Wake Up!!!" -t "20.04.2022 04:20" --token "gh_s3u9r2e4I2t8e3l6l2y4o2u5t2h2i2s" -y

# Set the GH_TOKEN in the ENV
docker run --env "GH_TOKEN=gh_s3u9r2e4I2t8e3l6l2y4o2u5t2h2i2s" whatsapp-messanger -n "My Friend" -m "Wake Up!!!" -t "20.04.2022 04:20" -y

# Send a message to two friends
docker run whatsapp-messanger -n "My Friend" "Other friend" -m "Wake Upclear!" -t "20.04.2022 04:20" --token "gh_s3u9r2e4I2t8e3l6l2y4o2u5t2h2i2s" -y
```

## Planned features
- [ ] Set some datetime settings (✅) and a intervall for sending the messages
- [ ] Saves the Login with your phone (after each restart of the programm you have to login again)
- [X] Headless usage (only with Firefox)
- [ ] Publish the docker image
- [ ] Random selection of multiple messages
- [ ] Read the settinngs from a file
- [ ] Improved Exception handling
- [ ] (Implement some other messanger)