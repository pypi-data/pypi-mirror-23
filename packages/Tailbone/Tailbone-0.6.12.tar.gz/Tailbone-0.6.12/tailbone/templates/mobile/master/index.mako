## -*- coding: utf-8; -*-
## ##############################################################################
## 
## Default master 'index' template for mobile.  Features a somewhat abbreviated
## data table and (hopefully) exposes a way to filter and sort the data, etc.
## 
## ##############################################################################
<%inherit file="/mobile/base.mako" />

<%def name="title()">${model_title_plural}</%def>

${grid.render_complete()|n}
