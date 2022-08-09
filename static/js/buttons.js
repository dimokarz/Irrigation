//Активация кнопки "Открыть"
$('.form-check-input').on('click', function() {
    $('#btn_sel').prop('disabled', false);
});

$('.btn').on('click', function (e) {
   switch (e.target.id) {
       case 'btn_sel':
           btn_sel();
           break;
   }
});