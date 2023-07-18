$(document).ready(function () {

    $('#clicker').click(function () {
        let a, clicks;
        a = $(this).attr('data-user');
        clicks = $(this).attr('data-click-upgraded');
        const token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/add_points/',
            type: 'POST',
            success: function (data) {
                $('#points_count').html(data.points);
                $('#user-counter').html(data.lifetime_points);
            },
            headers: { 'X-CSRFToken': token },
            data: { 'a': a, 'clicks': clicks }
        })
    });

    $('#darkmode-button').click(function () {
        let d;
        d = $(this).attr('data-user');
        const token = $(this).attr('data-csrf');

        $.ajax({
            url: '/clicker_app/darkmode/',
            type: 'POST',
            success: function (data) {
                $('#darkmode-button').html(data);
            },
            headers: { 'X-CSRFToken': token },
            data: { 'user-id': d }
        })
    });

    $('.purchase_button').click(function () {
        let a, upgrade;
        a = $(this).attr('data-user');
        upgrade = $(this).attr('data-upgrade');
        const token = $(this).attr('data-csrf');

        let s1 = "#upgrade-" + String(upgrade) + "-1";
        let s2 = "#upgrade-" + String(upgrade) + "-2";

        $.ajax({
            url: '/clicker_app/purchase/',
            type: 'POST',
            success: function (data) {
                $(s1).html(data.cost_instance);
                $(s2).html(data.quantity);
                location.reload();
            },
            headers: { 'X-CSRFToken': token },
            data: { 'user-id': a, 'upgrade': upgrade }
        })
    });

});