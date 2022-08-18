$(document).ready(function() {

    // let popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    // let popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    //     return new bootstrap.Popover(popoverTriggerEl);
    // });

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
                    for (let key in data) {
                        $('#spState' + data[key].states_system).removeClass('bg-warning');
                        $('#spState' + data[key].states_system).removeClass('text-dark');
                        if (data[key].states_ctrl == false) {
                            $('#spState' + data[key].states_system).addClass('bg-secondary');
                            $('#spState' + data[key].states_system).text('Не доступна');
                        }
                        else {
                            $('#chk' + data[key].states_system).prop('disabled', false)
                            if (data[key].states_dir == 'N') {
                                $('#spState' + data[key].states_system).addClass('bg-danger');
                                $('#spState' + data[key].states_system).text('Остановлена');
                            }
                            else {
                                $('#spState' + data[key].states_system).addClass('bg-success');
                                $('#spState' + data[key].states_system).text('Запущена');
                                $('#spState' + data[key].states_system).popover({
                                    trigger: 'hover',
                                    html: true,
                                    content: function () {
                                        return $('#pop_detail').html();
                                    }
                                });
                            }
                        }
                    }
                }, 2000);
            });
            break;
    }

});