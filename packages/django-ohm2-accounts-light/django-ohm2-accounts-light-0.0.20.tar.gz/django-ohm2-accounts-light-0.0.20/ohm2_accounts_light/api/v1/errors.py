from django.utils.translation import ugettext as _

BASE_ERROR_CODE = 499264

USER_ALREADY_LOGGED_IN = {
	"code" : BASE_ERROR_CODE | 1,
	"message" : _("The user is already logged in"),
}
USER_ALREADY_EXIST = {
	"code" : BASE_ERROR_CODE | 2,
	"message" : _("The user already exist"),
}
THE_PASSWORD_IS_NOT_SECURE = {
	"code" : BASE_ERROR_CODE | 3,
	"message" : _("The password is not secure"),
}
INVALID_EMAIL = {
	"code" : BASE_ERROR_CODE | 4,
	"message" : _("The email is not valid"),
}
SIGNUPS_DISABLED = {
	"code" : BASE_ERROR_CODE | 5,
	"message" : _("Signups are currently disabled"),
}
EMAIL_LOGIN_DISABLED = {
	"code" : BASE_ERROR_CODE | 6,
	"message" : _("Email login is disabled"),
}
WRONG_CREDENTIALS = {
	"code" : BASE_ERROR_CODE | 7,
	"message" : _("Wrong credentials"),
}
PASSWORD_RESET_IDENTITY_AND_CODE_CANT_BE_BOTH_EMPTY = {
	"code" : BASE_ERROR_CODE | 8,
	"message" : _("Identity and code can't be both empty"),
}
PASSWORD_RESET_INVALID = {
	"code" : BASE_ERROR_CODE | 9,
	"message" : _("Password reset invalid"),
}
PASSWORD_RESET_ALREADY_ACTIVATED = {
	"code" : BASE_ERROR_CODE | 10,
	"message" : _("Password reset already activated"),
}
SIGNUP_PIPELINE_FAILED = {
	"code" : BASE_ERROR_CODE | 11,
	"message" : _("Signup pipeline failed"),
}



