# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2017 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Views for label batches
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model

import formalchemy as fa

from tailbone import forms
from tailbone.views.batch import BatchMasterView


class LabelBatchView(BatchMasterView):
    """
    Master view for label batches.
    """
    model_class = model.LabelBatch
    model_row_class = model.LabelBatchRow
    default_handler_spec = 'rattail.batch.labels:LabelBatchHandler'
    model_title_plural = "Label Batches"
    route_prefix = 'labels.batch'
    url_prefix = '/labels/batches'
    creatable = False
    editable = False
    rows_editable = True
    cloneable = True

    def _preconfigure_fieldset(self, fs):
        super(LabelBatchView, self)._preconfigure_fieldset(fs)
        fs.append(fa.Field('handheld_batches', renderer=forms.renderers.HandheldBatchesFieldRenderer, readonly=True,
                           value=lambda b: b._handhelds))

    def configure_fieldset(self, fs):
        fs.configure(
            include=[
                fs.id,
                fs.created,
                fs.created_by,
                fs.handheld_batches,
                fs.rowcount,
                fs.executed,
                fs.executed_by,
            ])
        batch = fs.model
        if self.viewing and not batch._handhelds:
            del fs.handheld_batches

    def _preconfigure_row_grid(self, g):
        super(LabelBatchView, self)._preconfigure_row_grid(g)
        g.upc.set(label="UPC")
        g.brand_name.set(label="Brand")
        g.regular_price.set(label="Reg Price")
        g.label_profile.set(label="Label Type")
        g.label_quantity.set(label="Qty")

    def configure_row_grid(self, g):
        g.configure(
            include=[
                g.sequence,
                g.upc,
                g.brand_name,
                g.description,
                g.size,
                g.regular_price,
                g.sale_price,
                g.label_profile,
                g.label_quantity,
                g.status_code,
            ],
            readonly=True)

    def row_grid_row_attrs(self, row, i):
        attrs = {}
        if row.status_code != row.STATUS_OK:
            attrs['class_'] = 'warning'
        return attrs

    def _preconfigure_row_fieldset(self, fs):
        fs.sequence.set(readonly=True)
        fs.product.set(readonly=True)
        fs.upc.set(readonly=True, label="UPC")
        fs.brand_name.set(readonly=True)
        fs.description.set(readonly=True)
        fs.size.set(readonly=True)
        fs.department_number.set(readonly=True)
        fs.department_name.set(readonly=True)
        fs.regular_price.set(readonly=True)
        fs.pack_quantity.set(readonly=True)
        fs.pack_price.set(readonly=True)
        fs.sale_price.set(readonly=True)
        fs.sale_start.set(readonly=True)
        fs.sale_stop.set(readonly=True)
        fs.vendor_id.set(readonly=True, label="Vendor ID")
        fs.vendor_name.set(readonly=True)
        fs.vendor_item_code.set(readonly=True)
        fs.case_quantity.set(readonly=True)
        fs.status_code.set(readonly=True)
        fs.status_text.set(readonly=True)

        fs.label_profile.set(label="Label Type")

    def configure_row_fieldset(self, fs):
        if self.viewing:
            fs.configure(
                include=[
                    fs.sequence,
                    fs.upc,
                    fs.brand_name,
                    fs.description,
                    fs.size,
                    fs.department_number,
                    fs.department_name,
                    fs.regular_price,
                    fs.pack_quantity,
                    fs.pack_price,
                    fs.sale_price,
                    fs.sale_start,
                    fs.sale_stop,
                    fs.vendor_id,
                    fs.vendor_name,
                    fs.vendor_item_code,
                    fs.case_quantity,
                    fs.label_profile,
                    fs.label_quantity,
                    fs.status_code,
                    fs.status_text,
                ])

        elif self.editing:
            fs.configure(
                include=[
                    fs.sequence,
                    fs.upc,
                    fs.product,
                    fs.department_number,
                    fs.department_name,
                    fs.regular_price,
                    fs.sale_price,
                    fs.label_profile,
                    fs.label_quantity,
                    fs.status_code,
                    fs.status_text,
                ])


def includeme(config):
    LabelBatchView.defaults(config)
