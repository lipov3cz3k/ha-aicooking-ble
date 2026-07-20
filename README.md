# Aicooking Bluetooth Integration for Home Assistant

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/default)
[![Validate Integration](https://img.shields.io/github/actions/workflow/status/lipov3cz3k/ha-aicooking-ble/validate.yml?branch=main&style=for-the-badge&label=Validate)](https://github.com/lipov3cz3k/ha-aicooking-ble/actions/workflows/validate.yml)
[![GitHub Release](https://img.shields.io/github/v/release/lipov3cz3k/ha-aicooking-ble?style=for-the-badge&color=blue)](https://github.com/lipov3cz3k/ha-aicooking-ble/releases)
[![License](https://img.shields.io/github/license/lipov3cz3k/ha-aicooking-ble?style=for-the-badge)](LICENSE)

Home Assistant custom integration for **Aicooking (Ai Cooking)** Bluetooth wireless meat thermometers.

It passively listens to Bluetooth advertising packets broadcast by the device in real-time, providing instant temperature updates with zero impact on battery life.

---

## ⚡ Features

- ⚡ **Passive BLE Listener**: Reads temperature packets broadcasted over Bluetooth advertising.
- 📡 **ESPHome Bluetooth Proxy Support**: Seamlessly works with ESPHome Bluetooth proxies for unlimited range across your home & garden.
- 🌡️ **Real-Time Temperature Monitoring**: Reports meat probe temperature in °C / °F.
- 📶 **Signal Strength (RSSI)**: Optional sensor to track Bluetooth signal quality.
- 🔄 **Auto Discovery**: Automatically discovers nearby thermometers in Home Assistant.

---

## 📱 Supported Devices

The integration supports BLE meat probes operating under the Aicooking protocol (broadcast manufacturer ID `0x55AA` / `21930` or local name `BBQ*`).

<img src="images/tesla_bbq100.webp" alt="Tesla Cook BBQ100" width="220" align="right" />

| Manufacturer / Brand | Model / Local Name | Details |
|----------------------|--------------------|---------|
| **Tesla Cook** | BBQ100 | Smart wireless meat thermometer |
| **Chuangxinlian** | CXL001 / CXL001-Y | [FCC ID 2A2D2-CXL001-C](https://fcc.report/FCC-ID/2A2D2-CXL001-C) |
| **Aicooking** | BBQ* | Any BLE probe broadcasting `BBQ*` advertisement |

---

## 📊 Sensors Provided

| Sensor | Entity ID | Device Class | Unit |
|--------|-----------|--------------|------|
| **Probe Temperature** | `sensor.bbq_temperature` | `temperature` | °C / °F |
| **Signal Strength (RSSI)** | `sensor.bbq_signal_strength` | `signal_strength` | dBm (Disabled by default) |

---

## 🚀 Quick Setup with HACS

### 1. Add Custom Repository to HACS

Click the button below to add this repository directly to HACS:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=lipov3cz3k&repository=ha-aicooking-ble&category=integration)

*Or manually in HACS:*
1. Open **HACS** → **Integrations** → **⋮** (top right menu) → **Custom repositories**.
2. URL: `https://github.com/lipov3cz3k/ha-aicooking-ble`
3. Category: **Integration**
4. Click **Add**, then click **Download**.
5. **Restart Home Assistant**.

---

### 2. Add Integration to Home Assistant

Click the button below to start setting up the integration:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=aicooking_ble)

*Or manually in Home Assistant:*
1. Go to **Settings** → **Devices & Services** → **Add Integration**.
2. Search for **Aicooking Bluetooth**.
3. Select your discovered probe from the list and confirm setup.

---

## 🛠️ Manual Installation (Alternative)

If you do not use HACS:
1. Download the latest release `.zip` from [Releases](https://github.com/lipov3cz3k/ha-aicooking-ble/releases).
2. Copy the `custom_components/aicooking_ble` folder into your Home Assistant `/config/custom_components/` directory.
3. Restart Home Assistant.

---

## 📶 Coverage & Range Recommendation

Bluetooth range through thick oven doors or barbecue grills can be limited.

To extend range across your entire house or yard, we recommend using an **[ESPHome Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy.html)** (e.g., an inexpensive ESP32 board). Home Assistant will automatically receive advertisements forwarded by any proxy in your network without any extra configuration.

---

## 📄 License

Distributed under the [MIT License](LICENSE).
