$(document).ready(function () {

    function start() {
        $(".login").slideDown(function(){
            $("#footer").slideDown();
        });

        $("#register").click(function () {
            // alert("clicked");
            $(".login").fadeOut(function () {
                $(".registration").fadeIn();
            });
        })

        $("#login").click(function () {
            // alert("clicked");
            $(".registration").fadeOut(function () {
                $(".login").fadeIn();
            });
        })
    }


    var word = "elcome to the Book Review!";
    var el = document.getElementById('title_scroll');
    var character_counter = 0;
    // var finished = false;
    function updateText() {
        el.innerHTML = el.innerHTML + word[character_counter++];
        if (character_counter == word.length + 1) {
            character_counter = word.length;
            el.innerHTML = 'Welcome to the Book Review!';
            start();
            clearInterval(interval);
            // finished = true;
        }
    }

    var interval = setInterval(updateText, 28);

})
