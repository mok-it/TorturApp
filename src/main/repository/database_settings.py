from dataclasses import dataclass

@dataclass
class DatabaseSettings:
    drivername: str = 'sqlite'
    host: str = 'localhost'
    port: str = '5432'
    username: str = 'user'
    password: str = 'password'
    database: str = 'torturapp_db'