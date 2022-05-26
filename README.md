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
usage: WhatsApp Bot [-h] -n NAMES [NAMES ...] -m MESSAGE [-t TIME]

Send messages to your friends

optional arguments:
  -h, --help            show this help message and exit
  -n NAMES [NAMES ...], --names NAMES [NAMES ...]
                        The Name of the Users to send the message. At least one required
  -m MESSAGE, --message MESSAGE
                        The message to send
  -t TIME, --timestamp TIME
                        Add a timestamp when to send the message: dd.mm.yyyy hh:mm
```

If you download the chrome driver a lot, you need to set the env "GH_TOKEN" with your personal token. See [GH_TOKEN](https://github.com/SergeyPirogov/webdriver_manager#gh_token) <br>

At each start of the programm you need to connect whatsapp again with your phone. After that all given names will recive the message.

## Planned features
- [ ] Set some datetime settings (✅) and a intervall for sending the messages
- [ ] Saves the Login with your phone (after each restart of the programm you have to login again)
- [ ] Headless usage
- [ ] Random selection of multiple messages
- [ ] Read the settinngs from a file
- [ ] (Implement some other messanger)
- [ ] Improved Exception handling