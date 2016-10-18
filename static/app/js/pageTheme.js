$(document).ready(function() {

        /*  FORM PLACEHOLDERS -  ENTIRE APPLICATION */

        /* Login Form Placeholders */
        $("#id_username").attr('placeholder', 'User Name');
        $("#id_password").attr('placeholder', 'Password');

        /* Password Change Form Placeholders */
        $("#id_old_password").attr('placeholder', 'Old Password');
        $("#id_new_password1").attr('placeholder', 'New Password');
        $("#id_new_password2").attr('placeholder', 'ReType New Password');

        /* Password Reset forms */
        $("#id_email").attr('placeholder', 'Email Address');

        /* Registration */
        $("#id_first_name").attr('placeholder', 'Name');
        $("#id_password2").attr('placeholder', 'Enter Password Again');

});