$(document).ready(function() {
    $('.list-group-item.track-item').on('click', function(e) {
        window.location = $(this).find('a.track-link').attr('href');
        e.preventDefault();
    });

    $('.input-group-addon').on('click', function(e) {
        $(this).closest('form').submit();
        e.preventDefault();
    });
});
