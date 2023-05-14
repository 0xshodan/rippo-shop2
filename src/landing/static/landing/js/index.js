$(".panel_menu_wrap_item_brand").on("change", function () {
  var $option = $(this).find("option:selected");
  console.log($option);
  var id = $option.val();
  if (id === "-1") {
    $(".panel_menu_wrap_item_model").html('<option value="-1">Все</option>');
    $(".panel_menu_wrap_item_years").html('<option value="-1">Все</option>');
    $(".panel_menu_wrap_item_modification").html(
      '<option value="-1">Все</option>'
    );
  } else {
    $.get(`/api/cars/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $(".panel_menu_wrap_item_model").html(html);
    });
  }
});
$(".panel_menu_wrap_item_model").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
  if (id == "-1") {
    $(".panel_menu_wrap_item_years").html('<option value="-1">Все</option>');
    $(".panel_menu_wrap_item_modification").html(
      '<option value="-1">Все</option>'
    );
  } else {
    $.get(`/api/generations/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $(".panel_menu_wrap_item_years").html(html);
    });
  }
});
$(".panel_menu_wrap_item_years").on("change", function () {
  var $option = $(this).find("option:selected");
  var id = $option.val();
  if (id == "-1") {
    $(".panel_menu_wrap_item_modification").html(
      '<option value="-1">Все</option>'
    );
  } else {
    $.get(`/api/modifications/${id}`, function (data, _) {
      var html = '<option value="-1">Все</option>';
      for (const car of data.cars) {
        html += `<option value="${car.id}">${car.name}</option>`;
      }
      $(".panel_menu_wrap_item_modification").html(html);
    });
  }
});
$(".panel_menu_wrap_btn_click").on("click", function () {
  var $mod_option = $(".panel_menu_wrap_item_modification").find(
    "option:selected"
  );
  var mod_id = $mod_option.val();
  if (mod_id != "-1") {
    $.get(`/api/slugs/carmod/${mod_id}`, function (data, _) {
      window.location.replace(`/modification/${data.slug}`);
    });
  } else {
    var $year_option = $(".panel_menu_wrap_item_years").find("option:selected");
    var year_id = $year_option.val();

    if (year_id != "-1") {
      $.get(`/api/slugs/cargen/${year_id}`, function (data, _) {
        window.location.replace(`/generation/${data.slug}`);
      });
    } else {
      var $model_option = $(".panel_menu_wrap_item_model").find(
        "option:selected"
      );
      var model_id = $model_option.val();

      if (model_id != "-1") {
        $.get(`/api/slugs/car/${model_id}`, function (data, _) {
          window.location.replace(`/car/${data.slug}`);
        });
      } else {
        var $brand_option = $(".content_menu_wrap_item_brand").find(
          "option:selected"
        );
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
