var csrftoken = $("input[name=csrfmiddlewaretoken]").val();

function incrementCart() {
  var element = $(".head_last_cart_text");
  var current = parseInt(element.text());
  element.text(++current);
}
function addToCart(csrftoken, id, type, car_id) {
  $.post(
    `/cart/`,
    {
      csrfmiddlewaretoken: csrftoken,
      id: id,
      type: type,
      car_id: car_id,
    },
    function (data) {
      $(".modal_content_products_container").append(
        `<div class="modal_content_product">
        <div class="modal_content_product_wrap">
        <a href="#" class="modal_content_produsct_link"><img src="icons/modalicon.jpg" alt="" class="modal_content_product_wrap_img"></a>
      </div>

      <div class="modal_content_prudoct_descr">
        <b>Проставки ${data.article}</b>
        <br>
        <a href="${data.car_slug}" class="modal_content_product_descr_link">Автомобиль: ${data.car_name}</a>
        <br>
        Размер проставок: ${data.type}
      </div>

      <p class="modal_content_product_price">${data.price} ₽</p>
          <input id="spacer_id" type="hidden" name="id" value="${data.id}" />
      <button class="modal_content_product_backet" onclick=on_basket(this)>Мусорка</button>
      </div>`
      );
    }
  );
  incrementCart();
}
function openCart() {}
console.log($(".add20mm_btn"));
$(".add20mm_btn").on("click", function () {
  var id = $(this).children("#add20mm").val();
  var car_id = $("#car_id").val();
  addToCart(csrftoken, id, "20mm", car_id);
});
$(".add30mm_btn").on("click", function () {
  var id = $(this).children("#add30mm").val();
  var car_id = $("#car_id").val();
  addToCart(csrftoken, id, "30mm", car_id);
});
$(".add40mm_btn").on("click", function () {
  var id = $(this).children("#add40mm").val();
  var car_id = $("#car_id").val();
  addToCart(csrftoken, id, "40mm", car_id);
});
