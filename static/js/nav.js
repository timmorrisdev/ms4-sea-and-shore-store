$(document).ready(function () {

    $('.dropdown').on('mouseover', function () {
        $(this).children('.dropdown-menu').css({
            'display': 'block',
        })
    })
    $('.dropdown').on('mouseout', function () {
        $(this).children('.dropdown-menu').css({
            'display': 'none',
        })
    })

})