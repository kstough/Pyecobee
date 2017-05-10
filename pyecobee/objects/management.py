"""
This module is home to the Management class
"""
from .ecobee_object import EcobeeObject


class Management(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Management.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_administrative_contact', '_billing_contact', '_name', '_phone', '_email', '_web', '_show_alert_idt',
                 '_show_alert_web']

    attribute_name_map = {'administrative_contact': 'administrativeContact',
                          'administrativeContact': 'administrative_contact', 'billing_contact': 'billingContact',
                          'billingContact': 'billing_contact', 'name': 'name', 'phone': 'phone', 'email': 'email',
                          'web': 'web', 'show_alert_idt': 'showAlertIdt', 'showAlertIdt': 'show_alert_idt',
                          'show_alert_web': 'showAlertWeb', 'showAlertWeb': 'show_alert_web'}

    attribute_type_map = {'administrative_contact': 'six.text_type', 'billing_contact': 'six.text_type',
                          'name': 'six.text_type', 'phone': 'six.text_type', 'email': 'six.text_type',
                          'web': 'six.text_type', 'show_alert_idt': 'bool', 'show_alert_web': 'bool'}

    def __init__(self, administrative_contact=None, billing_contact=None, name=None, phone=None, email=None, web=None,
                 show_alert_idt=None, show_alert_web=None):
        """
        Construct a Management instance
        """
        self._administrative_contact = administrative_contact
        self._billing_contact = billing_contact
        self._name = name
        self._phone = phone
        self._email = email
        self._web = web
        self._show_alert_idt = show_alert_idt
        self._show_alert_web = show_alert_web

    @property
    def administrative_contact(self):
        """
        Gets the administrative_contact attribute of this Management instance.

        :return: The value of the administrative_contact attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._administrative_contact

    @property
    def billing_contact(self):
        """
        Gets the billing_contact attribute of this Management instance.

        :return: The value of the billing_contact attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._billing_contact

    @property
    def name(self):
        """
        Gets the name attribute of this Management instance.

        :return: The value of the name attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def phone(self):
        """
        Gets the phone attribute of this Management instance.

        :return: The value of the phone attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._phone

    @property
    def email(self):
        """
        Gets the email attribute of this Management instance.

        :return: The value of the email attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._email

    @property
    def web(self):
        """
        Gets the web attribute of this Management instance.

        :return: The value of the web attribute of this Management instance.
        :rtype: six.text_type
        """

        return self._web

    @property
    def show_alert_idt(self):
        """
        Gets the show_alert_idt attribute of this Management instance.

        :return: The value of the show_alert_idt attribute of this Management instance.
        :rtype: bool
        """

        return self._show_alert_idt

    @property
    def show_alert_web(self):
        """
        Gets the show_alert_web attribute of this Management instance.

        :return: The value of the show_alert_web attribute of this Management instance.
        :rtype: bool
        """

        return self._show_alert_web