from dataclasses import dataclass
from typing import Protocol

from .google import GoogleCredentials, GoogleServiceProvider, GoogleStorage


class Credentials(Protocol):

    def retrieve_credentials(self):
        ...


class ServiceProvider(Protocol):

    def connect(self, credentials):
        ...

    def get_context(self):
        ...


class Storage(Protocol):

    def initialize(self, context):
        ...


@dataclass
class CloudService:
    auth_provider: Credentials
    service: ServiceProvider
    storage_manager: Storage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")
