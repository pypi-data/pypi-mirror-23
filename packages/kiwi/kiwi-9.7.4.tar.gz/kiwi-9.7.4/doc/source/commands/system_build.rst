kiwi system build
=================

SYNOPSIS
--------

.. code-block:: bash

   kiwi [global options] service <command> [<args>]

   kiwi system build -h | --help
   kiwi system build --description=<directory> --target-dir=<directory>
       [--allow-existing-root]
       [--clear-cache]
       [--ignore-repos]
       [--set-repo=<source,type,alias,priority>]
       [--add-repo=<source,type,alias,priority>...]
       [--obs-repo-internal]
       [--add-package=<name>...]
       [--delete-package=<name>...]
       [--signing-key=<key-file>...]
   kiwi system build help

DESCRIPTION
-----------

build an image in one step. The build command combines kiwi's prepare and
create steps in order to build an image with just one command call. The
build command creates the root directory of the image below
`<target-dir>/build/image-root` and if not specified differently writes
a log file `<target-dir>/build/image-root.log`. The result image files
are created in the specified target-dir.

OPTIONS
-------

--add-package=<name>

  specify package to add(install). The option can be specified
  multiple times

--add-repo=<source,type,alias,priority>

  Add a new repository to the existing repository setup in the XML
  description. This option can be specified multiple times

--allow-existing-root

  Allow to use an existing root directory from an earlier
  build attempt. Use with caution this could cause an inconsistent
  root tree if the existing contents does not fit to the
  former image type setup

--clear-cache

  delete repository cache for each of the used repositories
  before installing any package. This is useful if an image build
  should take and validate the signature of the package from the
  original repository source for any build. Some package managers
  unconditionally trust the contents of the cache, which is ok for
  cache data dedicated to one build but in case of kiwi the cache
  is shared between multiple image builds on that host for performance
  reasons.

--signing-key=<key-file>

  set the key file to be trusted and imported into the package
  manager database before performing any opertaion. This is useful
  if an image build should take and validate repository and package
  signatures during build time. This option can be specified multiple
  times

--delete-package=<name>

  specify package to delete. The option can be specified
  multiple times

--description=<directory>

  Path to the XML description. This is a directory containing at least
  one _config.xml_ or _*.kiwi_ XML file.

--obs-repo-internal

  The repository source type **obs://** by default points to the
  `Open Build Service <http://download.opensuse.org>`_. With the
  *--obs-repo-internal* option the source type is changed to the
  **ibs://** type, pointing to the **Internal Build Service**.
  This allows to build images with repositories pointing to the SUSE
  internal build service. Please note this requires access permissions
  to the SUSE internal build service on the machine building the image.

--set-repo=<source,type,alias,priority>

  Overwrite the first repository entry in the XML description with the
  provided information:

  - **source**

    source url, pointing to a package repository which must be in a format
    supported by the selected package manager. See the URI_TYPES section for
    details about the supported source locators.

  - **type**

    repository type, could be one of `rpm-md`, `rpm-dir` or `yast2`.

  - **alias**

    An alias name for the repository. If not specified kiwi calculates
    an alias name as result from a sha sum. The sha sum is used to uniquely
    identify the repository, but not very expressive. We recommend to
    set an expressive and uniq alias name.

  - **priority**

    A number indicating the repository priority. How the value is evaluated
    depends on the selected package manager. Please refer to the package
    manager documentation for details about the supported priority ranges
    and their meaning.

--target-dir=<directory>

  Path to store the build results.

URI_TYPES
---------

- **http://** | **https://** | **ftp://**

  remote repository delivered via http or ftp protocol.

- **obs://**

  Open Buildservice repository. The source data is translated into
  an http url pointing to http://download.opensuse.org.

- **ibs://**

  Internal Open Buildservice repository. The source data is translated into
  an http url pointing to download.suse.de.

- **iso://**

  Local iso file. kiwi loop mounts the file and uses the mount point
  as temporary directory source type

- **dir://**

  Local directory
