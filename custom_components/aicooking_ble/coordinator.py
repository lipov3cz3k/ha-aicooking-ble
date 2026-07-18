"""The Aicooking Bluetooth integration."""

from collections.abc import Callable
import logging
from logging import Logger

from aicooking_ble import AicookingBluetoothDeviceData, SensorUpdate

from homeassistant.components.bluetooth import (
    BluetoothScanningMode,
    BluetoothServiceInfoBleak,
)
from homeassistant.components.bluetooth.passive_update_processor import (
    PassiveBluetoothDataProcessor,
    PassiveBluetoothProcessorCoordinator,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

type AicookingBLEConfigEntry = ConfigEntry[AicookingBLEBluetoothProcessorCoordinator]


def process_service_info(
    hass: HomeAssistant,
    entry: AicookingBLEConfigEntry,
    service_info: BluetoothServiceInfoBleak,
) -> SensorUpdate:
    """Process a BluetoothServiceInfoBleak.

    Runs side effects and returns sensor data.
    """
    coordinator = entry.runtime_data
    data = coordinator.device_data
    update = data.update(service_info)

    if not coordinator.device_name and data.title:
        coordinator.device_name = data.title

    return update


class AicookingBLEBluetoothProcessorCoordinator(
    PassiveBluetoothProcessorCoordinator[SensorUpdate]
):
    """Define an Aicooking BLE Bluetooth Passive Update Processor Coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        logger: Logger,
        address: str,
        update_method: Callable[[BluetoothServiceInfoBleak], SensorUpdate],
        device_data: AicookingBluetoothDeviceData,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the Aicooking BLE Bluetooth Passive Update Processor Coordinator."""
        super().__init__(
            hass, logger, address, BluetoothScanningMode.PASSIVE, update_method
        )
        self.device_data = device_data
        self.entry = entry


class AicookingBLEPassiveBluetoothDataProcessor[_T](
    PassiveBluetoothDataProcessor[_T, SensorUpdate]
):
    """Define an Aicooking BLE Bluetooth Passive Update Data Processor."""

    coordinator: AicookingBLEBluetoothProcessorCoordinator
