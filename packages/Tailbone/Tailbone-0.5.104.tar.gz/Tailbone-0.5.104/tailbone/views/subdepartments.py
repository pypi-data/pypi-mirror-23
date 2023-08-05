# -*- coding: utf-8 -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2017 Lance Edgar
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
Subdepartment Views
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model

from tailbone.db import Session
from tailbone.views import MasterView
from tailbone.views.continuum import VersionView, version_defaults


class SubdepartmentsView(MasterView):
    """
    Master view for the Subdepartment class.
    """
    model_class = model.Subdepartment
    mergeable = True
    merge_additive_fields = [
        'product_count',
    ]
    merge_fields = merge_additive_fields + [
        'uuid',
        'number',
        'name',
        'department_number',
    ]

    def configure_grid(self, g):
        g.filters['name'].default_active = True
        g.filters['name'].default_verb = 'contains'
        g.default_sortkey = 'name'
        g.configure(
            include=[
                g.number,
                g.name,
                g.department,
            ],
            readonly=True)

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.number,
                fs.name,
                fs.department,
            ])
        return fs

    def get_merge_data(self, subdept):
        return {
            'uuid': subdept.uuid,
            'number': subdept.number,
            'name': subdept.name,
            'department_number': subdept.department.number if subdept.department else None,
            'product_count': len(subdept.products),
        }

    def merge_objects(self, removing, keeping):

        # merge products
        for product in removing.products:
            product.subdepartment = keeping

        Session.delete(removing)


class SubdepartmentVersionView(VersionView):
    """
    View which shows version history for a subdepartment.
    """
    parent_class = model.Subdepartment
    route_model_view = 'subdepartments.view'


def includeme(config):
    SubdepartmentsView.defaults(config)
    version_defaults(config, SubdepartmentVersionView, 'subdepartment')
