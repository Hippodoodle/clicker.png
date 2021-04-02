$(document).ready(function () {

    $('#clicker').click(function () {
        var a;
        a = $(this).attr('data-user');
        token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/add_points/',
            type: 'POST',
            success: function (data) {
                $('#points_count').html(data);
            },
            headers: {'X-CSRFToken': token},
            data: {'a': a}
        })

    });

    $('.purchase_button').click(function() {
        msgStr = $('#hey').html();
        msgStr = msgStr + ' THERE!';
        $('#hey').html(msgStr);
    });

    $('#about-btn').click(function () {
        alert('You clicked the button using JQuery!');
    });

});