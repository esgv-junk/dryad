var editableNodes = 'p, section, .math-admonition, div.code, ul, ol, li';
var editModeOn = true;
var isEditedNow = false;

/* == PATH UTILITIES == */

function siblingIndex(element) {
  return $(element).prevAll(editableNodes).length;
}

function doctreePath(element) {
  if ($(element).hasClass('content')) {
    return [];
  }

  return doctreePath($(element).parent()).concat([siblingIndex(element)]);
}

/* == CODEMIRROR EDITOR == */

function createEditor(element, data) {
  $(element).click(stopPropagation);
  var editor = CodeMirror(element, {
    'value': data,

    'indentUnit': 4,
    'smartIndent': true,
    'indentWithTabs': false,
    'tabSize': 4,
    'electricChars': false,

    'autoClearEmptyLines': false,
    'lineWrapping': true,
    'lineNumbers': true,
    'autofocus': true,
    'extraKeys': { 'Ctrl-S': startSave }
  });

  var lineCount = editor.lineCount();
  var lastLineLength = editor.getLine(lineCount - 1).length;
  editor.setCursor(lineCount - 1, lastLineLength);
}

/* == AJAX EVENTS == */

function startEdit(element) {
  startSave();

  if (!$('body').hasClass('edit-mode')) {
    return;
  }

  isEditedNow = true;
  $(element).append('<div class="edit-overlay" id="editor"></div>');
  $("#editor").siblings().hide();

  $.get(
    '/onpage-edit' + document.location.pathname.slice(5),
    {
      'node_path': doctreePath(element).join(',')
    },
    nodeSourceRecieved
  );
}

function nodeSourceRecieved(data) {
  createEditor($('#editor')[0], data);
}

function startSave() {
  if (!isEditedNow) {
    return;
  }
  $.post('/onpage-edit' + document.location.pathname.slice(5),
    {
      'node_path': doctreePath($("#editor").parent()).join(','),
      'new_lines': editor.getValue(),
      'csrfmiddlewaretoken': csrf_token
    },
    endSave
  );
}

function endSave() {
  isEditedNow = false;
  //$editor = $('.edit-overlay');
  //$editor.siblings().show();
  //$editor.remove();
  location.reload();
}

/* == EVENT HANDLERS == */

function editableClicked(event) {
  if (editModeOn) {
    startEdit(this);
  }
  event.stopPropagation();
}

function stopPropagation(event) {
  event.stopPropagation();
}

function bodyClicked() {
  startSave();
  isEditedNow = false;
}
