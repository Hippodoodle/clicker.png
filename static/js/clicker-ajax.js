$(document).ready(function () {

    $('#clicker').click(function () {
        var username;
        username = $(this).attr('data-user');

        $.get('/clicker_app/add_points/', {'username': username},
            function (data) {
                $('#points_count').html(data);
            })
    });

    $('button').hover(
        function () {
            $(this).css('color', 'red');
        },
        function () {
            $(this).css('color', 'black');
        });


    $('#about-btn').click(function() {
        alert('You clicked the button using JQuery!');
    });

});