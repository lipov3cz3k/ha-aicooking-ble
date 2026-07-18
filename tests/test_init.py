"""Test the Aicooking Bluetooth init."""

from unittest.mock import patch

from homeassistant.components.aicooking_ble.const import DOMAIN
from homeassistant.components.bluetooth import BluetoothScanningMode
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry


async def test_setup_unload_entry(hass: HomeAssistant) -> None:
    """Test setup and unload of config entry."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="6956A80D-F871-021A-F38C-891A45EEEEC0",
        data={},
    )
    entry.add_to_hass(hass)

    with patch(
        "homeassistant.components.bluetooth.update_coordinator.async_register_callback"
    ) as mock_register_callback:
        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

    assert mock_register_callback.call_args.args[3] == BluetoothScanningMode.PASSIVE

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
