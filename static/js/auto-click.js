$(document).ready(function () {

    $('#clicker').ready(function () {
        setInterval(function () {
            let a, clicks;
            a = $('#clicker').attr('data-user');
            clicks = $('#clicker').attr('data-cps');
            const token = $('#clicker').attr('data-csrf');

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
        }, 1000);
    });

})