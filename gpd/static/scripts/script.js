// Code goes here

// Code goes here
// Code goes here
$(function () {
    $('#gpd-table-parameters').on('hide.bs.collapse', function () {
        $('#button').html('<span class="glyphicon glyphicon-triangle-bottom"></span> Display Options');
    })
    $('#gpd-table-parameters').on('show.bs.collapse', function () {
        $('#button').html('<span class="glyphicon glyphicon-triangle-top"></span> Display Options');
    })
})