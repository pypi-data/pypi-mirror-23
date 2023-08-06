=========
Mail Save
=========

Save emails to a file. It can be used as a replacement for sendmail or a SMTP server.

It is different from other tools like `maildump <https://pypi.org/project/maildump/>`__ because:

- It is very minimalist: no Web or GUI interface, just files.
- It can be used instead of sendmail.

To use in place of sendmail, just put the path to the ``mailsave`` executable instead of the sendmail one. For instance, in a ``php.ini`` file:

::

    sendmail_path = /home/jenselme/.virtualenvs/test/bin/mailsave --dir mails

To use as an SMTP server, launch it like this:

::

    mailsave --server --dir logs


Written for Python 3.5+.
