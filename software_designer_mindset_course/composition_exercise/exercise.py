from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth
from typing import Protocol


class AbstractCloudProvider(Protocol):
    def __init__(self, region, http_auth, secure):
        self.region: str = region
        self.http_auth = http_auth
        self.secure: bool = secure

    def filter_by_query(self, bucket, query, max):
        ...


class ACCloud:
    def __init__(self, bucket_name: str, region: str, provider: AbstractCloudProvider) -> None:
        self.provider = provider
        self.bucket_name = bucket_name

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.provider.filter_by_query(
            bucket=self.bucket_name, query=query, max=max_result
        )
        return response["result"]["data"][0]


class VideoStorage:
    def __init__(self) -> None:
        self.ac_cloud = ACCloud("video-backup.arjancodes.com", "eu-west-1c")

    def find_files(self, query: str, max_result: int) -> list[str]:
        return self.ac_cloud.find_files(query, max_result)
