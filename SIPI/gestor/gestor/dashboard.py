"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'gestor.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
#        self.children.append(modules.Group(
 #           _('Group: Administration & Applications'),
  #          column=1,
   #         collapsible=True,
    #        children = [
     #           modules.AppList(
      #              _('Administration'),
       #             column=1,
        #            collapsible=False,
         #           models=('django.contrib.*',),
          #      ),
           #     modules.AppList(
            #        _('Applications'),
             #       column=1,
              #      css_classes=('collapse closed',),
               #     exclude=('django.contrib.*',),
               # )
          #  ]
       # ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Modulos'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Administracion'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        # append another link list module for "support".
#        self.children.append(modules.LinkList(
 #           _('Media Management'),
  #          column=2,
   #         children=[
    #            {
     #               'title': _('FileBrowser'),
      #              'url': '/admin/filebrowser/browse/',
       #             'external': False,
        #        },
         #   ]
       # ))

        # append another link list module for "support".

        # append a feed module
#        self.children.append(modules.Feed(
 #           _('Latest Django News'),
  #          column=2,
   #         feed_url='http://www.djangoproject.com/rss/weblog/',
    #        limit=5
     #   ))

        # append a recent actions module
      #  self.children.append(modules.RecentActions(
       #     _('Recent actions'),
        #    limit=5,
         #   collapsible=False,
         #   column=3,
#        ))
