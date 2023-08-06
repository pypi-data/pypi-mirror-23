## -*- coding: utf-8; -*-

% if grid.filterable:
    ${grid.render_filters()|n}
% endif

<ul data-role="listview">
  % for obj in grid.iter_rows():
      <li>${grid.listitem.render_readonly()}</li>
  % endfor
</ul>

##   <table data-role="table" class="ui-responsive table-stroke">
##     <thead>
##       <tr>
##         % for column in grid.iter_visible_columns():
##             ${grid.column_header(column)}
##         % endfor
##       </tr>
##     </thead>
##     <tbody>
##       % for i, row in enumerate(grid.iter_rows(), 1):
##           <tr>
##             % for column in grid.iter_visible_columns():
##                 <td>${grid.render_cell(row, column)}</td>
##             % endfor
##           </tr>
##       % endfor
##     </tbody>
##   </table>

% if grid.pageable and grid.pager:
    <br />
    <div data-role="controlgroup" data-type="horizontal">
      ${grid.pager.pager('$link_first $link_previous $link_next $link_last',
          symbol_first='<< first', symbol_last='last >>',
          symbol_previous='< prev', symbol_next='next >',
          link_attr={'class': 'ui-btn ui-corner-all'},
          curpage_attr={'class': 'ui-btn ui-corner-all'},
          dotdot_attr={'class': 'ui-btn ui-corner-all'})|n}
    </div>
% endif
