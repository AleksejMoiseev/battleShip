from django import forms


class MyForm(forms.Form):
    message = forms.CharField(
        required=True, max_length=100, widget=forms.Textarea,)  #  required=True Делает поле обязательным стоит по умолчанию
#  max_length=100 ьфксимальная длина допустимая в поле формы, отображение формы в браузере
#     def clean_message(self):  # метод clean_ любой метод начинающтйся так запускается как валидация формы, может быть сколько угодно
#         print("!!!!!!!!!!", "мы попали сюда")
#         data = self.cleaned_data
#         message = data['message']
#         try:
#             if int(message) > 100:
#                 raise forms.ValidationError("Крутяк вызвана хорошая ошибка")  # Образец как нужно рейзить ошибки при
#                 # валидации форм, ошибки возвращаюся пользователю
#             return message
#         except ValueError:
#             raise forms.ValidationError("А Ну  давай корректные данные")

    def clean_new(self):
        data = self.cleaned_data
        message = data['message']
        print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ', message)