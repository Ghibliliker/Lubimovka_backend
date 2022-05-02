import logging
from pathlib import Path
from typing import Optional

import yadisk
from django.conf import settings
from yadisk.exceptions import YaDiskError

logger = logging.getLogger("django")


def yandex_disk_export(instance) -> Optional[bool]:
    try:
        yndx = yadisk.YaDisk(token=settings.YNDX_DISK_TOKEN)
        _, year, name = Path(str(instance.file)).parts
        to_dir = f"{year}/{name}"
        from_dir = (settings.MEDIA_ROOT / instance.file.name).as_posix()

        if not yndx.is_dir(year):
            yndx.mkdir(year)
        yndx.upload(from_dir, to_dir)

        if yndx.exists(to_dir):
            download_link = yndx.get_download_link(to_dir)
            return download_link
    except (ValueError, YaDiskError) as error:
        msg = f"Не удалось загрузить пьесу {instance.title} от {instance.email} на Яндекс диск."
        logger.critical(msg, error, exc_info=True)
