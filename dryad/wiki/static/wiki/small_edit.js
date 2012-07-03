var editableNodes = 'p, section, .math-admonition, div.code, ul, ol, li, table';
var editModeOn = true;
var isEditedNow = false;
var editor = null;

/* == PATH UTILITIES == */

function siblingIndex(element) {
  return $(element).prevAll('.editable').length;
}

function doctreePath(element) {
  if ($(element).hasClass('content')) {
    return [];
  }

  return doctreePath($(element).parent()).concat([siblingIndex(element)]);
}

function currentPagePath() {
  return document.location.pathname.slice(5);
}

/* == CODEMIRROR EDITOR == */

function createEditor(element, data) {
  $(element).click(stopPropagation);
  editor = CodeMirror(element, {
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
  if (lineCount < 10) {
    var lastLineLength = editor.getLine(lineCount - 1).length;
    editor.setCursor(lineCount - 1, lastLineLength);
  }
}

/* == AJAX EVENTS == */

function startEdit(element) {
  isEditedNow = true;


  $(element)
      .append('<div class="editor"></div>')
      .append($('.edit-info.loading').detach());
  $('body')
      .append('<div class="blocker-overlay"></div>')
      .removeClass('edit-mode');

  $.get(
    '/onpage-edit' + currentPagePath(),
    { 'node_path': doctreePath(element).join(',') },
    nodeSourceRecieved
  );
}

function nodeSourceRecieved(data) {
  $('.edit-info.loading').remove();
  $('.blocker-overlay')
      .addClass('active')
      .click(startSave);

  var $editor = $('.editor');
  $editor.click(stopPropagation);
  $editor.append($('.edit-info.info').detach());
  $editor.siblings().hide();
  createEditor($editor[0], data);
}

function startSave() {
  $('.edit-info.info').replaceWith($('.edit-info.saving').detach());
  $('.blocker-overlay')
      .off('click')
      .removeClass('active');

  $.post(
    '/onpage-edit' + currentPagePath(),
    {
      'node_path': doctreePath($(".editor").parent()).join(','),
      'new_lines': editor.getValue(),
      'csrfmiddlewaretoken': csrf_token
    },
    endSave
  );
}

function endSave() {
  location.reload();
}

/* == EVENT HANDLERS == */

function editableClicked(event) {
  if ($('body').hasClass('edit-mode')) {
    startEdit(this);
  }
  event.stopPropagation();
}

function stopPropagation(event) {
  event.stopPropagation();
}
