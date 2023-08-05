from __future__ import unicode_literals

from django.conf.urls import include, url
from django.core import urlresolvers
from wagtail.wagtailadmin.menu import MenuItem
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import hooks

from wagtaillinkchecker import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^link-checker/', include(urls)),
    ]


@hooks.register('register_settings_menu_item')
def register_menu_settings():
    return MenuItem(
        _('Link Checker'),
        urlresolvers.reverse('wagtaillinkchecker'),
        classnames='icon icon-link',
        order=300
    )
