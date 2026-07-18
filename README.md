# Aicooking Bluetooth Integration for Home Assistant

Home Assistant integration for Aicooking (Ai Cooking) Bluetooth meat thermometers (e.g., Tesla Cook BBQ100 / Chuangxinlian CXL001).

This integration uses Home Assistant's native passive Bluetooth stack to receive temperature and signal strength advertisements in real-time, supporting Bluetooth USB dongles and ESPHome Bluetooth proxies.

## Installation

### Method 1: HACS (Recommended)

1. Open **HACS** in your Home Assistant.
2. Go to **Integrations**.
3. Click the three dots in the top-right corner and select **Custom repositories**.
4. Paste the URL of this repository: `https://github.com/lipov3cz3k/ha-aicooking-ble`
5. Select **Integration** as the Category and click **Add**.
6. Find **Aicooking Bluetooth** in the HACS catalog, click **Download**, and download the integration.
7. Restart Home Assistant.

### Method 2: Manual Installation

1. Download the latest release or clone this repository.
2. Copy the `custom_components/aicooking_ble` directory into your Home Assistant's `custom_components` folder.
3. Restart Home Assistant.

## Configuration

1. In Home Assistant, go to **Settings** -> **Devices & Services**.
2. Click **Add Integration**.
3. Search for **Aicooking Bluetooth** and follow the instructions to set it up (it will auto-discover nearby active thermometers).
