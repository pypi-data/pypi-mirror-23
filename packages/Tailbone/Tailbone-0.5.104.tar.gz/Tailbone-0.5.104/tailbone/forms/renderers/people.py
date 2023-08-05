# -*- coding: utf-8; -*-
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
People Field Renderers
"""

from __future__ import unicode_literals, absolute_import

import six
from webhelpers.html import tags

from tailbone.forms.renderers.common import AutocompleteFieldRenderer


class PersonFieldRenderer(AutocompleteFieldRenderer):
    """
    Renderer for :class:`rattail.db.model.Person` instance fields.
    """
    service_route = 'people.autocomplete'

    def render_readonly(self, **kwargs):
        person = self.raw_value
        if not person:
            return ''
        return tags.link_to(person, self.request.route_url('people.view', uuid=person.uuid))


class CustomerFieldRenderer(AutocompleteFieldRenderer):
    """
    Renderer for :class:`rattail.db.model.Customer` instance fields.
    """

    service_route = 'customers.autocomplete'

    def render_readonly(self, **kwargs):
        customer = self.raw_value
        if not customer:
            return ''
        text = self.render_value(customer)
        return tags.link_to(text, self.request.route_url('customers.view', uuid=customer.uuid))

    def render_value(self, customer):
        return six.text_type(customer)
