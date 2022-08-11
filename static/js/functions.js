$(document).ready(function() {
    switch (document.location.pathname) {
        case '/login/':
            $('body').css('background-size', 'cover');
            $('body').css('background-image', 'url(/static/img/valley.jpg)');
            break;
        case '/simple/':
            $('body').css('background-image', '');
            break;
        default:
            $('body').css('background-image', '');
            $.getJSON('/states_list', function (data){
                for (key in data) {
                    alert(data[key].states_ctrl)
                }
            });
            break;
    }
});