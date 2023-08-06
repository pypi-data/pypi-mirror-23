try:
    # Uset setuptools if available to prevent "UserWarning: Unknown distribution option: 'entry_points'"
    from setuptools import setup
except ImportError:
    from distutils.core import setup

"""

Release protocol:

1. Make sure all tests passes in the dev environment ``pptx-downsizer-dev``, 
   installed in "editable" mode with ``pip install -e .``.
   Verify that all entry points are functional and able to successfully complete.
   Preferably verify that it works both when invoked from console and from Automator scripts.
   Also test that the setup.py and README.md is working (``docutils`` must be installed):
   ``python setup.py check --restructuredtext``

2. Bump version number (``version``+``download_url`` in ``setup.py`` and ``version`` in ``pptx_downsizer/__init__.py``),
   then ``git commit``.

3. Build release:
    (a) Change to dedicated build/dist environment, e.g. ``pptx-downsizer-build-test``:
        ``source activate pptx-downsizer-build-test``
    (b) Clear the old version: ``pip uninstall pptx-downsizer`` (or do a complete swipe).
    (c) Go to project root directory in terminal and build release with ``python setup.py sdist``,
    (d) Install build in sdist environment using ``pip install dist/pptx-downsizer-<version>.tar.gz``,
    (e) Run tests and verify that all entry points are working.

4. Register upload release and source distribution to PyPI test site:
   ``python setup.py sdist upload -r pypitest_legacy``,
   then check https://testpypi.python.org/pypi/pptx-downsizer/ and make sure it looks right.
   Note: Previously, this was a two-step process, requiring pre-registration with 
   ``python setup.py register -r pypi(test)``. This is no longer needed.  

5. Register and upload release to production PyPI site and check https://pypi.python.org/pypi/pptx-downsizer/
   ``python setup.py sdist upload -r pypi``.

6. Tag this version in git with ``git tag <version> -m "message"``, then push it with
   ``git push --follow-tags`` (or ``git push --tags`` if you have already pushed the branch/commits)
   You can also create tags/releases using GitHub's interface, c.f. https://help.github.com/articles/creating-releases/.

7. Test the PYPI release using the ``pptx-downsizer-pypi-test`` environment,
   preferably also on a different platforms as well (Windows/Mac/Linux).
   Use ``pip install -U pptx-downsizer`` to update.

8. Update ``version`` again, adding "-dev" postfix.

If you find an error at any point, go back to step 1.


Regarding PyPI and packaging/distribution:
* You can use a .pypirc to configure server/username/password (can be configured globally in ~/.pypirc).
* https://wiki.python.org/moin/TestPyPI
* https://wiki.python.org/moin/CheeseShopTutorial
* https://packaging.python.org/tutorials/distributing-packages/
* https://mail.python.org/pipermail/distutils-sig/2017-June/030766.html
* http://inre.dundeemt.com/2014-05-04/pypi-vs-readme-rst-a-tale-of-frustration-and-unnecessary-binding/  (OLD)
* http://python-packaging.readthedocs.io/en/latest/metadata.html
* https://docs.python.org/devguide/documenting.html

Regarding reStructuredText and Markdown:
* http://docutils.sourceforge.net/rst.html
* Markdown to rST using Pandoc: ``pandoc --from=markdown --to=rst --output=README.rst README.md``
* Fix line wrap using pandoc: ``pandoc README.rst -o README.rst`` [may also change a lot of other stuff!]
* Using docutils: ``python setup.py check --restructuredtext``
* Linting using restructuredtext_lint: ``rst-lint README.rst``
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* https://en.support.wordpress.com/markdown-quick-reference/
* http://www.sphinx-doc.org/en/stable/rest.html
* http://docutils.sourceforge.net/docs/user/rst/quickstart.html
* http://docutils.sourceforge.net/rst.html
* https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html


"""

# try:
#     import pypandoc
#     long_description = pypandoc.convert_file('README.md', 'rst')
#     long_description = long_description.replace("\r", "")
# except (ImportError, OSError):
#     print("NOTE: pypandoc not available, reading README.md as-is.")
# Edit, switched to using reStructuredText for README file:
long_description = open('README.rst').read()


# update 'version' and 'download_url', as well as pptx_downsizer.__init__.__version__
setup(
    name='pptx-downsizer',
    description='Tool for downsizing Microsoft PowerPoint pptx presentations.',
    long_description=long_description,
    url='https://github.com/scholer/pptx-downsizer',
    packages=['pptx_downsizer'],  # List all packages (directories) to include in the source dist.
    version='0.1.1',  # Update for each new version
    download_url='https://github.com/scholer/pptx-downsizer/tarball/0.1.1',  # Update for each new version
    # download_url='https://github.com/scholer/pptx_downsizer/archive/master.zip',
    author='Rasmus Scholer Sorensen',
    author_email='rasmusscholer@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    keywords=[
        "pptx",
        "PowerPoint",
        "compression",
        "downsizing",
        "file size reduction",
    ],
    # Automatic script creation using entry points has largely super-seeded the "scripts" keyword.
    # you specify: name-of-executable-script: module[.submodule]:function
    # When the package is installed with pip, a script is automatically created (.exe for Windows).
    # Note: The entry points are stored in ./<package name>.egg-info/entry_points.txt, which is used by pkg_resources.
    entry_points={
        'console_scripts': [
            # These should all be lower-case, else you may get an error when uninstalling:
            'pptx_downsizer=pptx_downsizer.pptx_downsizer:cli',
        ],
    },
    # install_requires: Minimal requirement for this project.
    # (Whereas `requirements.txt` is typically used to produce a comprehensive python environment.)
    install_requires=[
        'pyyaml',
        'pillow',
    ],
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        # 'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Healthcare Industry',

        # 'Topic :: Software Development :: Build Tools',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Office Suites',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Environment :: Console',

        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
    ],

)
