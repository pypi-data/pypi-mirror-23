# *-* coding: utf-8 *-*
"""
The :py:class:`EncryptedTempDirectory` class is designed for when you need a
directory whose contents are encrypted by `eCryptfs <http://ecryptfs.org/>`_,
but you would also like to take advantage of the features of in-memory-only
directories, such as increased access speed and automatic deletion (e.g.\  when
you're :doc:`unpacking a CRX <crx_unpack>`).

To understand this class fully, please also read the documentation on the
:py:func:`~tempfile.TemporaryDirectory` class.
"""

from base64 import b64encode
from os import mkdir, remove
from os.path import basename, isdir, join, expanduser
from re import search
from subprocess import run, PIPE
from tempfile import TemporaryDirectory


class EncryptedTempDirectory(TemporaryDirectory):
    """Create and return an encrypted temporary directory.

    This behaves similarly to :class:`TemporaryDirectory`, except for the
    following:

    - It requires that an "upper directory" be specified, which will be the
      mount point used by eCryptfs to mount the encrypted directory to the
      filesystem.
    - It creates two files in `~/.ecryptfs` required to mount the directory
      (both of which are deleted when this object is):

      - `ALIAS.sig` - Contains the signatures for the FEK and FNEK encryption
        keys.
      - `ALIAS.conf` - Contains `fstab`-style information for which directory
        eCryptfs should mount and where.

    In the above notes, `ALIAS` (which is a term used in the eCryptfs
    documentation, see links below) will be the name of the created temp
    directory, accessible as the basename of ``self.name``.

    To use an :class:`EncryptedTempDirectory` object, it's best to use it with
    a ``with`` clause, like so:

    ::

        with EncryptedTempDirectory(upper_dir=upper) as lower:
            ...

    Better yet, use an instance of :class:`TemporaryDirectory` as the upper
    directory, like this:

    ::

        with TemporaryDirectory() as upper, \\
                EncryptedTempDirectory(upper_dir=upper) as lower:
            ...

    .. note::

        In the above example, both temporary directories are deleted as soon as
        the ``__exit__()`` method is called (triggered by the close of the
        ``with`` clause). So make sure that anything you need to do with these
        objects, you do before leaving the ``with`` clause.

    .. note::

        This class depends on eCryptfs, so it will need to be installed on the
        system to work properly. Similarly, this class depends on the
        following Unix tools/devices:

        - ``head``
        - ``ecryptfs-add-passphrase``
        - ``mount``
        - ``keyctl``
        - ``/dev/urandom``

        On Debian/Ubuntu-based systems, you can install these with:

        ::

            sudo apt-get install coreutils mount keyutils ecryptfs-utils

    For more information, see the following resources:

    - http://manpages.ubuntu.com/manpages/zesty/en/man1/mount.ecryptfs_private.1.html
    - http://manpages.ubuntu.com/manpages/zesty/en/man1/ecryptfs-add-passphrase.1.html
    - https://askubuntu.com/questions/574110/how-to-use-ecryptfs-with-a-random-directory/574425#574425
    """

    def __init__(self, *, upper_dir, **kwargs):
        """
        :param str upper_dir: Path where the encrypted directory will be
            mounted, and where the unencrypted version of the files will be
            accessible.
        :param kwargs: Additional parameters to pass to the constructor of the
            :py:class:`~tempfile.TemporaryDirectory` class.
        """
        self._upper_dir = upper_dir
        super().__init__(**kwargs)

        # Make the ~/.ecryptfs dir if it doesn't already exist
        ecrypt_dir = expanduser(join('~', '.ecryptfs'))
        if not isdir(ecrypt_dir):
            mkdir(ecrypt_dir, mode=0o700)

        # Prep dirs for eCryptfs
        self._alias = basename(self.name)
        self._conf_file = '{}.conf'.format(join(ecrypt_dir, self._alias))
        with open(self._conf_file, 'w') as conf:
            conf.write('{} {} ecryptfs'.format(self.name, self._upper_dir))

        # Create the signature file and add it to the keyring
        self._sig_file = '{}.sig'.format(join(ecrypt_dir, self._alias))
        passwd = b64encode(run(['head',  '-c 32', '/dev/urandom'], check=True, stdout=PIPE).stdout)
        sig = run(['ecryptfs-add-passphrase', '--fnek'], input=passwd, stdout=PIPE).stdout.decode('utf-8')
        with open(self._sig_file, 'w') as sig_out:
            for line in sig.split('\n'):
                # There should be two matches. We want both in the signature file.
                m = search(r'sig \[(.*?)\]', line)
                if m:
                    sig_out.write(m.group(1))
                    sig_out.write('\n')

    def __enter__(self):
        # Mount the encrypted dir
        try:
            run(['mount.ecryptfs_private', self._alias], check=True)
        except:
            # No matter what the exception, we should try to remove the keys from the keyring
            keys = {}
            # Get a list of the keys so we can reference them later
            key_output = run(['keyctl', 'show'], stdout=PIPE).stdout.decode('utf-8')
            for key_line in key_output.split('\n'):
                m = search(r'^ *([0-9]*).* ([a-f0-9]*)$', key_line)
                if m:
                    keys[m.group(2)] = m.group(1)
            # The contents of the sig file will help us determine which keys should be deleted
            with open(self._sig_file) as sig_file:
                for line in sig_file:
                    line = line.strip()
                    if not len(line):
                        continue
                    # Unlink the key
                    run(['keyctl', 'unlink', keys[line]])

            self.cleanup()  # Do all the regular cleanup
            raise  # Re-raise the original exception

        return super().__enter__()

    def __exit__(self, exc, value, tb):
        # Unmount the encrypted dir
        run(['umount.ecryptfs_private', self._alias], check=True)
        super().__exit__(exc, value, tb)

    def cleanup(self):
        # Remove all the working files
        for f in (self._conf_file, self._sig_file):
            remove(f)
        super().cleanup()
