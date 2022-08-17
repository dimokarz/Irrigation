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
            //Статусы систем
            $.getJSON('/states_list', function (data){
                for (let i = 0; i < 2; i++) {
                    for (let y = 0; y <= data.length; y++) {
                        $('#spState' + y).fadeTo('slow', 0.0).fadeTo('slow', 1.0);
                    }
                }
                setTimeout(function () {
                    for (key in data) {
                        $('#spState' + key).removeClass('bg-warning');
                        $('#spState' + key).removeClass('text-dark');
                        if (data[key].states_ctrl == false) {
                            $('#spState' + key).addClass('bg-secondary');
                            $('#spState' + key).text('Не доступна');
                        }
                        else {
                            if (data[key].states_dir == 'N') {
                                $('#spState' + key).addClass('bg-danger');
                                $('#spState' + key).text('Остановлена');
                            }
                            else {
                                $('#spState' + key).addClass('bg-success');
                                $('#spState' + key).text('Запущена');
                            }
                        }
                    }
                }, 2000);
            });
            break;
    }
});