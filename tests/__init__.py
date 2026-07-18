"""Tests for the Aicooking Bluetooth integration."""

from home_assistant_bluetooth import BluetoothServiceInfo

NOT_AICOOKING_SERVICE_INFO = BluetoothServiceInfo(
    name="Not it",
    address="61DE521B-F0BF-9F44-64D4-75BBE1738105",
    rssi=-63,
    manufacturer_data={3234: b"\x00\x01"},
    service_data={},
    service_uuids=[],
    source="local",
)

BBQ100_SERVICE_INFO = BluetoothServiceInfo(
    name="BBQ",
    address="6956A80D-F871-021A-F38C-891A45EEEEC0",
    rssi=-54,
    manufacturer_data={21930: b"25.7"},
    service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
    service_data={},
    source="local",
)
