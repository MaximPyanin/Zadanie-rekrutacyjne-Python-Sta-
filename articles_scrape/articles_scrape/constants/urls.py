from enum import Enum
from ..core.bistrolubie_service import BistrolubieService
from ..core.spidersweb_service import SpidersWebService
from ..core.chip_service import ChipService
from ..core.newonce_service import NewonceService


class URLS(Enum):
    BISTROLUBIE = ("https://bistrolubie.pl", lambda: BistrolubieService())
    SPIDERSWEB = ("https://spidersweb.pl", lambda: SpidersWebService())
    CHIP = ("https://www.chip.pl", lambda: ChipService())
    NEWONCE = ("https://newonce.net", lambda: NewonceService())

    @property
    def domain(self):
        return self.value[0]

    @property
    def service(self):
        return self.value[1]()
