import logging
import subprocess

from get_hostname import get_hostname

logger = logging.getLogger(__name__)


class Publisher:

    @staticmethod
    def send_statistics(receiver_ip: str, receiver_user: str, receiver_pass: str, stats: str, publisher_cntnr: str) -> bool:

        __topic__ = f"unbound/stats/{get_hostname('lower')}"

        try:
            subprocess.run(["mosquitto_pub", "-h", f"{receiver_ip}", "-u", f"{receiver_user}", "-P", f"{receiver_pass}","-q", "1", "-t",>
            logger.debug("Send statistics to MQTT broker successful.")
            success = True
        except subprocess.CalledProcessError as e:
            logger.error(
                f"Send statistics to MQTT broker failed: Exit code {e.return_code}, {e.stderr.strip()}")
            logger.error(
                f"Exception: {e}")
            success = False

        return success
