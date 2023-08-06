.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/collective.pantry.svg?branch=master
    :target: https://travis-ci.org/collective/collective.pantry

=================
collective.pantry
=================

The main objective of this product is to make it easy for integrators to enable
TinyMCE templates (user addable HTML snippets) in your RichText fields and
tiles. These HTML snippets can be added using two approaches. You can define
theme defined snippets, idealy defined by the themer or designer. In addition,
you can also enable the users to be able to define their own HTML snippets
using the content type provided.

The snippets are available from the template button on TinyMCE, ready to be
used.

It also enables the "Pantry". It's a summary view of Plone style elements along
with the theme and user snippets. It's an update of the good old
`test_rendering` view.

Theme Snippets
--------------

They are defined as HTML files in a directory called `pantry`. The format is
plain HTML. At a later point, you can also override them or add more theme
snippets if you customize the theme using the Plone Theme editor.

User Snippets
-------------

This product makes available a content type called `snippet`. Each snippet is a
page-like object that defines a single snippet. They are meant to be
user-defined. As any other content type, you can give the users permissions
over them, or disable them completely, depending on your use case.

Installation
------------

Install collective.pantry by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.pantry


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.pantry/issues
- Source Code: https://github.com/collective/collective.pantry
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
