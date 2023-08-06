## -*- coding: utf-8; -*-
## ##############################################################################
## 
## Default master 'index' template.  Features a prominent data table and
## exposes a way to filter and sort the data, etc.  Some index pages also
## include a "tools" section, just above the grid on the right.
## 
## ##############################################################################
<%inherit file="/master/index.mako" />

<%def name="title()">${model_title_plural}</%def>

<%def name="context_menu_items()">
  % if master.creatable and request.has_perm('{}.create'.format(permission_prefix)):
      <li>${h.link_to("Create a new {}".format(model_title), url('{}.create'.format(route_prefix)))}</li>
  % endif
</%def>

## ${grid.render_complete(tools=capture(self.grid_tools).strip(), context_menu=capture(self.context_menu_items).strip())|n}

<div class="newgrid-wrapper">

  <table class="grid-header">
    <tbody>
      <tr>

        <td class="filters" rowspan="2">
          % if grid.filterable:
              ## TODO: should this be variable sometimes?
              ${grid.render_filters(allow_save_defaults=True)|n}
          % endif
        </td>

        <td class="menu">
          <ul id="context-menu">
            ${self.context_menu_items()}
          </ul>
        </td>
      </tr>

      <tr>
        <td class="tools">
          <div class="grid-tools">
            ${self.grid_tools()}
          </div><!-- grid-tools -->
        </td>
      </tr>

    </tbody>
  </table><!-- grid-header -->

  ${grid.render_grid()|n}

</div><!-- newgrid-wrapper -->

