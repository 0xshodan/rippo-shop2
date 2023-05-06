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
$(".select_menu_wrapper_btn").on("click", function () {
  var $mod_option = $("#select_modification").find("option:selected");
  var mod_id = $mod_option.val();
  if (mod_id != "-1") {
    $.get(`/api/slugs/carmod/${mod_id}`, function (data, _) {
      window.location.replace(`/modification/${data.slug}`);
    });
  } else {
    var $year_option = $("#select_year").find("option:selected");
    var year_id = $year_option.val();

    if (year_id != "-1") {
      $.get(`/api/slugs/cargen/${year_id}`, function (data, _) {
        window.location.replace(`/generation/${data.slug}`);
      });
    } else {
      var $model_option = $("#select_model").find("option:selected");
      var model_id = $model_option.val();

      if (model_id != "-1") {
        $.get(`/api/slugs/car/${model_id}`, function (data, _) {
          window.location.replace(`/car/${data.slug}`);
        });
      } else {
        var $brand_option = $("#select_brand").find("option:selected");
        var brand_id = $brand_option.val();

        if (brand_id != "-1") {
          $.get(`/api/slugs/brand/${brand_id}`, function (data, _) {
            window.location.replace(`/brand/${data.slug}`);
          });
        }
      }
    }
  }
});
