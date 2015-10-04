Gloss Project
==============

A design process

One of the key tools of the project is a theme which uses special gloss classes.

CONSIDERED ALPHA: This project is considered in an alpha stage. This is because  we still need more comprehensive documentation. We are adding documentation as we go and when it is ready we will move the status to Beta.

For the most up-to-date reference documentation visit http://the-gloss-project.readthedocs.org/en/latest/

See the `INSTALL` docs

Gloss for Plone 5
---------------------

Gloss 0.8.x is for Plone 5.

Gloss for Plone 4.3.x
-----------------------

If you are on Plone 4.3.x make sure to use a version less than 0.8.x.

Gloss Classes
--------------------

The general approach is to use a gl namespace.
So class will be always named in the manner below::

            {gl namespace}-{what}-n{qualifier}

classes provided::

            core classes:
            ==============
            a.gl-logo (must be placed on an a tag, this is to preserve home link)
            {gl namespace}-{what}-n{qualifier}
            .gl-menu-link - add style to individual menu items
            .gl-inner-only - (deprecated will be removed soon) only show on inner pages
            .gl-front-only - (deprecated will be removed soon) only show on the frontpage
            .gl-editbar - adds an edit bar
            .gl-content - inserts the site content
            .gl-content-body
            .gl-content-byline
            .gl-content-description
            .gl-content-title
            .gl-footer
            .gl-below-content

            drop classes:
            ==============
            .gl-drop
            .gl-front-drop
            .gl-inner-drop

            layout classes:
            ================
            .gl-one-column-layout
            .gl-two-column-layout.gl-right-sidebar
            .gl-two-column-layout.gl-left-sidebar
            .gl-two-column-layout.gl-right-column (deprecated will be removed soon)
            .gl-two-column-layout.gl-left-column (deprecated will be removed soon)
            .gl-three-column-layout
            
                 .gl-second-column
                 .gl-first-column
