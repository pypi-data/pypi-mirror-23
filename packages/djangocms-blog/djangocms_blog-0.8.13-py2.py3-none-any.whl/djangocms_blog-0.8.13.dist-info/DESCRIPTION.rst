==============
djangocms-blog
==============

.. image:: https://img.shields.io/pypi/v/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-blog
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-blog
    :alt: Monthly downloads

.. image:: https://img.shields.io/pypi/pyversions/djangocms-blog.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-blog
    :alt: Python versions

.. image:: https://img.shields.io/travis/nephila/djangocms-blog.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-blog
    :alt: Latest Travis CI build status

.. image:: https://img.shields.io/coveralls/nephila/djangocms-blog/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-blog?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/codecov/c/github/nephila/djangocms-blog/develop.svg?style=flat-square
    :target: https://codecov.io/github/nephila/djangocms-blog
    :alt: Test coverage

.. image:: https://codeclimate.com/github/nephila/djangocms-blog/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-blog
   :alt: Code Climate

django CMS blog application - Support for multilingual posts, placeholders, social network meta tags and configurable apphooks.

Supported Django versions:

* Django 1.6
* Django 1.7
* Django 1.8
* Django 1.9

Supported django CMS versions:

* django CMS 3.x

.. warning:: Version 0.8 will be the last one supporting Python 2.6, Python 3.3,
             Django<1.8 and django CMS<3.2.

.. warning:: Starting from version 0.8, date_published is not set anymore
             when creating a post but rather when publishing.
             This does not change the overall behavior, but be warned if you
             expect it to be not null in custom code.

.. warning:: Version 0.6 changes the field of LatestPostsPlugin.tags field.
             A datamigration is in place to migrate the data, but check that
             works ok for your project before upgrading, as this might delete
             some relevant data.
             Some plugins have a broken tag management prior to 0.6, in case
             you have issues with tags, upgrade to latest version to have it fixed.

*****************************************
Upgrading cmsplugin-filer from 1.0 to 1.1
*****************************************

Due to changes in cmsplugin-filer/filer which moved ``ThumbnailOption`` model from the
former to the latter, ``djangocms-blog`` must be migrated as well.

Migrating cmsplugin-filer to 1.1 and djangocms-blog up to 0.8.4
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you have djangocms-blog up to 0.8.4 (included) installed or you are upgrading from a previous
djangocms-blog version together with cmsplugin-filer upgrade, you can just apply the migrations::

    pip install cmsplugin-filer==1.1.3 django-filer==1.2.7 djangocms-blog==0.8.4
    python manage.py migrate

Migrating cmsplugin-filer to 1.1 and djangocms-blog 0.8.5+
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you already a djangocms-blog 0.8.5+ up to 0.8.11, upgrade to 0.8.11, then 
you have to de-apply some blog migrations when doing the upgrade::

    pip install djangocms-blog==0.8.11
    python manage.py migrate djangocms_blog 0017 ## reverse for these migration is a noop
    pip install cmsplugin-filer==1.1.3 django-filer==1.2.7
    python manage.py migrate

After this step you can upgrade to 0.8.12::

    pip install djangocms-blog==0.8.12

.. note:: de-apply migration **before** upgrading cmsplugin-filer. If running before upgrade, the
          backward migration won't alter anything on the database, and it will just allow the code
          to migrate ``ThumbnailOption`` from cmsplugin-filer to filer

.. note:: If you upgrade in a Django 1.10 environment, be sure to upgrade both packages
          at the same time to allow correct migration dependencies to be evaluated.

Installing djangocms-blog in an existing project with Django 1.10
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If your project has cmsplugin-filer 1.1+ already installed and it uses Django 1.10, 
install djangocms-blog 0.8.12 (and above)::

    pip install djangocms-blog==0.8.12

********
Features
********

* Placeholder content editing
* Frontend editing using django CMS 3.x frontend editor
* Multilingual support using django-parler
* Support for Twitter cards, Open Graph and Google+ snippets meta tags
* Optional support for simpler TextField-based content editing
* Multisite support (posts can be visible in one or more Django sites on the
  same project)
