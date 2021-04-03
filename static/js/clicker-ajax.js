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
                $('#user-counter').html(data);
            },
            headers: {'X-CSRFToken': token},
            data: {'a': a}
        })
    });

    $('.darkmode-button').click(function () {
        var a;
        a = $(this).attr('data-user');
        token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/myaccount/darkmode/',
            type: 'POST',
            success: function (data) {
                $('#darkmode-button').html(data);
            },
            headers: {'X-CSRFToken': token},
            data: {'d': d}
        })
    });

    $('.purchase_button').click(function() {
        msgStr = $('#hey').html();
        msgStr = msgStr + ' THERE!';
        $('#hey').html(msgStr);
    });

});