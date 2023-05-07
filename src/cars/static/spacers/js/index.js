var csrftoken = $("input[name=csrfmiddlewaretoken]").val()

function incrementCart(){
  var element = $(".head_last_cart_text")
  var current = parseInt(element.text())
  element.text(++current)
}
console.log($(".add20mm_btn"))
$(".add20mm_btn").on("click", function () {
  var id = $(this).children("#add20mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "20mm",
    car_id: car_id,
  });
  incrementCart();
});
$(".add30mm_btn").on("click", function () {
  var id = $(this).children("#add30mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "30mm",
    car_id: car_id,
  });
  incrementCart();
});
$(".add40mm_btn").on("click", function () {
  var id = $(this).children("#add40mm").val();
  var car_id = $("#car_id").val();
  console.log(id);
  $.post(`/cart/`, {
    csrfmiddlewaretoken: csrftoken,
    id: id,
    type: "40mm",
    car_id: car_id,
  });
  incrementCart();
});
