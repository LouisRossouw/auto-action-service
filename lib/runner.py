import os
import logging
import requests

from logging.handlers import RotatingFileHandler

from lib.utils import is_internet_available, start_time

this_dir = os.path.dirname(__file__)

handler = RotatingFileHandler(
    "data/service.log", maxBytes=1_000_000, backupCount=3)

console = logging.StreamHandler()

logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_action(settings, action_slug):
    st = start_time()

    if not is_internet_available():
        logging.info("No internet connection..")
        return

    action = settings.actions_by_slug[action_slug]
    device = settings.devices_by_slug[action["device"]]

    url = f"{device['base_url']}{action['route']}"

    method = action.get("method", "GET")
    payload = action.get("payload")

    try:

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            timeout=5
        )

        response.raise_for_status()

        logging.info(
            "Executed %s -> %s payload=%s",
            action_slug,
            url,
            payload
        )

    #     elapsed_time = calculate_request_time(st)

    #     date_now = datetime.now()
    #     manifest_path = os.path.join(settings.data_dir, f"{name}_manifest.json")

    #     data = {
    #         "system_name": settings.name,
    #         "system_slug": settings.slug,
    #         "elapsed_time": elapsed_time,
    #         "timestamp": date_now.timestamp(),
    #         "datetime": date_now.strftime("%d-%m-%Y %H:%M")}

    #     # Update recorded results - this is to compare against future results.
    #     write_to_json(results_path, results)

    #     # Manifest
    #     write_to_json(manifest_path, {
    #         **web_task,
    #         **data
    #     })

    #     # System
    #     write_to_json(settings.service_path, data)

    except Exception as e:
        logging.error("Action failed: %s - %s", action_slug, e)


if __name__ == "__main__":
    pass
