$("#login").click(function(){
    window.location.href = "login";
    console.log('hi');
});

$("#menu>div").hover(function () {
    $(this).css("font-weight","900");
    $(this).css("color","green");
},
function () {
    $(this).css("font-weight","normal");
    $(this).css("color","black");
}
);
