from django import forms
from models import Request

#
# class UserAdminForm(forms.ModelForm):
#     """
#     A custom form to add validation rules which cannot live in the
#     model. We check that users belonging to various groups actually
#     have the corresponding profiles.
#     """
#     class Meta:
#         model = Request
#
#     def __hasNumbers(self,inputString):
#         return any(char.isdigit() for char in inputString)
#
#     def clean(self):
#         name = self.data['firstname']
#         # some validations
#         if self.__hasNumbers(name):
#             self.data['fisrstname'] = 'Debil'
#         return self.cleaned_data