* Per-Apphook configuration
* Configurable permalinks
* Configurable django CMS menu support
* Per-Apphook templates set
* Auto Apphook setup
* Django sitemap framework support
* Support for django CMS 3.2+ Wizard
* Haystack index support

**********
Quickstart
**********

django CMS blog assumes a completely setup and working django CMS project.
See `django CMS installation docs`_ for reference.

Install djangocms-blog::

    pip install djangocms-blog

or -when installing in Django 1.6/1.7::

    pip install djangocms-blog[admin-enhancer]

Add ``djangocms_blog`` and its dependencies to INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'filer',
        'easy_thumbnails',
        'aldryn_apphooks_config',
        'cmsplugin_filer_image',
        'parler',
        'taggit',
        'taggit_autosuggest',
        'meta',
        'djangocms_blog',
        ...
    ]

If you installed the **admin-enhancer** variant, add ``admin_enhancer`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'admin_enhancer',
        ...
    ]


Then sync and migrate::

    $ python manage.py syncdb
    $ python manage.py migrate

External applications configuration
+++++++++++++++++++++++++++++++++++

Dependency applications may need configuration to work properly.

Please, refer to each application documentation on details.

* django-cms: http://django-cms.readthedocs.io/en/release-3.4.x/how_to/install.html
* django-filer: http://django-filer.readthedocs.org
* django-meta: https://github.com/nephila/django-meta#installation
* django-meta-mixin: https://github.com/nephila/django-meta-mixin#installation
* django-parler: http://django-parler.readthedocs.org/en/latest/quickstart.html#configuration
* django-taggit-autosuggest: https://bitbucket.org/fabian/django-taggit-autosuggest

Quick hint
++++++++++

The following are minimal defaults to get the blog running; they may not be
suited for your deployment.

* Add the following settings to your project::

    SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
        'taggit': 'taggit.south_migrations',
    }
    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )
    META_SITE_PROTOCOL = 'http'
    META_USE_SITES = True

* If you are using Django 1.7+, be aware that ``filer`` < 0.9.10,
  ``cmsplugin_filer`` and ``django-cms`` < 3.1 currently requires you to
  setup ``MIGRATION_MODULES`` in settings::

    MIGRATION_MODULES = {
       'cms': 'cms.migrations_django', # only for django CMS 3.0
       'menus': 'menus.migrations_django',  # only for django CMS 3.0
       'filer': 'filer.migrations_django',  # only for django filer up to 0.9.9
       'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    }

  Please check
  `django CMS installation <http://django-cms.readthedocs.org/en/support-3.0.x/how_to/integrate.html#installing-and-configuring-django-cms-in-your-django-project>`_,
  `cmsplugin-filer README <https://github.com/stefanfoulis/cmsplugin-filer#installation>`_
  for detailed information.

* Configure parler according to your languages::

    PARLER_LANGUAGES = {
        1: (
            {'code': 'en',},
            {'code': 'it',},
            {'code': 'fr',},
        ),
        'default': {
            'fallbacks': ['en', 'it', 'fr'],
        }
    }

* Add the following to your ``urls.py``::

    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

* To start your blog you need to use `AppHooks from django CMS <http://django-cms.readthedocs.org/en/support-3.0.x/how_to/apphooks.html>`_
  to add the blog to a django CMS page; this step is not required when using
  `Auto setup <auto_setup>`_:

  * Create a new django CMS page
  * Go to **Advanced settings** and select Blog from the **Application** selector and
    create an **Application configuration**;
  * Eventually customise the Application instance name;
  * Publish the page
  * Restart the project instance to properly load blog urls.

.. warning:: After adding the apphook to the page you **cannot** change the **Instance Namspace**
             field for the defined **AppHokConfig**; if you want to change it, create a new one
             with the correct namespace, go in the CMS page **Advanced settings** and switch to the
             new **Application configuration**

