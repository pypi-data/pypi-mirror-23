#!/usr/bin/env python

"""
test_amt
----------------------------------

Tests for `amt` module's wsman.py file
"""
import mock
import testtools

from amt import wsman


def fake_uuid4():
    return "00000000-1111-2222-3333-444455556666"


class BaseTestCase(testtools.TestCase):

    def assertXmlEqual(self, one, two):
        one = one.strip()
        two = two.strip()
        array1 = [x.strip() for x in str(one).split("\n")]
        array2 = [x.strip() for x in str(two).split("\n")]
        self.maxDiff = None
        self.assertEqual(array1, array2)


class TestXMLGen(BaseTestCase):

    @mock.patch('uuid.uuid4', fake_uuid4)
    def test_get_request(self):
        uri = 'http://10.42.0.50:16992/wsman'
        res = ('http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/'
               'CIM_AssociatedPowerManagementService')

        shouldbe = """<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsman="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd">
<s:Header>
<wsa:Action s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/09/transfer/Get</wsa:Action>
<wsa:To s:mustUnderstand="true">http://10.42.0.50:16992/wsman</wsa:To>
<wsman:ResourceURI s:mustUnderstand="true">http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_AssociatedPowerManagementService</wsman:ResourceURI>
<wsa:MessageID s:mustUnderstand="true">uuid:00000000-1111-2222-3333-444455556666</wsa:MessageID>
<wsa:ReplyTo>
<wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
</wsa:ReplyTo>
</s:Header>
<s:Body/>
</s:Envelope>"""  # noqa

        self.assertXmlEqual(wsman.get_request(uri, res), shouldbe)

    @mock.patch('uuid.uuid4', fake_uuid4)
    def test_change_boot_to_pxe_request(self):
        uri = 'http://10.42.0.50:16992/wsman'

        shouldbe = """<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsman="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns:n1="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_BootConfigSetting">
<s:Header>
<wsa:Action s:mustUnderstand="true">http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_BootConfigSetting/ChangeBootOrder</wsa:Action>
<wsa:To s:mustUnderstand="true">http://10.42.0.50:16992/wsman</wsa:To>
<wsman:ResourceURI s:mustUnderstand="true">http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_BootConfigSetting</wsman:ResourceURI>
<wsa:MessageID s:mustUnderstand="true">uuid:00000000-1111-2222-3333-444455556666</wsa:MessageID>
<wsa:ReplyTo>
    <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
</wsa:ReplyTo>
<wsman:SelectorSet>
   <wsman:Selector Name="InstanceID">Intel(r) AMT: Boot Configuration 0</wsman:Selector>
</wsman:SelectorSet>
</s:Header>
<s:Body>
  <n1:ChangeBootOrder_INPUT>
     <n1:Source>
        <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
        <wsa:ReferenceParameters>
            <wsman:ResourceURI>http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_BootSourceSetting</wsman:ResourceURI>
            <wsman:SelectorSet>
                <wsman:Selector wsman:Name="InstanceID">Intel(r) AMT: Force PXE Boot</wsman:Selector>
            </wsman:SelectorSet>
         </wsa:ReferenceParameters>
     </n1:Source>
   </n1:ChangeBootOrder_INPUT>
</s:Body></s:Envelope>"""  # noqa

        self.assertXmlEqual(wsman.change_boot_to_pxe_request(uri), shouldbe)

    def test_change_boot_order_request_invalid_boot_device(self):
        uri = 'http://10.42.0.50:16992/wsman'
        self.assertRaises(AssertionError,
                          wsman.change_boot_order_request,
                          uri, 'pxe2')


class TestFriendlyPowerState(testtools.TestCase):

    def test_power_on(self):
        self.assertEqual(wsman.friendly_power_state('2'), 'on')
        self.assertEqual(wsman.friendly_power_state(2), 'on')

    def test_power_off(self):
        self.assertEqual(wsman.friendly_power_state('8'), 'off')
        self.assertEqual(wsman.friendly_power_state(8), 'off')

    def test_standby(self):
        self.assertEqual(wsman.friendly_power_state('4'), 'standby')
        self.assertEqual(wsman.friendly_power_state(4), 'standby')

    def test_reboot(self):
        self.assertEqual(wsman.friendly_power_state('5'), 'reboot')
        self.assertEqual(wsman.friendly_power_state(5), 'reboot')

    def test_hibernate(self):
        self.assertEqual(wsman.friendly_power_state('7'), 'hibernate')
        self.assertEqual(wsman.friendly_power_state(7), 'hibernate')

    def test_unknown(self):
        self.assertEqual(wsman.friendly_power_state('42'), 'unknown')
        self.assertEqual(wsman.friendly_power_state(42), 'unknown')

    def test_non_integer(self):
        self.assertRaises(ValueError, wsman.friendly_power_state, 'not-a-number')


class TestAmt(testtools.TestCase):

    def test_something(self):
        pass

# Local Variables:
# turn off whitespace mode because xml is *so* long
# eval: (whitespace-mode -1)
# End:
