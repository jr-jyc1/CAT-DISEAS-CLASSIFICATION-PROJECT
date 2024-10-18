from your_module import ConfigurationManager


# Assuming ConfigurationManager is defined in config_module.py
from config_module import ConfigurationManager
from data_ingestion_module import DataIngestion

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e

