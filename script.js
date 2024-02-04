const URL = "http://localhost:3000";

const result = $("#result");

$(document).ready(function () {
  $("#result-btn").on("click", function () {
    const selectedQuestion = $("#questions").val();
    result.empty();
    makeRequest(selectedQuestion);
  });
});

function makeRequest(questionId) {
  $.ajax({
    url: URL + "/query-question",
    method: "GET",
    headers: {
      "Question-Id": questionId,
    },
    success: function (response) {
      createTable(response);
    },
    error: function (_, status, error) {
      result.empty().html("<h2>Error while making a query</h2>");
    },
  });
}

function createTable(data) {
  const table = $("<table>").addClass("table");

  const thead = $("<thead>");
  const headerRow = $("<tr>");

  data.columns.forEach(function (column) {
    headerRow.append($("<th>").text(column));
  });
  thead.append(headerRow);
  table.append(thead);
  const tbody = $("<tbody>");
  data.data.forEach((d) => {
    const rowElement = $("<tr>");
    d.forEach((a) => {
      const cell = $("<td>").text(a);

      if (typeof a === "number") {
        cell.addClass("numeric");
      }
      rowElement.append(cell);
    });
    tbody.append(rowElement);
  });

  table.append(tbody);

  result.empty().append(table);
}
