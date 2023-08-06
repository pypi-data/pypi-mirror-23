==========================
django-affiliate-tracking
==========================

A `Django <https://www.djangoproject.com/>`_ app to do affiliation tracking.

.. image:: https://saxo.githost.io/publish/django-affiliate-tracking/badges/master/build.svg
   :alt: Build status
   :target: https://saxo.githost.io/publish/django-affiliate-tracking

.. image:: https://saxo.githost.io/publish/django-affiliate-tracking/badges/master/coverage.svg
   :alt: Test coverage
   :target: https://saxo.githost.io/publish/django-affiliate-tracking


About
*****

Another similar app,
`django-affiliate <https://pypi.python.org/pypi/django-affiliate>`_, also
exists, which might suit your needs better.

The main difference between the two apps is that with ``django-affiliate`` you
need to mix your tracking logic into your regular business logic, while with
``django-affiliate-tracking``, you can isolate your tracking logic into
separate modules and/or functions, thereby avoid polluting your regular
business logic with tracking logic. You can even create a separate app for all
your tracking, to do a full isolation and keep your existing apps reusable
across Django projects.

This is achieved by tying your tracking logic to Django signals via
configuration. Thus, signals has to be emitted at the events that could
trigger the tracking. In most cases these signals already exist (e.g. on model
save). And otherwise, you could implement custom signals for these events in
your business logic that might also be useful outside a tracking scope (and
thus not be as much of a pollution of your business logic).

This way, it's also easy to enable/disable triggers without having to rewrite
your apps or comment out tracking code each time you team up with a new partner
or your deal with an existing partner expires. It's simply done by changing
your settings and/or updating partners, e.g. via the Django Admin.

As soon as all your triggers are configured, non-techical staff can even manage
partners and trigger subscriptions via the Django Admin, reducing the need to
involve developers and doing a new release of your project.

We prefer this approach, and thus saw the need for a new Django app. if
you don't care about separation, both apps will get your job done, and
``django-affiliate`` might be the easier option for you.


Requirements/support
********************

* Python (2.x, 3.x)
* Django (1.9, 1.10, 1.11)

And any combination of these.


Installation
******************

Install the app from PyPi::

    $ pip install django-affiliate-tracking

Add the app to your Django project::

    INSTALLED_APPS = [
        ...
        'affiliations',
        ...
    ]

And add a couple of new middlewares::

    MIDDLEWARE_CLASSES = [
        ...
        'tls.TLSRequestMiddleware',
        'affiliations.middleware.AffiliateVisitorsRegistrationMiddleware',
    ]

Finally migrate the app::

    $ ./manage.py migrate


Using the app
************************

There is a ``dummy_project`` inside the app that should help you set up
a new project using the app, but we are giving more details about
it below.


Settings
=============

The following new settings should be introduced in your settings file
for the project using the app:

* ``AFFILIATE_QUERY_STRING_KEY`` – Optional name of the query string parameter
  that identifies which affiliate partner an incoming request is caused by. A
  default value of ``affiliate_id`` is assumed.
* ``AFFILIATE_SESSION_KEY`` – Optional name of the session key that the visitor
  id is kept in. A default value of ``affiliate_visitor_id`` is assumed.
* ``AFFILIATE_TRIGGERS`` – Mandatory list of 4 item tuples, defining which
  triggers should be enabled. The 4 items of each tuple should be:

 #. A "pretty name" for the trigger.
 #. A string defining a Python path to a signal that the trigger should be
    listening to.
 #. A string defining a Python path to the function that works as the signal
    reciever for the trigger.
 #. A valid value for the ``sender`` argument when connecting
    signal ``receivers``.

An example::

    [
        (
            'User registered',
            'django.db.models.signals.post_save',
            'affiliations.triggers.object_created',
            'django.contrib.auth.models.User',
        ),
    ]


Models explanation
******************

A partner is someone you make an affiliate deal with. The partner will then
(hopefully) generate traffic to your site. The initial referral should include
the partner ``uid`` in the query string (e.g.
``https://www.yoursite.com/?affiliate_id=moox6esi``), to identify the traffic
as originating from that particular partner::

    Partner
        * uid -- CharField, unique, 8 random alphanumeric characters.
        * name -- CharField, the name of the affiliate partner.
        * active -- BooleanField, whether there’s an active affiliate deal with
          this partner.


A subscription tells which triggers a partner subscribes to. The triggers in
your settings are not tied to specific partners (as you might have different
partners sharing the same trigger), you need to tie a partner and a trigger
together with a subscription. This also prevents you from accidentally paying
Partner A for Trigger X without that being part of your agreement::

    Subscription
        * partner, ForeignKey
        * trigger, CharField -- the 'name' of one of the triggers defined in
          the settings.
        * callback_url -- UrlField, the partner callback URL for the given
          trigger event. Should have the placeholder ``{visitor_id}`` in it
          somewhere, e.g. as the value for a query string parameter. An
          example: https://www.yourpartner.com/track/?campaign_id=123&visitor_id={visitor_id}


A visitor is someone who gets referred to your site by a partner. The
middleware will detect that a request was caused by an affiliate partner and
then register a new visitor::

    Visitor
        * partner -- ForeignKey
        * user -- ForeignKey, nullable, references user model (remember to use
          ``get_user_model``).
        * referred_on -- datetime, auto_now_add=True.
        * entry_point -- UrlField, the URL at which the visitor entered
          your site.
        * successful_on -- datetime, nullable, tells the date the conditions of
          a "success" were met, if at all.


Triggers
*****************

``django-affiliation-tracking`` comes with the two most basic triggers: ``object_created`` and ``object_saved``, located in the module ``affiliations.triggers``. They will probably serve 95% of your needs, if not all.

These can be used e.g. if you need to trigger when a new user registers or someone places an order in your shop.

If you need custom triggers, it's easy write your own. We'd recommend to take a look at or simply copy the built in triggers, to understand how triggers work, and built your own triggers with custom trigger logic on top of these.

What they both basically do is to call ``affiliations.triggers.complete_trigger()`` (one of them wraps it in a simple ``if``), but you can wrap it in more complex logic if you need. E.g. to have a trigger that only triggers on Fridays for users between 25 and 50 years old. It all depends on your own needs.

Please note that ``affiliations.triggers.complete_trigger()`` takes care of verifying that the the there's actually an affiliation visitor for the request, that the partner of the visitor is active and that the partner is subscribed to the actual trigger being trigged. So you don't need to include these checks in your custom trigger logic. Only your own special needs, like day of week and age of the user.


Authors
******************

* Mikkel Munch Mortensen
* Søren Howe Gersager
* Vladir Parrado Cruz


Maintenance
******************

To submit bugs, feature requests, submit patches, please use `the official repository <https://saxo.githost.io/publish/django-affiliate-tracking/>`_.


Copyright and licensing information
***********************************

© Saxo.com A/S under a BSD License 2.0, 3-clause license.