* Add and edit blog by creating them in the admin or using the toolbar,
  and the use the `django CMS frontend editor <http://django-cms.readthedocs.org/en/support-3.0.x/user/reference/page_admin.html#the-interface>`_
  to edit the blog content:

  * Create a new blog entry in django admin backend or from the toolbar
  * Click on "view on site" button to view the post detail page
  * Edit the post via djangocms frontend by adding / editing plugins
  * Publish the blog post by flagging the "Publish" switch in the blog post
    admin

Configurable permalinks
+++++++++++++++++++++++

Blog comes with four different styles of permalinks styles:

* Full date: ``YYYY/MM/DD/SLUG``
* Year /  Month: ``YYYY/MM/SLUG``
* Category: ``CATEGORY/SLUG``
* Just slug: ``SLUG``

As all the styles are loaded in the urlconf, the latter two does not allow
to have CMS pages beneath the page the blog is attached to. If you want to
do this, you have to override the default urlconfs by setting something
like the following in the project settings::

    BLOG_PERMALINK_URLS = {
        'full_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        'short_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        'category': r'^post/(?P<category>\w[-\w]*)/(?P<slug>\w[-\w]*)/$',
        'slug': r'^post/(?P<slug>\w[-\w]*)/$',
    }

And change ``post/`` with the desired prefix.

Attaching blog to the home page
+++++++++++++++++++++++++++++++

If you want to attach the blog to the home page you have to adapt settings a bit otherwise the
"Just slug" permalink will swallow any CMS page you create.

To avoit this add the following settings to you project::

    BLOG_AVAILABLE_PERMALINK_STYLES = (
        ('full_date', _('Full date')),
        ('short_date', _('Year /  Month')),
        ('category', _('Category')),
    )
    BLOG_PERMALINK_URLS = {
        'full_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        'short_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        'category': r'^(?P<category>\w[-\w]*)/(?P<slug>\w[-\w]*)/$',
    }

Notice that the last permalink type is no longer present.

Then, pick any of the three remaining permalink types in the layout section of the apphooks config
linked ot the home page (see http://yoursite.com/admin/djangocms_blog/blogconfig/).'

Menu
++++

``djangocms_blog`` provides support for django CMS menu framework.

By default all the categories and posts are added to the menu, in a hierarchical structure.

It is possibile to configure per Apphook, whether the menu includes post and categories
(the default), only categories, only posts or no item.

If "post and categories" or "only categories" are set, all the posts not associated with a
category are not added to the menu.

Templates
+++++++++

To ease the template customisations a ``djangocms_blog/base.html`` template is
used by all the blog templates; the templates itself extends a ``base.html``
template; content is pulled in the ``content`` block.
If you need to define a different base template, or if your base template does
not defines a ``content`` block, copy in your template directory
``djangocms_blog/base.html`` and customise it according to your needs; the
other application templates will use the newly created base template and
will ignore the bundled one.

Templates set
+++++++++++++

By using **Apphook configuration** you can define a different templates set.
To use this feature provide a directory name in **Template prefix** field in
the **Apphook configuration** admin (in *Layout* section): it will be the
root of your custom templates set.

.. _auto_setup:

Auto setup
++++++++++

``djangocms_blog`` can install and configue itself if it does not find any
attached instance of itself.
This feature is enable by default and will create:

* a ``BlogConfig`` with default values
* a ``Blog`` CMS page and will attach ``djangocms_blog`` instance to it
* a **home page** if no home is found.

All the items will be created in every language configured for the website
and the pages will be published. If not using **aldryn-apphook-reload** or
**django CMS 3.2** auto-reload middleware you are required to reload the
project instance after this.
This will only work for the current website as detected by
``Site.objects.get_current()``.


The auto setup is execute once for each server start but it will skip any
action if a ``BlogConfig`` instance is found.


Sitemap
+++++++

``djangocms_blog`` provides a sitemap for improved SEO indexing.
Sitemap returns all the published posts in all the languages each post is available.

The changefreq and priority is configurable per-apphook (see ``BLOG_SITEMAP_*`` in
`Global settings <settings>`_).

To add the blog Sitemap, add the following code to the project ``urls.py``::


    from cms.sitemaps import CMSSitemap
    from djangocms_blog.sitemaps import BlogSitemap


    urlpatterns = patterns(
        '',
        ...
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
            {'sitemaps': {
                'cmspages': CMSSitemap, 'blog': BlogSitemap,
            }
        }),
    )

