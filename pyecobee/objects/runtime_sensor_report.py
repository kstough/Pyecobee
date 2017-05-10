"""
This module is home to the RuntimeSensorReport class
"""
from .ecobee_object import EcobeeObject


class RuntimeSensorReport(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/RuntimeSensorReport.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_thermostat_identifier', '_sensors', '_columns', '_data']

    attribute_name_map = {'thermostat_identifier': 'thermostatIdentifier',
                          'thermostatIdentifier': 'thermostat_identifier', 'sensors': 'sensors', 'columns': 'columns',
                          'data': 'data'}

    attribute_type_map = {'thermostat_identifier': 'six.text_type', 'sensors': 'List[RuntimeSensorMetadata]',
                          'columns': 'List[six.text_type]', 'data': 'List[six.text_type]'}

    def __init__(self, thermostat_identifier=None, sensors=None, columns=None, data=None):
        """
        Construct a RuntimeSensorReport instance
        """
        self._thermostat_identifier = thermostat_identifier
        self._sensors = sensors
        self._columns = columns
        self._data = data

    @property
    def thermostat_identifier(self):
        """
        Gets the thermostat_identifier attribute of this RuntimeSensorReport instance.

        :return: The value of the thermostat_identifier attribute of this RuntimeSensorReport instance.
        :rtype: six.text_type
        """

        return self._thermostat_identifier

    @property
    def sensors(self):
        """
        Gets the sensors attribute of this RuntimeSensorReport instance.

        :return: The value of the sensors attribute of this RuntimeSensorReport instance.
        :rtype: List[RuntimeSensorMetadata]
        """

        return self._sensors

    @property
    def columns(self):
        """
        Gets the columns attribute of this RuntimeSensorReport instance.

        :return: The value of the columns attribute of this RuntimeSensorReport instance.
        :rtype: List[six.text_type]
        """

        return self._columns

    @property
    def data(self):
        """
        Gets the data attribute of this RuntimeSensorReport instance.

        :return: The value of the data attribute of this RuntimeSensorReport instance.
        :rtype: List[six.text_type]
        """

        return self._data