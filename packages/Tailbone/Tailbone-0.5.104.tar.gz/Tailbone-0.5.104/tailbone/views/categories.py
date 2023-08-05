# -*- coding: utf-8 -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2016 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for
#  more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Category Views
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model

from tailbone.views import MasterView
from tailbone.views.continuum import VersionView, version_defaults


class CategoriesView(MasterView):
    """
    Master view for the Category class.
    """
    model_class = model.Category
    model_title_plural = "Categories"
    route_prefix = 'categories'

    def configure_grid(self, g):
        g.filters['name'].default_active = True
        g.filters['name'].default_verb = 'contains'
        g.default_sortkey = 'code'
        g.configure(
            include=[
                g.code,
                g.number,
                g.name,
                g.department,
            ],
            readonly=True)

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.code,
                fs.number,
                fs.name,
                fs.department,
            ])
        return fs


class CategoryVersionView(VersionView):
    """
    View which shows version history for a category.
    """
    parent_class = model.Category
    model_title_plural = "Categories"
    route_model_list = 'categories'
    route_model_view = 'categories.view'


def includeme(config):
    CategoriesView.defaults(config)
    version_defaults(config, CategoryVersionView, 'category', template_prefix='/categories')
