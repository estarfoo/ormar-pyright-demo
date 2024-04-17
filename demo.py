import databases
import ormar
from pydantic import Field
from sqlalchemy import MetaData
from typing import Annotated

db = databases.Database("sqlite:///:memory")
md = MetaData()


class Demo(ormar.Model):
    ormar_config = ormar.OrmarConfig(database=db, metadata=md)

    foo: str = ormar.Text(primary_key=True)
    bar: float | None = ormar.Float()


print(repr(Demo(foo="hello", bar=42.)))


class Demo2(ormar.Model):
    ormar_config = ormar.OrmarConfig(database=db, metadata=md)

    foo: Annotated[str, Field(default=ormar.Text(primary_key=True))]
    bar: Annotated[float | None, Field(default=ormar.Float())]


print(repr(Demo2(foo="hello", bar=42.)))


class Demo3(ormar.Model):
    ormar_config = ormar.OrmarConfig(database=db, metadata=md)

    foo: Annotated[str, Field(), ormar.Text(primary_key=True)]
    bar: Annotated[float | None, Field(), ormar.Float()]


print(repr(Demo3(foo="hello", bar=42.)))
