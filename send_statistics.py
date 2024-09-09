import logging
import subprocess

logger = logging.getLogger(__name__)


class Publisher:
    @staticmethod
    def send_statistics(
        receiver_ip: str,
        receiver_user: str,
        receiver_pass: str,
        stats: str,
        unbound_hostname: str,
    ) -> bool:
        __topic__ = f"unbound/stats/{unbound_hostname}"

        try:
            mqttsend = subprocess.run(
                (
                    [
                        "mosquitto_pub",
                        "-h",
                        f"{receiver_ip}",
                        "-u",
                        f"{receiver_user}",
                        "-P",
                        f"{receiver_pass}",
                        "-q",
                        "1",
                        "-t",
                        f"{__topic__}",
                        "-m",
                        f"{stats}",
                    ]
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            mqttsend.check_returncode()
            logger.debug("Send statistics to MQTT broker successful.")
            success = True
        except subprocess.CalledProcessError as e:
            logger.error(
                f"Send statistics to MQTT broker failed: Exit code {e.returncode}, {e.stderr.strip()}"
            )
            logger.error(f"Exception: {e}")
            success = False

        return success
