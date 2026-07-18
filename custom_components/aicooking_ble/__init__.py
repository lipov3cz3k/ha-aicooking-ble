"""The Aicooking Bluetooth BLE integration."""

from functools import partial
import logging

from aicooking_ble import AicookingBluetoothDeviceData

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .coordinator import (
    AicookingBLEBluetoothProcessorCoordinator,
    AicookingBLEConfigEntry,
    process_service_info,
)

PLATFORMS: list[Platform] = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: AicookingBLEConfigEntry) -> bool:
    """Set up Aicooking BLE device from a config entry."""
    address = entry.unique_id
    assert address is not None
    data = AicookingBluetoothDeviceData()
    entry.runtime_data = coordinator = AicookingBLEBluetoothProcessorCoordinator(
        hass,
        _LOGGER,
        address=address,
        update_method=partial(process_service_info, hass, entry),
        device_data=data,
        entry=entry,
    )
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    # only start after all platforms have had a chance to subscribe
    entry.async_on_unload(coordinator.async_start())
    return True


async def async_unload_entry(hass: HomeAssistant, entry: AicookingBLEConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
