# Hypershot

Create screen shots of a video file, and upload them to an image host.

**IN DEVELOPMENT**

[![GitLab CI](https://gitlab.com/kybernetics/hypershot/badges/master/build.svg)](https://gitlab.com/kybernetics/hypershot/commits/master)
[![Coverage Report](http://img.shields.io/badge/coverage-%3e80%25-5555ff.svg)](https://kybernetics.gitlab.io/hypershot/)
[![PyPI](https://img.shields.io/pypi/v/hypershot.svg)](https://pypi.python.org/pypi/hypershot/)
[![Documentation](https://readthedocs.org/projects/hypershot/badge/?version=latest)](http://hypershot.readthedocs.io/en/latest/?badge=latest)

**Contents**

 * [Introduction](#introduction)
   * [What it Does](#what-it-does)
   * [How it Works](#how-it-works)
 * [Installation](#installation)
   * [Installing the Python Application](#installing-the-python-application)
   * [Installing Tools](#installing-tools)
 * [Usage](#usage)
   * [Common Options](#common-options)
   * [Generating and Uploading Screen Shots](#generating-and-uploading-screen-shots)
   * [Uploading Existing Images](#uploading-existing-images)
 * [Configuration](#configuration)
   * [Configuration File](#configuration-file)
   * [Image Hosters](#image-hosters)
     * [imgur](#imgur)
     * [Simple File Upload Sites](#simple-file-upload-sites)
     * [Chevereto Sites](#chevereto-sites)
   * [Logging Configuration](#logging-configuration)
 * [Templating of Upload Results](#templating-of-upload-results)
   * [Templating Introduction](#templating-introduction)
   * [Writing Custom Templates](#writing-custom-templates)
 * [Working with the Source Code](#working-with-the-source-code)
   * [Creating a Working Directory](#creating-a-working-directory)
   * [Building the Documentation Locally](#building-the-documentation-locally)
   * [Releasing to PyPI](#releasing-to-pypi)
 * [Links](#links)


## Introduction

### What it Does

Look at one or more video files, taking screen shots without any human interaction,
uploading the results to an image hosting service, and finally produce some text
output containing links to the images.
That output can be used for posting to forums, blogs, etc.

*hypershot* is designed for and tested on *Linux*, and it is expected and supported
to run on *Mac OSX* (report any issues you might encounter).
It *might* run on *Windows*, if you use *CygWin/Babun*, *Ubuntu for Windows*,
or one of the *Docker* distributions for *Windows*.


### How it Works

*hypershot* looks at a video file using *mediainfo*,
and then decides on the offsets for the screen shots,
depending on how many you requested and the duration of the video.
It then calls an external script or command to take those screenshots
– a default script using *mplayer*, *ffmpeg* or *avconv* is provided.

The resulting images are then uploaded to a configured image hoster,
and the returned URLs plus the mediainfo data are fed into a templating engine.
This way you can generate HTML, BBcode, Markdown, or whatever (text) format
you need. Then take the final result and post your screen shots on the web
– for your convenience, it's already in your paste buffer.

See [Usage](#usage) for more details, and the following section
on how to install the necessary software.


## Installation

### Installing the Python Application

You can install this software into your user home by using the following commands:

    mkdir -p ~/.local/venvs/hypershot && /usr/bin/pyvenv $_ ; . $_/bin/activate
    pip install -U pip
    pip install -r "https://gitlab.com/kybernetics/hypershot/raw/master/requirements.txt"
    pip install hypershot

    mkdir -p ~/bin && ln -nfs ../.local/venvs/hypershot/bin/hypershot $_

Doing it this way ensures that the software is installed in isolation not interfering
with other apps, and vice versa.
It also makes uninstalling very easy, because all files are contained in a single directory tree.

For a global install, do the above as `root` and replace `~/.local` by `/usr/local`,
and also replace the last command by this:

    ln -nfs ../venvs/hypershot/bin/hypershot /usr/local/bin

You might need to install `pyvenv` first, on Debian and Ubuntu this is done using
`sudo apt-get install python3-venv`.
If your platform does not come with a suitable Python3 package, consider using
[pyenv](https://github.com/pyenv/pyenv) to get Python 3.4+.


### Installing Tools

For uploading images, the above installation is all you need.
Doing screen shots though requires some additional tools to be available
on the system you want to use ``hypershot`` on.
You need to provide ``mediainfo`` and at least one of the supported video players.
The following describes installation on *Debian* and derived distros,
for others call the native package manager instead of APT.

``mediainfo`` and ``mplayer`` come pre-packaged starting with *Debian Wheezy* and *Ubuntu Trusty*,
so just install them like this:

    apt-get install mediainfo mplayer2

**TODO** Is ``mpv`` the better option?

The shell script bundled with this software is able to also use ``ffmpeg`` or ``avconv``.
Depending on the type of video file, these might be able to handle cases ``mplayer`` can not,
and vice versa, so it's best to have both.

Especially when it comes to *HEVC* encoded media (also known as *x.265*),
it's best to have a current *ffmpeg* version.
You can get one from the project's
[FFmpeg Static Builds](https://www.johnvansickle.com/ffmpeg/) website,
which also avoids the problems resulting from
the *“switch between ffmpeg and avconv and back”* game
Linux distros played a while ago.

To install the git build of ``ffmpeg``, do this:

    mkdir -p ~/.local/ffmpeg && cd $_
    wget "https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz"
    tar -xJ --no-same-owner --strip-components=1 -f $(basename "$_")
    ln -nfs $PWD/{ffmpeg,ffmpeg-10bit,ffprobe} ~/bin

Choose another archive from the website for 32bit or ARM machines (*Raspberry Pi*).

If you're able to become ``root``, install into ``/opt/ffmpeg``
and create the symlinks in ``/usr/local/bin`` instead.


## Usage

### Common Options

Look at the start of the
[cli.py](https://gitlab.com/kybernetics/hypershot/blob/master/src/hypershot/cli.py)
module for usage information on the ``hypershot`` command,
or call ``hypershot -h`` after installation.

Here is a copy of the ``--help`` output, but it might be outdated:

    Usage:
        hypershot [options] upload <image>...
        hypershot [options] services
        hypershot [options] templates
        hypershot [options] <video>...
        hypershot (-h | --help)
        hypershot --version

    Options:
        -h, --help          Show this screen.
        --version           Show version.
        --debug             Enable debugging features?
        -q, --quiet         Hide result output?
        -v, --verbose       Verbose logging?
        -n, --dry-run       Do not really upload images

        -c PATH, --config-dir=PATH
            Custom configuration directory.

        -s NAME, --service=NAME
            Select image hosting service.

        -t NAME, --template=NAME
            Select template for result formatting.

        -T PIXELS, --thumb-size=PIXELS
            Also create thumbnail with given width.

See the [Configuration](#configuration) section for examples
and details on all supported configuration settings.
Without a configuration file, only ``imgur`` is available for uploading,
and you still need to provide access credentials for that.
So be sure to read that section.

``--help`` and ``--version`` print usage and version information, as usual.

``--debug`` activates detailed logging (level ``DEBUG``), and in case of errors
also prints full *Python* tracebacks where normally a simple one-line message is shown.

``--quiet`` hides any result output, so that only the clipboard is filled.

``--verbose`` raises the logging level from the default ``WARNING`` to ``INFO``.
It also enables progress indicators, whatever the configuration says,
unless combined with ``--no-progress``.

``--dry-run`` prevents image uploading and writing to disk
– although screen shots are written to ``/tmp`` anyway.


### Generating and Uploading Screen Shots

If you feed ``hypershot`` with a list of video files, they're first inspected using ``mediainfo``.
Then the requested number of screen shots is taken,
evenly spaced over the video's duration but starting with a small offset.
If only one is requested, it is taken from smack in the middle.

After uploading the generated images, the resulting links are fed into a *Jinja2* template.
To list all available templates, call ``hypershot templates``.

![Output of 'hypershot templates'](https://gitlab.com/kybernetics/hypershot/raw/master/docs/_static/hypershot-templates.png)

Use ``--template`` to select one from the list, or set a default in your configuration.
For more details, see [Templating of Upload Results](#templating-of-upload-results).


### Uploading Existing Images

Besides taking screenshots, you can also upload existing image files explicitly,
via the ``upload`` sub-command. The image links are also fed into the result template,
but no videofile or mediainfo values are available (the ``videos`` value is empty
and thus logically ``False``, so you can check on that in a template).


## Configuration

### Configuration File

Configuration is read from the file ``~/.config/hypershot/config.yaml`` (on Linux, following the XDG spec).
Only [YAML](http://lzone.de/cheat-sheet/YAML) is supported.
You can set a different location for the configuration file using ``--config-dir``,
the file itself is always called either ``config.yaml`` or ``config.yml``.

All command line parameters can be given a custom default via either the configutation file or an environment variable.
Specifically, ``HYPERSHOT_CONFIG_DIR`` can be used to set a different default for the ``--config-dir`` option.

The lookup order is this (first wins):
command line options, environment variables, configuration settings, configuration defaults.

To select a named image hosting service (which can be configured as shown in the next section),
use either ``service: ‹name›`` in the config file, ``HYPERSHOT_SERVICE=‹name›`` in the environment,
or ``-s ‹name›`` on the command line.

*Any* option that takes a value works this way.


### Image Hosters

To list all the image hosting services, both provided as defaults and those added
via the configuration, call ``hypershot services``.

Below you find information on how to configure the built-in ``imgur`` service,
and how to add others to your configuration.

Also see
[this config.yaml](https://gitlab.com/kybernetics/hypershot/blob/master/docs/examples/config.yaml)
for more examples.


#### imgur

To use the built-in ``imgur`` service you need to
[register](https://api.imgur.com/oauth2/addclient) with them.
Select *“Anonymous usage without user authorization”*,
which will give you a *client ID* and a *client secret*.

Add those values to the ``~/.netrc`` file like this:

    machine hypershot:api.imgur.com
        login ‹CLIENT_ID›
        password ‹CLIENT_SECRET›


#### Simple File Upload Sites

If a site basically does a HTML form upload (``multipart/form-data``), use the ``file_upload`` handler.

Consider this example for [https://lut.im/](https://lut.im/):

    services:
      lutim:
        handler: file_upload
        url: "https://lut.im/"
        limit: 5M
        types: [JPG, PNG, BMP, GIF]
        upload_url: "{url}"
        headers:
          Referer: "{url}"
        data:
          delete-day: 0
          crypt: on
        files_field_name: "file"
        response_regex: '<a href="(?P<scheme>[^:]+)://(?P<domain>[^/]+)/(?P<image>[^"]+)"[^>]*><img class="thumbnail'
        image_url: "https://{response[domain]}/{response[image]}"

You can set the HTTP POST request ``headers``,
and add any form ``data`` in addition to the file upload field.
The name of that field must be given in ``files_field_name``.

The provided ``response_regex`` is used to scan a HTTP response of type ``text/html`` or ``text/plain``,
and must contain at least one named group of the form ``(?P<name>...)``.
Those named groups are available in ``response``, in addition to all the handler's settings,
to build an ``image_url`` using the [Python string formatter](https://pyformat.info/#getitem_and_getattr).

In case of a JSON response, you can use ``json`` instead of ``response`` for building your ``image_url``.


#### Chevereto Sites

A good service powered by [Chevereto](https://chevereto.com/) is ``malzo.com``,
because you can use it anonymously
and it has a high size limit of 30 MiB.
If you want to use an account you have there,
the next paragraph shows you how
– otherwise leave out the ``login`` attribute.

Here is an example including user account credentials
– these settings go into ``config.yaml`` like all other ones:

    services:
      malzo:
        handler: chevereto
        url: "https://malzo.com"
        limit: 30M
        types: [JPG, PNG, BMP, GIF]
        login: .netrc

In this example, the special value ``.netrc`` means
the username and password are kept separate in the ``~/.netrc`` file,
which is commonly used to store credentials for FTP access and similar services.
Otherwise, provide ``login`` and ``password`` in the YAML file directly.

So also add this to the ``~/.netrc`` file:

    machine hypershot:malzo.com
        login YOURNAME
        password KEEP_ME_SECRET

This file must be private, therefor call ``chmod 0600 ~/.netrc`` after you initially create it.


### Logging Configuration

The Python logging system can be configured by one of the files
`logging.yaml`, `logging.yml`, or `logging.ini`.
They must be located in the configuration directory,
and are checked in the mentioned order.

Consult the [Python Guide](http://python-guide-pt-br.readthedocs.io/en/latest/writing/logging/#logging-in-an-application)
and the [Logging How-To](https://docs.python.org/3/howto/logging.html#basic-logging-tutorial)
for details on the logging machinery and its configuration.
For the YAML files, the *dictionary* method applies (using ``dictConfig``),
see [this logging.yaml](https://gitlab.com/kybernetics/hypershot/blob/master/docs/examples/logging.yaml)
for a full example.

The logging level threshold of the root logger depends
on the values of ``debug`` (``DEBUG``) and ``verbose`` (``INFO``)
– if neither is set, the level is ``WARNING``.


## Templating of Upload Results

### Templating Introduction

As mentioned earlier, after uploading image files,
the resulting links are fed into a *Jinja2* template.

To list all the currently defined templates,
use the ``hypershot templates`` command.

Template file names always end with a ``.j2`` extension.
Built-in ones can be overridden by placing a file with the same name
in the configuration directory.

You can also pass the path of an existing file with the ``-t`` option,
then the template can be located anywhere.

If you want to write your own templates,
or have some error in an existing one,
the ``yaml`` and ``json`` templates come in handy.
They dump all the keys and values available to a template
as a YAML or JSON document, so you can see what's where.


### Writing Custom Templates

See the [Jinja homepage](http://jinja.pocoo.org/) for the full documentation
of the template engine. You might not need it at all, if the
available built-in templates serve your needs – then just skip this section.

Here's the built-in ``bbcode.j2`` template as an example:

    {# Simple BBcode Template [built-in] #}
    {%- for image in images -%}
    [img]{{ image.hypershot.link }}[/img]
    {% endfor %}

Start your own templates with a comment line like shown,
so they get a proper description in ``hypershot templates``.

These additional utility functions are available:

* ``u.context`` – The Jinja2 context object, make sure you understand what you're doing when accessing this.
* ``u.namespace`` – A shallow copy of the Jinja2 template namespace, without helper functions.

And these are the custom filters:

* ``json`` – Dump the value as JSON document.
* ``mask_secrets`` – Replace any secret values (passwords) with question marks.
* ``re_sub(pattern, repl)`` – Substitute regular expression matches with the text in ``repl``.
* ``repr`` – Apply Python's ``repr``.
* ``yaml`` – Dump the value as YAML document.


## Working with the Source Code

### Creating a Working Directory

    deactivate 2>/dev/null
    pip3 --version || sudo apt-get install python3-pip
    xargs -n1 pip3 install --user -U <<<"pip tox"

    # Use "git@gitlab.com:kybernetics/hypershot.git" if you have developer access
    git clone "https://gitlab.com/kybernetics/hypershot.git"
    cd hypershot && ~/.local/bin/tox -e $_
    . .env


### Building the Documentation Locally

To build the *Sphinx* documentation, call ``tox -e docs``.
On success, the index page can be found at ``docs/_build/html/index.html``.


### Releasing to PyPI

Building and uploading a (pre-)release:

    # pre-release
    next=$(( 1 + $(grep ^tag_build setup.cfg | tr -cd 0-9) ))
    sed -i -e 's/^\(tag_build = .dev\).*/\1'$next'/' setup.cfg

    # release
    sed -i -re 's/^(tag_[a-z ]+=)/##\1/' setup.cfg
    version="$(./setup.py --version)"
    git commit -m "Release $version" setup.cfg
    git push

    git tag -a "v$version" -m "Release $version"
    git push --tags

    # build & upload
    rm -rf dist
    ./setup.py sdist bdist_wheel
    twine upload --config-file setup.cfg dist/*.{zip,whl}

    # post release
    bumpversion --list minor
    sed -i -e 's/^##\(tag_build =\).*/\1 .dev1/' setup.cfg
    git ci -m "bump to $(./setup.py --version).dev1 after $version release" setup.cfg src/*/__init__.py


## Links

 * [docopt Manual](http://docopt.org/)
 * [A hands-on introduction to video technology](https://github.com/leandromoreira/digital_video_introduction#intro)
