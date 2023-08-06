define([
  'base/js/namespace',
  'notebook/js/celltoolbar',
], function(Jupyter, celltoolbar) {
  'use strict';

  var CellToolbar = celltoolbar.CellToolbar;
  var toolbar_preset_name = 'Student Solutions';
  var solutions_visible = true;

  var solutions_ui_callback = CellToolbar.utils.checkbox_ui_generator(
    'Hide From Students',
    function setter (cell, value) {
      if (cell.metadata.tags === undefined) {
        cell.metadata.tags = [];
      }
      if (value) {
        cell.metadata.tags.push('hide_from_student');
      }
      else {
        var index = cell.metadata.tags.indexOf('hide_from_student');
        if (index > -1) {
          cell.metadata.tags.splice(index,1);
        }
      }
    },
    function getter (cell) {
      if (cell.metadata.tags === undefined) {
        return false;
      }
      else {
        return cell.metadata.tags.indexOf('hide_from_student') > -1;
      }
    }
  );

  var register = function(notebook) {
    CellToolbar.register_callback('nbsolutions.is_solution', solutions_ui_callback);

    var attachments_preset = [];
    attachments_preset.push('nbsolutions.is_solution');

    CellToolbar.register_preset(toolbar_preset_name, attachments_preset, notebook);

  };

  function toggle_solution_visibility() {
    var cells = Jupyter.notebook.get_cells();
    solutions_visible = !solutions_visible;
    for (var i = 0; i < cells.length; i++) {
      // ignore cells without tags
      if (cells[i].metadata.tags === undefined) {
        continue;
      }

      if (cells[i].metadata.tags.indexOf('hide_from_student') > -1) {
        if (!solutions_visible) {
          cells[i].element.addClass('hidden');
        }
        else {
          cells[i].element.removeClass('hidden');
        }
      }
    }
  }

  var action = {
    'label'   : 'Student View',
    'icon'    : 'fa fa-university',
    'callback': toggle_solution_visibility
  };

  var load_extension = function() {
    register(Jupyter.notebook);
    Jupyter.toolbar.add_buttons_group([action]);
  };

  var extension = {
    load_jupyter_extension : load_extension,
    load_ipython_extension : load_extension
  };

  return extension;

});
