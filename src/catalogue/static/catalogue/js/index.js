$("#select_brand").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
  if (id === "-1") {
    $("#select_model").html('<option value="-1">Все</option>');
    $("#select_year").html('<option value="-1">Все</option>');
    $("#select_modification").html('<option value="-1">Все</option>');
  } else {
    $.get(`/api/cars/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $("#select_model").html(html);
    });
  }
});
// asdasd
$("#select_model").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
  if (id == "-1") {
    $("#select_year").html('<option value="-1">Все</option>');
    $("#select_modification").html('<option value="-1">Все</option>');
  } else {
    $.get(`/api/generations/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $("#select_year").html(html);
    });
  }
});
$("#select_year").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
  if (id == "-1") {
    $("#select_modification").html('<option value="-1">Все</option>');
  } else {
    $.get(`/api/modifications/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $("#select_modification").html(html);
    });
  }
});
$("#select_modification").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
});
