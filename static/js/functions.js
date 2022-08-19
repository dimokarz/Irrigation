let irrigLst

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
                irrigLst = data
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
                                    content: function () { return $('#pop_detail').html(); }
                                });
                            }
                        }
                    }
                }, 2000);
            });
            break;
    }
});

//Открыть выбранные системы
function btnSel(){
    let sel = []
    for (let i=0; i<irrigLst.length; i++){
        if ($('#chk' + irrigLst[i].states_system).prop('checked') == true){
            sel.push($('#chk' + irrigLst[i].states_system).val());
        }
    }
    switch (sel.length){
        case 1:
            window.open('/simple?first=1', '_self');
            break;
        case 2:
            if (sel[0] == sel[1] && sel[0] != 0  && sel[1] != 0){
                window.open('/simple?first=1&?second=4', '_self');
            }
            else{
                $('#mTxt1').text('Выбранные системы не могут работать в паре')
                $('#modAlert').modal('show')
            }
            break;
        default:
            $('#mTxt1').text('Вы можете выбрать не более двух систем');
            $('#modAlert').modal('show');
            break;
    }
}