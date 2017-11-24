$(document).ready(function(){

    $("#register").click(function(){
        // alert("clicked");
        $(".login").fadeOut(function(){
            $(".registration").fadeIn();
        });
    })

    $("#login").click(function(){
        // alert("clicked");
        $(".registration").fadeOut(function(){
            $(".login").fadeIn();
        });
    })
})