Multisite
+++++++++

django CMS blog provides full support for multisite setups.

Each blog post can be assigned to none, one or more sites: if no site is selected, then
it's visible on all sites.

This is matched with and API that allows to restrict users to only be able to edit
blog posts only for some sites.

To implement this API, you must add a ``get_sites`` method on the user model which
returns a queryset of sites the user is allowed to add posts to.

Example::

    class CustomUser(AbstractUser):
        sites = models.ManyToManyField('sites.Site')

        def get_sites(self):
            return self.sites


django CMS 3.2+ Wizard
++++++++++++++++++++++

django CMS 3.2+ provides a content creation wizard that allows to quickly created supported
content types, such as blog posts.

For each configured Apphook, a content type is added to the wizard.

Some issues with multiple registrations raising django CMS ``AlreadyRegisteredException``
hae been reported; to handle these cases gracefully, the exception is swallowed
when Django ``DEBUG == True`` avoiding breaking production websites. In these cases they
wizard may not show up, but the rest will work as intended.

django-knocker
++++++++++++++

``djangocms-blog`` is integrated with `django-knocker <https://github.com/nephila/django-knocker>`_
to provide real time desktop notifications.

See `django-knocker documentation <https://django-knocker.readthedocs.org/>`_ for how to configure
knocker.

.. _settings:

***************
Global Settings
***************
* BLOG_IMAGE_THUMBNAIL_SIZE: Size of the main image when shown on the post
  lists; it's a dictionary with ``size``, ``crop`` and ``upscale`` keys;
  (default: ``{'size': '120x120', 'crop': True,'upscale': False}``)
* BLOG_IMAGE_FULL_SIZE: Size of the main image when shown on the post
  detail; it's a dictionary with ``size``, ``crop`` and ``upscale`` keys;
  (default: ``{'size': '640x120', 'crop': True,'upscale': False}``)
* BLOG_PAGINATION: Number of post per page; (default: ``10``)
* BLOG_LATEST_POSTS: Default number of post in the **Latest post** plugin;
  (default: ``5``)
* BLOG_POSTS_LIST_TRUNCWORDS_COUNT: Default number of words shown for
  abstract in the post list; (default: ``100``)
* BLOG_TYPE: Generic type for the post object; (default: ``Article``)
* BLOG_TYPES: Choices of available blog types;
  (default: to ``META_OBJECT_TYPES`` defined in `django-meta-mixin settings`_)
* BLOG_FB_TYPE: Open Graph type for the post object; (default: ``Article``)
* BLOG_FB_TYPES: Choices of available blog types;
  (default: to ``META_FB_TYPES`` defined in `django-meta-mixin settings`_)
* BLOG_FB_APPID: Facebook Application ID
* BLOG_FB_PROFILE_ID: Facebook profile ID of the post author
* BLOG_FB_PUBLISHER: Facebook URL of the blog publisher
* BLOG_FB_AUTHOR_URL: Facebook profile URL of the post author
* BLOG_FB_AUTHOR: Facebook profile URL of the post author
* BLOG_TWITTER_TYPE: Twitter Card type for the post object;
  (default: ``Summary``)
* BLOG_TWITTER_TYPES: Choices of available blog types for twitter;
  (default: to ``META_TWITTER_TYPES`` defined in `django-meta-mixin settings`_)
* BLOG_TWITTER_SITE: Twitter account of the site
* BLOG_TWITTER_AUTHOR: Twitter account of the post author
* BLOG_GPLUS_TYPE: Google+ Snippet type for the post object;
  (default: ``Blog``)
* BLOG_GPLUS_TYPES: Choices of available blog types for twitter;
  (default: to ``META_GPLUS_TYPES`` defined in `django-meta-mixin settings`_)
