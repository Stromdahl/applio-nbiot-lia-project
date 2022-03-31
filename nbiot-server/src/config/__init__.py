from .config import envclass


@envclass
class EnvConfig:
	ADDRESS: str = "127.0.0.1"
	PORT: int = 20001


Config = EnvConfig()
