function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie("csrftoken");
$("#add20mm_btn").on("click", function () {
  var id = $("#add20mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "20mm",
    car_id: car_id,
  });
});
$("#add30mm_btn").on("click", function () {
  var id = $("#add30mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "30mm",
    car_id: car_id,
  });
});
$("#add40mm_btn").on("click", function () {
  var id = $("#add40mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "40mm",
    car_id: car_id,
  });
});
