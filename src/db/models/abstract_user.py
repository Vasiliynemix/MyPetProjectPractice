from dataclasses import dataclass


@dataclass
class AbstractUser:
    telegram_id: int = 123
    username: str = 'username'
    is_admin: bool = False
    is_super_admin: bool = False
