from .models import KeyBoard

### Клавиатура
class btnList():
    def __int__(self):
        self._btnLst = KeyBoard.objects.all().values()

    @property
    def allBtn(self):
        return self._btnLst