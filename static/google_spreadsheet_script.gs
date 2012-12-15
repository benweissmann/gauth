/**
 * Finds all cells that start with "gauth:" and resolves the token inthe cell with the GAuth service.
 */
function authResolve() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var rows = sheet.getDataRange();
  var numRows = rows.getNumRows();
  var values = rows.getValues();

  for (var i = 0; i <= numRows - 1; i++) {
    var row = values[i];
    for(var j = 0; j < row.length; j++) {
      val = String(values[i][j]);
      if(val.slice(0, 6) == 'gauth:') {
        cell = sheet.getRange(i+1, j+1);
        token = val.slice(6);
        var name = UrlFetchApp.fetch("https://bsw.scripts.mit.edu/gauth/tokens/" + token).getContentText();
        cell.setValue(name);
      }
    }
  }
};

function onInstall() {
  // Get spreadsheet key
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  // Create onEdit trigger using the Spreadsheet
  var onEditTrigger = ScriptApp.newTrigger("authResolve")
      .forSpreadsheet(spreadsheet)
      .onFormSubmit()
      .create();
}