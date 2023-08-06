aws-google-auth
===============

This command-line tool allows you to acquire AWS temporary (STS)
credentials using Google Apps as a federated (Single Sign-On, or SSO)
provider.

Setup
-----

You'll first have to set up Google Apps as a SAML identity provider
(IdP) for AWS. There are tasks to be performed on both the Google Apps
and the Amazon sides; these references should help you with those
configurations:

-  `How to Set Up Federated Single Sign-On to AWS Using Google
   Apps <https://aws.amazon.com/blogs/security/how-to-set-up-federated-single-sign-on-to-aws-using-google-apps/>`__
-  `Using Google Apps SAML SSO to do one-click login to
   AWS <https://blog.faisalmisle.com/2015/11/using-google-apps-saml-sso-to-do-one-click-login-to-aws/>`__

If you need a fairly simple way to assign users to roles in AWS
accounts, we have another tool called `Google AWS
Federator <https://github.com/cevoaustralia/google-aws-federator>`__
that might help you.

Important Data
~~~~~~~~~~~~~~

You will need to know Google's assigned Identity Provider ID, and the ID
that they assign to the SAML service provider.

Once you've set up the SAML SSO relationship between Google and AWS, you
can find the SP ID by drilling into the Google Apps console, under
``Apps > SAML Apps > Settings for AWS SSO`` -- the URL will include a
component that looks like ``...#AppDetails:service=123456789012...`` --
that number is ``GOOGLE_SP_ID``

You can find the ``GOOGLE_IDP_ID``, again from the admin console, via
``Security > Set up single sign-on (SSO)`` -- the ``SSO URL`` includes a
string like ``https://accounts.google.com/o/saml2/idp?idpid=aBcD01AbC``
where the last bit (after the ``=``) is the IDP ID.

Installation
------------

You can install quite easily via ``pip``, if you want to have it on your
local system:

.. code:: shell

    localhost$ sudo pip install aws-google-auth

If you don't want to have the tool installed on your local system, or if
you prefer to isolate changes, there is a Dockerfile provided, which you
can build with:

.. code:: shell

    localhost$ cd ..../aws-google-auth && docker build -t aws-google-auth .

Usage
-----

1. Set environment variables for ``GOOGLE_USERNAME``, ``GOOGLE_IDP_ID``,
   and ``GOOGLE_SP_ID`` (see above under "Important Data" for how to
   find the last two; the first one is usually your email address)
2. For Docker:
   ``docker run -it -e GOOGLE_USERNAME -e GOOGLE_IDP_ID -e GOOGLE_SP_ID aws-google-auth``
3. For Python: ``aws-google-auth``

You'll be prompted for your password. If you've set up an MFA token for
your Google account, you'll also be prompted for the current token
value.

If you have more than one role available to you, you'll be prompted to
choose the role from a list; otherwise, if your credentials are correct,
you'll just see the AWS keys printed on stdout.

You should ``eval`` the ``export`` statements that come out, because
that'll set environment variables for you. This tools currently doesn't
write credentials to an ``~/.aws/credentials`` file

Notes on Authentication
-----------------------

Google supports a number of 2-factor authentication schemes. Each of these
results in a slightly different "next" URL, if they're enabled, during ``do_login``

Google controls the preference ordering of these schemes in the case that
you have multiple ones defined.

The varying 2-factor schemes and their representative URL fragments handled
by this tool are:

+------------------+-------------------------------------+
| Method           | URL Fragment                        |
+==================+=====================================+
| No second factor | (none)                              |
+------------------+-------------------------------------+
| TOTP (eg Google  | ``.../signin/challenge/totp/2?...`` |
|  Authenticator   |                                     |
|  or Authy)       |                                     |
+------------------+-------------------------------------+
| SMS (or voice    | ``.../signin/challenge/ipp/2?...``  |
|  call)           |                                     |
+------------------+-------------------------------------+
| Google Prompt    | ``.../signin/challenge/az/2?...``   |
|  (phone app)     |                                     |
+------------------+-------------------------------------+
| Backup code      | ``... (unknown yet) ...``           |
|  (printed codes) |                                     |
+------------------+-------------------------------------+
| Security key     | ``... (unknown yet) ...``           |
|  (eg yubikey)    |                                     |
+------------------+-------------------------------------+

Acknowledgements
----------------

This work is inspired by `keyme <https://github.com/wheniwork/keyme>`__
-- their digging into the guts of how Google SAML auth works is what's
enabled it.
