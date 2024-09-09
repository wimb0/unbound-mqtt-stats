import argparse
import logging
import os
import subprocess

from get_statistics import Collector
from send_statistics import Publisher
from get_hostname import get_hostname

logger = logging.getLogger(__name__)


def main(receiver_ip, receiver_user, receiver_pass, reset_unbound_stats: bool):
    publisher_cntnr = f"mosquitto_{get_hostname('lower')}"

    logger.debug(f"Param reset_unbound_stats = {reset_unbound_stats}")
    unbound_stats = Collector.get_statistics(reset_unbound_stats)
    statistic_sent = Publisher.send_statistics(receiver_ip, receiver_user, receiver_pass, unbound_stats, publisher_cntnr)
    if statistic_sent:
        logger.debug(f"Unbound statistics sent successful.")
    else:
        logger.error(f"Unbound statistics failed. Check log for details.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("receiver_ip", help="IP address of MQTT Broker")
    parser.add_argument("receiver_user", help="Username for MQTT Broker")
    parser.add_argument("receiver_pass", help="Password for MQTT Broker")
    parser.add_argument("-nr", "--no-reset", action="store_false", dest="reset_unbound_stats",
                        help="Do not reset unbound statistics")
    parser.add_argument("--debug", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING,
                        help="Set loglevel to DEBUG")
    args = parser.parse_args()

    logdir = "log"
    if not os.path.isdir(logdir):
        os.makedirs(logdir)

    logging.basicConfig(level=args.loglevel, filename=f"{logdir}/unbound-stats.log",
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    main(args.receiver_ip, args.receiver_user, args.receiver_pass, args.reset_unbound_stats)







