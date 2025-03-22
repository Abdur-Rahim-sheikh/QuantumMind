import base64
from typing import Optional

from ai_shortener.domain.models import Url
from ai_shortener.domain.repository import UrlShortenerRepository
from public.models import Url as DBUrl


class DefaultUrlShortenerRepository(UrlShortenerRepository):
    def shorten(self, long_url: str, title: str = None, description: str = None, img: base64 = None) -> str:
        if DBUrl.objects.filter(long_url=long_url).exists():
            return DBUrl.objects.get(pid=long_url).short_url

        long_url = DBUrl.objects.create(
            title=title,
            description=description,
            img_base64=img,
            long_url=long_url,
        )

        return long_url.short_url

    def get(self, pid: int) -> Optional[Url]:
        try:
            url = DBUrl.objects.get(pid=pid)
        except DBUrl.DoesNotExist:
            return None

        return Url(
            title=url.title,
            description=url.description,
            image=url.img_base64,
            long_url=url.long_url,
            short_url=url.short_url,
            ai_url=url.ai_url,
        )

    def get_all(self) -> list[Url]:
        urls = DBUrl.objects.all()
        return [
            Url(
                title=url.title,
                description=url.description,
                image=url.img_base64,
                long_url=url.long_url,
                short_url=url.short_url,
                ai_url=url.ai_url,
            )
            for url in urls
        ]

    def update(self, pid: int, title: str = None, description: str = None, img: base64 = None) -> None:
        try:
            url = DBUrl.objects.get(pid=pid)
        except DBUrl.DoesNotExist:
            return

        url.title = title
        url.description = description
        url.img_base64 = img
        url.save()

    def delete(self, pid: int) -> bool:
        try:
            url = DBUrl.objects.get(pid=pid)
        except DBUrl.DoesNotExist:
            return False

        url.delete()
        return True