* BLOG_GPLUS_AUTHOR: Google+ account of the post author
* BLOG_ENABLE_COMMENTS: Whether to enable comments by default on posts;
  while ``djangocms_blog`` does not ship any comment system, this flag
  can be used to control the chosen comments framework; (default: ``True``)
* BLOG_USE_ABSTRACT: Use an abstract field for the post; if ``False``
  no abstract field is available for every post; (default: ``True``)
* BLOG_USE_PLACEHOLDER: Post content is managed via placeholder;
  if ``False`` a simple HTMLField is used; (default: ``True``)
* BLOG_MULTISITE: Add support for multisite setup; (default: ``True``)
* BLOG_AUTHOR_DEFAULT: Use a default if not specified; if set to ``True`` the
  current user is set as the default author, if set to ``False`` no default
  author is set, if set to a string the user with the provided username is
  used; (default: ``True``)
* BLOG_DEFAULT_PUBLISHED: If posts are marked as published by default;
  (default: ``False``)
* BLOG_ADMIN_POST_FIELDSET_FILTER: Callable function to change(add or filter)
  fields to fieldsets for admin post edit form; (default: ``False``). Function simple example::


    def fieldset_filter_function(fsets, request, obj=None):
        if request.user.groups.filter(name='Editor').exists():
            fsets[1][1]['fields'][0].append('author')  # adding 'author' field if user is Editor
        return fsets


* BLOG_AVAILABLE_PERMALINK_STYLES: Choices of permalinks styles;
* BLOG_PERMALINK_URLS: URLConf corresponding to
  BLOG_AVAILABLE_PERMALINK_STYLES;
* BLOG_DEFAULT_OBJECT_NAME: Default name for Blog item (used in django CMS Wizard);
* BLOG_AUTO_SETUP: Enable the blog **Auto setup** feature; (default: ``True``)
* BLOG_AUTO_HOME_TITLE: Title of the home page created by **Auto setup**;
  (default: ``Home``)
* BLOG_AUTO_BLOG_TITLE: Title of the blog page created by **Auto setup**;
  (default: ``Blog``)
* BLOG_AUTO_APP_TITLE: Title of the ``BlogConfig`` instance created by
  **Auto setup**; (default: ``Blog``)
* BLOG_SITEMAP_PRIORITY_DEFAULT: Default priority for sitemap items; (default: ``0.5``)
* BLOG_SITEMAP_CHANGEFREQ: List for available changefreqs for sitemap items; (default: **always**,
  **hourly**, **daily**, **weekly**, **monthly**, **yearly**, **never**)
* BLOG_SITEMAP_CHANGEFREQ_DEFAULT: Default changefreq for sitemap items; (default: ``monthly``)
* BLOG_CURRENT_POST_IDENTIFIER: Current post identifier in request (default ``djangocms_post_current``)
* BLOG_CURRENT_NAMESPACE: Current post config identifier in request  (default: ``djangocms_post_current_config``)
* BLOG_ENABLE_THROUGH_TOOLBAR_MENU: Is the toolbar menu throught whole all applications (default: ``False``)
* BLOG_PLUGIN_MODULE_NAME: Blog plugin module name (default: ``Blog``)
* BLOG_LATEST_ENTRIES_PLUGIN_NAME: Blog latest entries plugin name (default: ``Latest Blog Articles``)
* BLOG_AUTHOR_POSTS_PLUGIN_NAME: Blog author posts plugin name (default: ``Author Blog Articles``)
* BLOG_TAGS_PLUGIN_NAME: Blog tags plugin name (default: ``Tags``)
* BLOG_CATEGORY_PLUGIN_NAME: Blog categories plugin name (default: ``Categories``)
* BLOG_ARCHIVE_PLUGIN_NAME: Blog archive plugin name (default: ``Archive``)
* BLOG_FEED_CACHE_TIMEOUT: Cache timeout for RSS feeds
* BLOG_FEED_INSTANT_ITEMS: Number of items in Instant Article feed
* BLOG_FEED_LATEST_ITEMS: Number of items in latest items feed
* BLOG_FEED_TAGS_ITEMS: Number of items in per tags feed

