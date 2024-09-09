import json
import logging
import subprocess


logger = logging.getLogger(__name__)


class Collector:

    @staticmethod
    def __convert_to_json(stats):
        tmp_stats = stats.replace("t", '{"t', 1).replace("=", '":').replace("\n", ',"')
        tmp_stats = tmp_stats[:-2]
        tmp_stats += '}'
        logger.debug(f"Converted unbound statistics: {tmp_stats}")

        try:
            json_stats = json.loads(tmp_stats)
            logger.debug(f"JSONified unbound statistics: {json_stats}")
            # dumps to JSON string, because json.loads create single quotes. For JSON format double quotes are required.
            return json.dumps(json_stats)

        except json.decoder.JSONDecodeError as e:
            logger.error(f"Not possible to create json statistics. Exception: {e}, \n "
                         f"stats: {tmp_stats}")

    @staticmethod
    def get_statistics(reset_unbound_stats: bool = False):
        if reset_unbound_stats:
            stats_param = "stats"
        else:
            stats_param = "stats_noreset"

        logger.debug(f"Set <stats_param> = '{stats_param}'")

        try:
            stats = subprocess.run(["/usr/sbin/unbound-control", stats_param], stdout = subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)
            stats.check_returncode()
            success = True
        except subprocess.CalledProcessError as e:
            logger.error(
                f"Get Unbound stats from unbound-control failed: Exit code {e.returncode}, {e.stderr.strip()}")
            logger.error(
                f"Exception: {e}")
            success = False

        if success == True:
            stats_json = Collector.__convert_to_json(stats.stdout)
            if stats_json:
                logger.debug(type(stats_json))
                logger.debug(f"Received unbound statistics: {stats_json}")
                return stats_json
            else:
                logger.error(f"No json statistics available. type = {type(stats_json)}, payload = {stats_json}")
