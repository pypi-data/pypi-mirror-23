from xknx.knx import Address, DPTBinary, DPTArray, \
    DPTScaling, DPTTemperature, DPTLux, DPTWsp, DPTUElCurrentmA
from .device import Device

class Sensor(Device):

    def __init__(self,
                 xknx,
                 name,
                 group_address=None,
                 value_type=None,
                 device_class=None,
                 significant_bit=1,
                 device_updated_cb=None):
        # pylint: disable=too-many-arguments

        Device.__init__(self, xknx, name, device_updated_cb)

        if isinstance(group_address, (str, int)):
            group_address = Address(group_address)
        if not isinstance(significant_bit, int):
            raise TypeError()

        self.group_address = group_address
        self.value_type = value_type
        self.device_class = device_class
        self.significant_bit = significant_bit
        self.state = None


    @classmethod
    def from_config(cls, xknx, name, config):
        group_address = \
            config.get('group_address')
        value_type = \
            config.get('value_type')
        device_class = \
            config.get('device_class')
        significant_bit = \
            config.get('significant_bit', 1)

        return cls(xknx,
                   name,
                   group_address=group_address,
                   value_type=value_type,
                   device_class=device_class,
                   significant_bit=significant_bit)


    def has_group_address(self, group_address):
        return self.group_address == group_address


    def set_internal_state(self, state):
        if state != self.state:
            self.state = state
            self.after_update()

    def state_addresses(self):
        return [self.group_address,]


    def process(self, telegram):
        self.set_internal_state(telegram.payload)

    def is_binary(self):
        return self.value_type == 'binary'


    def binary_state(self):
        if not self.is_binary() or \
                not isinstance(self.state, DPTBinary):
            return False

        return self.state.value & (1 << (self.significant_bit-1)) != 0


    def unit_of_measurement(self):
        if self.value_type == 'percent':
            return "%"
        elif self.value_type == 'temperature':
            return "°C"
        elif self.value_type == 'brightness':
            return "lx"
        elif self.value_type == 'speed_ms':
            return "m/s"
        elif self.value_type == 'current':
            return "mA"
        else:
            return None


    def resolve_state(self):
        # pylint: disable=invalid-name,too-many-return-statements
        if self.state is None:
            return None

        elif self.value_type == 'percent' and \
                isinstance(self.state, DPTArray) and \
                len(self.state.value) == 1:
            # TODO: Instanciate DPTScaling object with DPTArray class
            return "{0}".format(DPTScaling().from_knx(self.state.value))
        elif self.value_type == 'binary':
            return self.binary_state()
        elif self.value_type == 'temperature':
            return DPTTemperature().from_knx(self.state.value)
        elif self.value_type == 'brightness':
            return DPTLux().from_knx(self.state.value)
        elif self.value_type == 'speed_ms':
            return DPTWsp().from_knx(self.state.value)
        elif self.value_type == 'current':
            return DPTUElCurrentmA().from_knx(self.state.value)
        elif isinstance(self.state, DPTArray):
            return ','.join('0x%02x'%i for i in self.state.value)

        elif isinstance(self.state, DPTBinary):
            return "{0:b}".format(self.state.value)

        raise TypeError()


    def __str__(self):
        return '<Sensor name="{0}" ' \
               'group_address="{1}" ' \
               'state="{2}" ' \
               'resolve_state="{3}" />' \
            .format(self.name,
                    self.group_address,
                    self.state,
                    self.resolve_state())


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
