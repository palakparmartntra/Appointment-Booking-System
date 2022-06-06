from allauth.account.models import EmailAddress


class Account():
    def set_email(self, userdata, *args, **kwargs):
        """
        store the data in EmailAddress model of created user using FK.
        """
        userd = EmailAddress.objects.get_or_create(user=userdata,
                                                   email=userdata.email,
                                                   verified=True,
                                                   primary=True)
        return userd
