// Проверка выбранных систем
function btn_sel() {
    let duet = [];
    let valley = [];
    let inputElems = document.getElementsByTagName("input");
    let count = 0;

    for (let i = 0; i < inputElems.length; i++) {
        if (inputElems[i].type == "checkbox" && inputElems[i].checked == true) {
            count++;
            duet.push(inputElems[i].value);
            valley.push(inputElems[i].id);
        }
    }
    switch (count) {
        case 1:
            window.open("/simple?first=" + valley[0], "_self");
            break;
        case 2:
            if (duet[0] == duet[1] && duet[0] != 0) {
                window.open("/simple?first=" + valley[0] + "&second=" + valley[1], "_self");
            }
            else {
                $('#mal1').text("Выбранные системы не могут работать в паре");
                $('#modAlert').modal("show");
            }
            break;
        default:
            $('#mal1').text("Вы можете выбрать не более двух систем");
            $('#modAlert').modal("show");
            break;
    }
}