import os
import shlex
import pipes

try:
    import pync
except:
    pync = None

from plumbum.cmd import file as file_cmd
from send2trash import send2trash as to_trash

from .metadata import Metadata, FileFormatError
from .geo import location
from .creation_datetime import creation_datetime


__all__ = [
    'to_trash', 'Metadata', 'location', 'creation_datetime',
    'parse_cmd_args', 'list_dirs', 'list_files', 'notify',
    'FileFormatError',
]


def parse_cmd_args(s, **wildcards):
    wildcards = {
        wildcard: pipes.quote(value) for
        (wildcard, value) in wildcards.items()
    }
    s = s.format(**wildcards)
    return shlex.split(s.strip())


def list_dirs(directory):
    filenames = (os.path.join(directory, basename) for basename
                 in os.listdir(directory))
    return sorted(filename for filename
                  in filenames if os.path.isdir(filename))


def list_files(directory, exts=None, recursive=False):
    if exts is not None:
        exts = frozenset('.' + ext.lstrip('.') for ext in exts)

    def list_dir(directory):
        for basename in os.listdir(directory):
            filename = os.path.join(directory, basename)
            if recursive and os.path.isdir(filename):
                for filename in list_files(filename, exts, recursive=True):
                    yield filename
                continue
            elif exts and not os.path.splitext(filename)[1].lower() in exts:
                continue
            yield filename

    return sorted(list_dir(directory))


def is_corrupted_file(filename):
    return file_cmd(filename).strip() == '{}: data'.format(filename)


def notify(name, message):
    if pync:
        pync.Notifier.notify(message, title=name)
