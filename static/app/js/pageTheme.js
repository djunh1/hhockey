$(document).ready(function() {

        /*  FORM PLACEHOLDERS -  ENTIRE APPLICATION */

        /* Login Form Placeholders */
        $("#id_login-username").attr('placeholder', 'Email Address');
        $("#id_login-password").attr('placeholder', 'Password');

        /* Password Change Form Placeholders */
        $("#id_old_password").attr('placeholder', 'Old Password');
        $("#id_new_password1").attr('placeholder', 'New Password');
        $("#id_new_password2").attr('placeholder', 'ReType New Password');

        /* Password Reset forms */
        $("#id_email").attr('placeholder', 'Email Address');

        /* Registration */
        $("#id_registration-email").attr('placeholder', 'Email');
        $("#id_registration-password1").attr('placeholder', 'Enter Password');
        $("#id_registration-password2").attr('placeholder', 'Re Enter Password');

        /* NAVBAR MENU */

        $('#nav-cart-toggle').on('click', function (e) {
             $('#nav-list').toggleClass("menu-cart");
        });

});