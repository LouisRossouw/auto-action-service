# auto-action-service

WIP!

A lightweight automation service for triggering HTTP actions on devices using scheduled jobs.

## Overview

The service core is driven by four JSON configuration files in the `configs/` directory.

---

## Configurations

### 1. Main Settings (`config.json`)
Defines the service environment and notification settings.

- `host` / `port`: The address and port the API service runs on.
- `notifications`: Boolean to enable/disable Telegram alerts.
- `tele_jam_api_baseurl`: Endpoint for the notification relay.

### 2. Devices (`devices.json`)
Lists the hardware targets available for actions.

```json
[
  {
    "slug": "living-room-wled",
    "base_url": "http://10.0.0.156",
    "type": "wled"
  }
]
```

### 3. Actions (`actions.json`)
Defines specific HTTP commands to send to devices.

```json
[
  {
    "slug": "lights-on",
    "device": "living-room-wled",
    "method": "POST",
    "route": "/json/state",
    "payload": { "on": true }
  }
]
```

### 4. Schedules (`schedules.json`)
Determines when actions are triggered (supports `cron` and `interval`).

```json
[
  {
    "name": "sunset-on",
    "action": "lights-on",
    "trigger": "cron",
    "hour": 18,
    "minute": 0
  }
]
```

---

## Setup & Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Launch**:
   ```bash
   python main.py
   ```

Alternatively, use Docker:
```bash
docker-compose up -d
```
