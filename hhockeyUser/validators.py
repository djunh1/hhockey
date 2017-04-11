oscar.core.validators import CommonPasswordValidator as CoreCommonPasswordValidator

class CommonPasswordValidator(CoreCommonPasswordValidator):

    def clean_password(self, password):
        if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$', password):
            return password
        else:
            raise ValidationError("Your password needs to contain one upper case letter, and one number.  Do not use "
                                  "special characters.  Please try a new password.")