"""This module defines an sshd configuration."""
from distutils.spawn import find_executable
import subprocess
import os
import tempfile

from .base import Daemon


# Generate a new ssh keypair at each run
KEYFILE = tempfile.mktemp(dir='/tmp')
PUBKEY = '%s.pub' % KEYFILE
if os.path.exists(KEYFILE):
    os.unlink(KEYFILE)
if os.path.exists(PUBKEY):
    os.unlink(PUBKEY)
subprocess.call(['ssh-keygen', '-b', '2048', '-t', 'rsa', '-f', KEYFILE, '-q',
                 '-P', ''])


class SSHd(Daemon):

    NAME = 'sshd'

    @property
    def startup_line(self):
        return ('{name} -D -u0 -f {cfg}'
                .format(name=find_executable(self.NAME),
                        pubkey=PUBKEY,
                        cfg=os.path.abspath(self.cfg_filename)))

    @property
    def dry_run(self):
        return '%s -t' % self.startup_line

    def set_defaults(self, defaults):
        super(SSHd, self).set_defaults(defaults)

    def build(self):
        cfg = super(SSHd, self).build()
        cfg.authorized_keys = PUBKEY
        return cfg
