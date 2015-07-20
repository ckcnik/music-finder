/**
 * Created by denis on 20.07.15.
 */
$( document ).ready(function() {
    $('.table').height($(window).height());
    $(window).resize(function () {
        $('.table').height($(window).height());
    });
});
