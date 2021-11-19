# Mac Notifier
Mac_notifier is a command line utility to display notifications, alerts and dialogs on mac. It executes apple scripts underneath to achieve the purpose.

## Installation
```
pip install mac-notifier
```

## Usage
```
dsp notify 'Hello wolrd'                                 # send notification
dsp notify -t 'Hurry up!' 'Time is precious'             # send notification with title

dsp alert WARNING                                        # display alert
dsp alert -b '["Sorry", "I will"]' 'Will you marry me?'  # display alert with customized buttons

dsp dialog 'Man is not made for defeat. A man can be destroyed but not defeated.'
```
For more detailed usage, refer to command help.

## Command Help
Use `dsp --help` to show help:
```
Usage: dsp [OPTIONS] COMMAND [ARGS]...

  Display notifications, alerts and dialogs on mac

Options:
  --help  Show this message and exit.

Commands:
  alert   Display an alert on mac
  dialog  Display a dialog on mac
  notify  Display a notification on mac
```

Use `dsp subcommand --help` to show help for subcommands, for example:
```
Usage: dsp alert [OPTIONS] CONTENT

  Display an alert on mac

Options:
  -m, --message TEXT     Explanatory message.
  -b, --buttons TEXT     List of button names in json format, e.g. ["Cancel",
                         "OK"].
  -d, --default INTEGER  Index of default buttons, 1 based.
  -l, --lasting INTEGER  Number of seconds before dismissing. Wait forever if
                         not specified.
  --help                 Show this message and exit.
```