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
      if (!$.isEmptyObject(data)) {
        console.log($(".modal_content"));
        $(".modal_content").prepend(`
      <div class="modal_content_product">
        <div class="modal_content_product_wrap">
          <a href="#" class="modal_content_produsct_link">
            <img src="icons/modalicon.jpg" alt="" class="modal_content_product_wrap_img">
          </a>
        </div>

        <div class="modal_content_product_descr">
          <b>Проставки ${data.article}</b>
          <br>
          <a href="${data.car_slug}" class="modal_content_product_descr_link">Автомобиль: ${data.car_name}</a>
          <br>
          Размер проставок: ${data.type}
        </div>
        <div class="modal_content_product_menu">
            <button class="modal_content_product_menu_btn" onclick=on_decrement(this)>-</button>
            <div class="modal_content_product_menu_item">${data.quantity}</div>
            <button class="modal_content_product_menu_btn" onclick=on_increment(this)>+</button>
        </div>
            <p class="modal_content_product_price">${data.price} ₽</p>
            <input id="spacer_id" type="hidden" name="id" value="${data.id}" />
            <button class="modal_content_product_backet" onclick=on_basket(this)><img src="icons/trash.svg" alt="trash" class="modal_content_product_backet_img"></button>
      </div>`);
        incrementCart();
      }
    }
  );
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
