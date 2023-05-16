function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
var csrftoken = getCookie("csrftoken");
$(".modal_btn").on("click", function () {
  $(".modal").removeClass("modal_active");
});

function on_increment(e) {
  var $parent = $(e).parent();
  var $pparent = $parent.parent();
  var id = $pparent.children("#spacer_id").val();
  var quantity = $parent.children(".modal_content_product_menu_item");
  var price = $pparent.children(".modal_content_product_price");
  var spacer_price = parseInt($pparent.children("#spacer_price").val());
  var current_price = parseInt(price.text().split(" ")[0]);
  $.ajax({
    url: "/cart/",
    type: "PATCH",
    // contentType:"application/json",
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    data: {
      csrfmiddlewaretoken: csrftoken,
      id: id,
      quantity: 1,
    },
  });
  var qt = parseInt(quantity.text());
  var newPrice = current_price + spacer_price;
  price.text(`${newPrice} ₽`);
  quantity.text(++qt);
}
function on_decrement(e) {
  var $parent = $(e).parent();
  var $pparent = $parent.parent();
  var id = $pparent.children("#spacer_id").val();
  var quantity = $parent.children(".modal_content_product_menu_item");
  var qt = parseInt(quantity.text());
  var price = $pparent.children(".modal_content_product_price");
  var spacer_price = parseInt($pparent.children("#spacer_price").val());
  var current_price = parseInt(price.text().split(" ")[0]);
  if (qt > 1) {
    $.ajax({
      url: "/cart/",
      type: "PATCH",
      // contentType:"application/json",
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      },
      data: {
        csrfmiddlewaretoken: csrftoken,
        id: id,
        quantity: -1,
      },
    });
    quantity.text(--qt);
    var newPrice = current_price - spacer_price;
    price.text(`${newPrice} ₽`);
  }
}
function on_basket(e) {
  var $parent = $(e).parent();
  var id = $parent.children("#spacer_id").val();
  $.ajax({
    url: "/cart/",
    type: "DELETE",
    // contentType:"application/json",
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    data: {
      csrfmiddlewaretoken: csrftoken,
      id: id,
    },
  });
  $parent.remove();
  var element = $(".head_last_cart_text");
  var current = parseInt(element.text());
  element.text(--current);
  var $now = $(".modal_content_product_text_link");
  var qt = parseInt($now.text().split(" ")[2]);
  --qt;
  if (qt === 0) {
    $now.text("Корзина пуста");
  } else {
    $now.text(`В корзине ${qt} товаров`);
  }
}

$(".modal_content_product_footer_btn").on("click", function () {
  $(".modal").removeClass("modal_active");
});
