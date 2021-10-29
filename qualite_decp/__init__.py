""" Package qualite_decp pour le projet qualite-decp.
"""
import logging
import os

import yaml
import munch

# Définit un logger pour le projet
log_level = os.environ.get("LOG_LEVEL", "DEBUG")
if log_level == "DEBUG":
    level = logging.DEBUG
elif log_level == "INFO":
    level = logging.INFO
elif log_level == "WARNING":
    level = logging.WARNING
elif log_level == "ERROR":
    level = logging.ERROR
elif log_level == "CRITICAL":
    level = logging.CRITICAL
logging.basicConfig(
    level=level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)

# Charge les entrées du fichier de configuration et les
# place dans un objet python nommé 'conf' utilisé dans le reste du projet
with open("qualite_decp/conf.yaml", encoding="utf-8") as f:
    conf_dict = yaml.safe_load(f)
conf = munch.DefaultMunch.fromDict(conf_dict)
