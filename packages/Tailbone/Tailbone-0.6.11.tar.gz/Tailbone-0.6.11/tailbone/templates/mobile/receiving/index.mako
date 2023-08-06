## -*- coding: utf-8; -*-
<%inherit file="/mobile/master/index.mako" />

<%def name="title()">Receiving</%def>

% if request.has_perm('receiving.create'):
    ${h.link_to("New Receiving Batch", url('mobile.receiving.create'), class_='ui-btn ui-corner-all')}
% endif

${parent.body()}
