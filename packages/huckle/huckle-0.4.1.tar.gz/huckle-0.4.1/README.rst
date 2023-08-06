Huckle (hypermedia unified CLI... with a kick)
============================================

Huckle is a CLI that can act as an impostor for any CLI expressed via hypertext
command line interface (HCLI) semantics.

----

As is normally seen with any well-behaved client/server interaction under REST,
all changes published by the server are distributed to all clients without there
being a need to update the client as the API changes. This is used to huckle's
advantage and this benefit is brought to the command line interface and the
unix/linux shell.

Given that most programming languages have a way to issue shell commands, such
APIs become readily consumable anywhere, and can be experimented with quickly
by developers, with Huckle's help.

Huckle provides a dynamic view of the documentation, commands, options and
parameters that can be issued to an HCLI API it interacts with.

The standard HCLI Internet-Draft [1] is a work in progress by the author.

The current implementation leverages hal+json alongside a static form of ALPS
(semantic profile) [2] to help enable widespread cross media-type support.

You can access an simple example HCLI server to play with huckle [3]

Help shape huckle and HCLI on the discussion list [4] or by raising issues on github!

[1] https://github.com/cometaj2/I-D/tree/master/hcli

[2] http://alps.io

[3] https://hcli.io

[4] https://groups.google.com/forum/#!forum/huck-hypermedia-unified-cli-with-a-kick

Install Python, pip and huckle
-------------------

Huckle requires bash with access to man pages, Python 2.7 and pip

  - Install Python 2.7 for your system

Install pip (if it didn't get install alongside Python). For example:

  - curl -O https://bootstrap.pypa.io/get-pip.py
  - python get-pip.py

Install huckle

  - pip install huckle

Usage
-----

huckle create <cliname>

    This creates an new cliname alias and configuration file. Once a CLI is created via huckle,
    it can be invoked by name directly after restarting the terminal.
   
    Note that an existing configuration file is left alone if the command is run multiple times 
    for the same cliname.

huckle cli <cliname>

    This invokes the cliname to issue HCLI API calls; the details of which are left to API implementers.
    
    Commands, options and parameters are presented gradually, to provide users with a way to
    incrementally discover and learn how the CLI is used.

<cliname> ... help

    The reserved "help" command can be used anywhere in a command line sequence to have huckle generate
    a man page from the last successfully received HCLI Document. This helps with CLI exploration.

huckle help

    This opens up a man page that describes how to use huckle.

Configuration
-------------

Huckle uses the ~/.bash_profile to defer to a ~/.huckle/huckle_profile for CLI aliases; to avoid
crowding the ~/.bash_profile and to facilitate cleanup if huckle is uninstalled.

Huckle also uses CLI configuration files (e.g. ~/.huckle/<cliname>/config) to associate a specific
CLI to a hypermedia API URL root and other CLI specific configuration.

Each CLI configuration file contains:
    - A URL to the root of the hypermedia CLI API

An example CLI that can be used with Huckle is available on hcli.io.
    - https://hcli.io/hcli-webapp/cli/jsonf?command=jsonf (HCLI root)  
    - https://hcli.io/hal/#/hcli-webapp/ (HAL Browser navigation)  

Versioning
----------

Huckle uses semantic versioning (http://semver.org) and may make use of the "prealphax", "alphax"
"betax", and "rcx" extensions where x is a number (e.g. 0.3.0-prealpha1) on github. Only full
major.minor.patch releases will be pushed to pip from now on.

Supports
--------

- Automatic man page document generation with the "help" command.
- HCLI version 1.0 semantics for:

    - hal+json

- Command line execution responses for:

    - All media types

- Streaming:
 
    - Handles very large stdin/stdout streams (fixed chunk size of 16834)

- Error output to stderr on client response status code >= 400

- SOCKS tunneling through environment variables (ALL_PROXY)

To Do
-----
- Fork restnavigator repo or otherwise adjust to use restnavigator with requests (single http client instead of two)

- Support help docs output in the absence of man pages (e.g. git-bash on Windows)

- Support immediate use of a CLI created through huckle create <cliname> (instead of having to restart the terminal)

- Support HCLI version 1.0 semantics for: 

    - Collection+JSON
    - hal+xml
    - HTML
    - Siren
    - JSON API
    - JSON-LD
    - Mason

- Support stream configuration

    - sending and receiving streams (configurable via CLI config)
    - sending and receiving non-streams (configuration via CLI config)
    - chunk size for streams send/receive (configurable via CLI config)

- Support non-stream send/receive (via CLI configuration)

- Support various authentication per CLI configuration  

    - HTTP Basic Auth  
    - HTTP Digest  
    - Oauth  
    - X509 (HTTPS mutual authentication)  
    - AWS
    - SAML 

- Support server certificate validation bypass (e.g. --ssl-no-verify. This is not secure but is sometimes useful to troubleshoot)  

- Support auto configuration of an hcli when providing a url to an HCLI document (e.g. huckle get https://hcli.io/hcli-webapp/cli/jsonf?command=jsonf)  

- Support forward proxy configuration through proxy environment variables (HTTP_PROXY, HTTPS_PROXY)

- Support hcli name conflic resolution (brainstorm implementation; alias or rename?)

Bugs
----

None are known... so far.