Read-only settings
++++++++++++++++++

* BLOG_MENU_TYPES: Available structures of the Blog menu; (default list **Posts and Categories**,
  **Categories only**, **Posts only**, **None**)
* BLOG_MENU_TYPE: Structure of the Blog menu;
  (default: ``Posts and Categories``)


********************
Per-Apphook settings
********************

* application title: Free text title that can be used as title in templates;
* object name: Free text label for Blog items in django CMS Wizard;
* Post published by default: Per-Apphook setting for BLOG_DEFAULT_PUBLISHED;
* Permalink structure: Per-Apphook setting for
  BLOG_AVAILABLE_PERMALINK_STYLES;
* Use placeholder and plugins for article body: Per-Apphook setting for
  BLOG_USE_PLACEHOLDER;
* Use abstract field: Per-Apphook setting for BLOG_USE_ABSTRACT;
* Set author: Per-Apphook setting for BLOG_AUTHOR_DEFAULT;
* Paginate sizePer-Apphook setting for BLOG_PAGINATION;
* Template prefix: Alternative directory to load the blog templates from;
* Menu structure: Per-Apphook setting for BLOG_MENU_TYPE
* Sitemap changefreq: Per-Apphook setting for BLOG_SITEMAP_CHANGEFREQ_DEFAULT
* Sitemap priority: Per-Apphook setting for BLOG_SITEMAP_PRIORITY_DEFAULT
* Object type: Per-Apphook setting for BLOG_TYPE
* Facebook type: Per-Apphook setting for BLOG_FB_TYPE
* Facebook application ID: Per-Apphook setting for BLOG_FB_APP_ID
* Facebook profile ID: Per-Apphook setting for BLOG_FB_PROFILE_ID
* Facebook page URL: Per-Apphook setting for BLOG_FB_PUBLISHER
* Facebook author URL: Per-Apphook setting for BLOG_AUTHOR_URL
* Facebook author: Per-Apphook setting for BLOG_AUTHOR
* Twitter type: Per-Apphook setting for BLOG_TWITTER_TYPE
* Twitter site handle: Per-Apphook setting for BLOG_TWITTER_SITE
* Twitter author handle: Per-Apphook setting for BLOG_TWITTER_AUTHOR
* Google+ type: Per-Apphook setting for BLOG_GPLUS_TYPE
* Google+ author name: Per-Apphook setting for BLOG_GPLUS_AUTHOR
* Send notifications on post publish: Send desktop notifications when a post is published
* Send notifications on post update: Send desktop notifications when a post is updated


Import from Wordpress
+++++++++++++++++++++

If you want to import content from existing wordpress blog, check
https://pypi.python.org/pypi/the-real-django-wordpress and
this gist https://gist.github.com/yakky/11336204 as a base.

Known djangocms-blog websites
+++++++++++++++++++++++++++++

See DjangoPackages for an updated list https://www.djangopackages.com/packages/p/djangocms-blog/


.. _django-meta-mixin settings: https://github.com/nephila/django-meta-mixin#settings
.. _django CMS installation docs: http://django-cms.readthedocs.io/en/release-3.4.x/how_to/install.html




=======
History
=======

*******************
0.8.13 (2017-07-25)
*******************

* Dropped python 2.6 compatibility
* Fixed exceptions in __str__
* Fixed issue with duplicated categories in menu

*******************
0.8.12 (2017-03-11)
*******************

* Fixed migrations on Django 1.10

*******************
0.8.11 (2017-03-04)
*******************

* Fixed support for aldryn-apphooks-config 0.3.1

*******************
0.8.10 (2017-01-02)
*******************

* Fix error in get_absolute_url

******************
0.8.9 (2016-10-25)
******************

* Optimized querysets
* Fixed slug generation in wizard

******************
0.8.8 (2016-09-04)
******************

* Fixed issue with one migration
* Improved support for django CMS 3.4

******************
0.8.7 (2016-08-25)
******************

* Added support for django CMS 3.4
* Fixed issue with multisite support

