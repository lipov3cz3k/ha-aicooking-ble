"""Test the Aicooking BLE sensors."""

from homeassistant.components.aicooking_ble.const import DOMAIN
from homeassistant.components.sensor import ATTR_STATE_CLASS
from homeassistant.const import (
    ATTR_FRIENDLY_NAME,
    ATTR_UNIT_OF_MEASUREMENT,
)
from homeassistant.core import HomeAssistant

from . import BBQ100_SERVICE_INFO
from tests.common import MockConfigEntry
from tests.components.bluetooth import inject_bluetooth_service_info


async def test_sensors(hass: HomeAssistant) -> None:
    """Test setting up creates the sensors."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="6956A80D-F871-021A-F38C-891A45EEEEC0",
    )
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_all()) == 0
    inject_bluetooth_service_info(hass, BBQ100_SERVICE_INFO)
    await hass.async_block_till_done()

    # We should have temperature and signal strength sensors registered
    assert len(hass.states.async_all()) == 2

    temp_sensor = hass.states.get("sensor.bbq_temperature")
    assert temp_sensor.state == "25.7"
    assert temp_sensor.attributes[ATTR_FRIENDLY_NAME] == "BBQ Temperature"
    assert temp_sensor.attributes[ATTR_UNIT_OF_MEASUREMENT] == "°C"
    assert temp_sensor.attributes[ATTR_STATE_CLASS] == "measurement"
