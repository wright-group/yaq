"""Start yaq."""


# --- import --------------------------------------------------------------------------------------


import appdirs
import os
import shutil

from yaq.app import main_window


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))
base = os.path.dirname(os.path.dirname(here))

icons = []
icons.append(os.path.join(base, 'images', 'icon.ico'))
icons.append(os.path.join(base, 'images', 'icon.png'))


# --- main ----------------------------------------------------------------------------------------


def main():
    """Start yaq application."""
    # create app data directory
    d = os.path.join(appdirs.user_data_dir(), 'yaq')
    if not os.path.isdir(d):
        os.mkdir(d)
        # add icons
        for p in icons:
            src = p
            dst = os.path.join(d, os.path.basename(p))
            shutil.copy(src, dst)
    # begin
    main_window.main()


if __name__ == '__main__':
    main()
