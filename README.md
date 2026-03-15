# auto-action-service

Work-in-progress automation service for triggering HTTP actions on devices using scheduled jobs.

This service allows you to control devices (such as WLED or ESP32 devices) using simple JSON configuration files.
Schedules are handled using APScheduler and can run using **cron** or **interval** triggers.

---

# How It Works

The service uses three configuration files:

```
configs/
 ├─ devices.json
 ├─ actions.json
 └─ schedules.json
```

Each layer has a different responsibility.

| File               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| **devices.json**   | Defines the devices and their base URLs          |
| **actions.json**   | Defines commands that can be executed on devices |
| **schedules.json** | Defines when actions should run                  |

The scheduler loads these configs at startup and automatically creates jobs.

---

# Devices

Devices represent the physical hardware or services that will receive HTTP requests.

Example:

```json
[
  {
    "slug": "minigt-desk-display",
    "type": "wled",
    "base_url": "http://10.0.0.156"
  }
]
```

Fields:

| Field    | Description                                   |
| -------- | --------------------------------------------- |
| slug     | Unique identifier for the device              |
| type     | Device type (optional, used for organization) |
| base_url | Base URL used when building requests          |

---

# Actions

Actions define **what command to execute** on a device.

Example:

```json
[
  {
    "slug": "display-on",
    "device": "minigt-desk-display",
    "method": "POST",
    "route": "/json/state",
    "payload": {
      "on": true
    }
  },
  {
    "slug": "display-off",
    "device": "minigt-desk-display",
    "method": "POST",
    "route": "/json/state",
    "payload": {
      "on": false
    }
  }
]
```

Fields:

| Field   | Description                               |
| ------- | ----------------------------------------- |
| slug    | Unique identifier for the action          |
| device  | Device slug the action belongs to         |
| method  | HTTP method (GET, POST, PUT, etc.)        |
| route   | Endpoint path appended to device base_url |
| payload | Optional JSON payload                     |

The service builds the final request like:

```
{device.base_url}{route}
```

Example:

```
http://10.0.0.156/json/state
```

---

# Schedules

Schedules determine **when actions are executed**.

Example:

```json
[
  {
    "name": "display-on-evening",
    "action": "di
```
