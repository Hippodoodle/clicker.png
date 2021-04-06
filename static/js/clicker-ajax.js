$(document).ready(function () {

    $('#clicker').click(function () {
        var a;
        a = $(this).attr('data-user');
        clicks = $(this).attr('data-click-upgraded');
        token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/add_points/',
            type: 'POST',
            success: function (data) {
                $('#points_count').html(data.points);
                $('#user-counter').html(data.lifetime_points);
            },
            headers: {'X-CSRFToken': token},
            data: {'a': a, 'clicks': clicks}
        })
    });

    $('#darkmode-button').click(function () {
        var d;
        d = $(this).attr('data-user');
        token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/darkmode/',
            type: 'POST',
            success: function (data) {
                $('#darkmode-button').html(data);
            },
            headers: {'X-CSRFToken': token},
            data: {'user-id': d}
        })
    });

    $('.purchase_button').click(function () {
        var a = $(this).attr('data-user');
        var token = $(this).attr('data-csrf');
        var upgrade = $(this).attr('data-upgrade');

        var s11 = '#upgrade-'
        var s12 = String(upgrade)
        var s13 = '-1'
        var s1 =  s11.concat(s12, s13);

        var s23 = '-2'
        var s2 =  s11.concat(s12, s23);

        $.ajax({
            url: '/clicker_app/purchase/',
            type: 'POST',
            success: function (data) {
                $(s1).html(data.cost_instance);
                $(s2).html(data.quantity);
                location.reload();
            },
            headers: {'X-CSRFToken': token},
            data: {'user-id': a, 'upgrade': upgrade}
        })
    });

});