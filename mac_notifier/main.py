import json
import subprocess
import click


@click.command()
@click.option("-t", "--title", help="Add title to notification.")
@click.option("-st", "--subtitle", help="Add subtitle to notification.")
@click.argument("content")
def notify(title, subtitle, content):
    """Display a notification on mac"""
    osa_stat = f'display notification "{content}"'
    if title:
        osa_stat += f' with title "{title}"'
    if subtitle:
        osa_stat += f' subtitle "{subtitle}"'
    subprocess.run(args=["osascript", "-e", osa_stat])


@click.command()
@click.option("-m", "--message", help="Explanatory message.")
@click.option(
    "-b",
    "--buttons",
    help='List of button names in json format, e.g. ["Cancel", "OK"].',
)
@click.option("-d", "--default", type=int, help="Index of default buttons, 1 based.")
@click.option(
    "-l",
    "--lasting",
    type=int,
    help="Number of seconds before dismissing. Wait forever if not specified.",
)
@click.argument("content")
def alert(message, buttons, default, lasting, content):
    """Display an alert on mac"""
    osa_stat = f'display alert "{content}"'
    if message:
        osa_stat += f' message "{message}"'
    if buttons:
        buttons = json.loads(buttons)
        assert isinstance(buttons, list), "buttons should be a json list"
        buttons = [f'"{button}"' for button in buttons]
        buttons = f'{{{", ".join(buttons)}}}'
        osa_stat += f" buttons {buttons}"

    if default:
        osa_stat += f" default button {default}"
    if lasting:
        osa_stat += f" giving up after {lasting}"

    subprocess.run(args=["osascript", "-e", osa_stat])


@click.command()
@click.option(
    "-b",
    "--buttons",
    help='List of button names in json format, e.g. ["Cancel", "OK"].',
)
@click.option("-d", "--default", type=int, help="Index of default buttons, 1 based.")
@click.option("-t", "--title", help="Add title to dialog.")
@click.option(
    "-l",
    "--lasting",
    type=int,
    help="Number of seconds before dismissing. Wait forever if not specified.",
)
@click.argument("content")
def dialog(buttons, default, title, lasting, content):
    """Display a dialog on mac"""
    osa_stat = f'display dialog "{content}"'
    if buttons:
        buttons = json.loads(buttons)
        assert isinstance(buttons, list), "buttons should be a json list"
        buttons = [f'"{button}"' for button in buttons]
        buttons = f'{{{", ".join(buttons)}}}'
        osa_stat += f" buttons {buttons}"

    if default:
        osa_stat += f" default button {default}"
    if title:
        osa_stat += f' with title "{title}"'
    if lasting:
        osa_stat += f" giving up after {lasting}"

    subprocess.run(args=["osascript", "-e", osa_stat])


@click.group()
def dsp():
    """Display notifications, alerts and dialogs on mac"""
    pass


dsp.add_command(notify)
dsp.add_command(alert)
dsp.add_command(dialog)

if __name__ == "__main__":
    dsp()
