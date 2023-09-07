#updata config.yaml 
from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str 
    local_file: Path 
    unzip_dir: Path

#entity for data_val
@dataclass(frozen=True)
class Datavalidationconfig:
    root_dir: Path 
    status_file: str
    all_required_files: list 