******************
0.8.6 (2016-08-03)
******************

* Set the correct language during indexing

******************
0.8.5 (2016-06-26)
******************

* Fixed issues with ThumbnailOption migration under mysql.

******************
0.8.4 (2016-06-22)
******************

* Fixed issues with cmsplugin-filer 1.1.

******************
0.8.3 (2016-06-21)
******************

* Stricter filer dependency versioning.

******************
0.8.2 (2016-06-12)
******************

* Aldryn-only release. No code changes

******************
0.8.1 (2016-06-11)
******************

* Aldryn-only release. No code changes

******************
0.8.0 (2016-06-05)
******************

* Added django-knocker integration
* Changed the default value of date_published to null
* Cleared menu cache when changing menu layout in apphook config
* Fixed error with wizard multiple registration
* Made django CMS 3.2 the default version
* Fixed error with on_site filter
* Removed meta-mixin compatibility code
* Changed slug size to 255 chars
* Fixed pagination setting in list views
* Added API to set default sites if user has permission only for a subset of sites
* Added Aldryn integration

******************
0.7.0 (2016-03-19)
******************

* Make categories non required
* Fix tests with parler>=1.6
* Use all_languages_column to admin
* Add publish button
* Fix issues in migrations. Thanks @skirsdeda
* Fix selecting current menu item according to menu layout
* Fix some issues with haystack indexes
* Add support for moved ThumbnailOption
* Fix Django 1.9 issues
* Fix copy relations method in plugins
* Mitigate issue when apphook config can't be retrieved
* Mitigate issue when wizard double registration is triggered

******************
0.6.3 (2015-12-22)
******************

* Add BLOG_ADMIN_POST_FIELDSET_FILTER to filter admin fieldsets
* Ensure correct creation of full URL for canonical urls
* Move constants to settings
* Fix error when no config is found

******************
0.6.2 (2015-11-16)
******************

* Add app_config field to BlogLatestEntriesPlugin
* Fix __str__ plugins method
* Fix bug when selecting plugins template

******************
0.6.1 (2015-10-31)
******************

* Improve toolbar: add all languages for each post
* Improve toolbar: add per-apphook configurable changefreq, priority

******************
0.6.0 (2015-10-30)
******************

* Add support for django CMS 3.2 Wizard
* Add support for Apphook Config
* Add Haystack support
* Improved support for meta tags
* Improved admin
* LatestPostsPlugin tags field has been changed to a plain TaggableManager field.
  A migration is in place to move the data, but backup your data first.

******************
0.5.0 (2015-08-09)
******************

* Add support for Django 1.8
* Drop dependency on Django select2
* Code cleanups
* Enforce flake8 / isort checks
* Add categories menu
* Add option to disable the abstract

******************
0.4.0 (2015-03-22)
******************

* Fix Django 1.7 issues
* Fix dependencies on python 3 when using wheel packages
* Drop Django 1.5 support
* Fix various templates issues
* UX fixes in the admin

******************
0.3.1 (2015-01-07)
******************

* Fix page_name in template
* Set cascade to set null for post image and thumbnail options

******************
0.3.0 (2015-01-04)
******************

* Multisite support
* Configurable default author support
* Refactored settings
* Fix multilanguage issues
* Fix SEO fields length
* Post absolute url is generated from the title in any language if current is
  not available
* If djangocms-page-meta and djangocms-page-tags are installed, the relevant
  toolbar items are removed from the toolbar in the post detail view to avoid
  confusings page meta / tags with post ones
* Plugin API changed to filter out posts according to the request.
* Django 1.7 support
* Python 3.3 and 3.4 support

******************
0.2.0 (2014-09-24)
******************

* **INCOMPATIBLE CHANGE**: view names changed!
* Based on django parler 1.0
* Toolbar items contextual to the current page
* Add support for canonical URLs
* Add transifex support
* Add social tags via django-meta-mixin
* Per-post or site-wide comments enabling
* Simpler TextField-based content editing for simpler blogs
* Add support for custom user models

******************
0.1.0 (2014-03-06)
******************

* First experimental release


