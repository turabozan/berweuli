$(document).ready(function () {
    $("#kahvalti").click(function () {
        $("#breakfast_items").slideToggle("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#soup").click(function () {
        $("#soup_items").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#zeytinyagli").click(function () {
        $("#zeytinyagli_items").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#pilav").click(function () {
        $("#pilafs").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#makarna").click(function () {
        $("#pastas").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#anayemek").click(function () {
        $("#special").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#osmanli").click(function () {
        $("#ottoman").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#salata").click(function () {
        $("#salads").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#dessets").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#tatli").click(function () {
        $("#desserts").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#hots").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#sicak").click(function () {
        $("#hots").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#desserts").slideUp("slow");
        $("#colds").slideUp("slow");
    });

    $("#soguk").click(function () {
        $("#colds").slideToggle("slow");
        $("#breakfast_items").slideUp("slow");
        $("#soup_items").slideUp("slow");
        $("#zeytinyagli_items").slideUp("slow");
        $("#pilafs").slideUp("slow");
        $("#pastas").slideUp("slow");
        $("#special").slideUp("slow");
        $("#ottoman").slideUp("slow");
        $("#salads").slideUp("slow");
        $("#desserts").slideUp("slow");
        $("#hots").slideUp("slow");
    });
});


//Social Media
$("#share").click(function () {
    $(".social.twitter").toggleClass("clicked");
    $(".social.facebook").toggleClass("clicked");
    //  $(".social.google").toggleClass("clicked");
    $(".social.instagram").toggleClass("clicked");
});

$("#evaluate").click(function () {
    $(".social_evaluate.google").toggleClass("clicked");
});
