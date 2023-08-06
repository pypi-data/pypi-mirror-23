"""
'||
 || ...  ... ...  .. .. ..
 ||'  ||  ||  ||   || || ||
 ||    |  ||  ||   || || ||
 '|...'   '|..'|. .|| || ||.

Created by Dylan Araps
"""
import argparse
import pathlib
import signal

from . import display
from . import song


__version__ = "0.0.1"


def get_args():
    """Get the script arguments."""
    description = "bum - Download and display album art \
                   for mopidy-spotify tracks."
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("--size", metavar="\"px\"",
                     help="what size to display the album art in.",
                     default=250)

    arg.add_argument("--cache_dir", metavar="\"/path/to/dir\"",
                     help="Where to store the downloaded cover art.",
                     default=pathlib.Path.home() / ".cache/bum")

    arg.add_argument("--version", action="store_true",
                     help="Print \"bum\" version.")

    return arg.parse_args()


def process_args(args):
    """Process the arguments."""
    if args.version:
        print(f"bum {__version__}")
        exit(0)


def main():
    """Main script function."""
    args = get_args()
    process_args(args)

    def signal_usr1(sig, frame):
        """Handle 'pkill -USR1 bum'."""
        print("Recieved SUGUSR1, swapping album art.")

        song.get_art(args.cache_dir)

        # Args are required when using signal, but we don't need them.
        del sig, frame

    signal.signal(signal.SIGUSR1, signal_usr1)
    disp = display.init()

    song.get_art(args.cache_dir)

    while True:
        display.launch(disp, "/home/dylan/.cache/bum/current.jpg")
        signal.pause()


if __name__ == "__main__":
    main()
