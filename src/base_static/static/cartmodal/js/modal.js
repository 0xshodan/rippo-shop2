function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
var csrftoken = getCookie('csrftoken');
$(".modal_btn").on("click", function(){
    $(".modal").removeClass("modal_active");
});
$(".modal_content_product_backet").on("click", function(){
    var $parent = $(this).parent()
    var id = $parent.children("#spacer_id").val();
    $.ajax(
        {
            url:"/cart/", 
            type:"DELETE", 
            // contentType:"application/json",
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken',csrftoken);
              },
            data:
            {
                csrfmiddlewaretoken: csrftoken,
                id: id,
            }
        }
    );
    $parent.remove();
    var element = $(".head_last_cart_text")
    var current = parseInt(element.text())
    element.text(--current)
})