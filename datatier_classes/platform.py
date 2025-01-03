from dataclasses import dataclass
from operator import concat

from dataclasses import dataclass
from datetime import datetime

@dataclass
class platform_variables:
        start_time: datetime
        component_name: str
        processing_run_datetime: datetime
        processing_objectname: str
        local_path: str
        local_database_path: str

@dataclass
class platform_settings:
        platform_operation_name: str
        output_settings: bool
        auditing: bool
        datatier_technologies: str
        platform_datatier: str
        referenceapp_guid: str
        organization_guid: str
        auditing_datatier: str
        auditing_platform_datatier: str
