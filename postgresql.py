#!/usr/bin/nix-shell
#!nix-shell -i python3 -p "pkgs.python3.withPackages(ps: [ps.sqlalchemy ps.pg8000])"
import itertools
import sys
from sqlalchemy import create_engine, text, Table, Column, MetaData, insert, select
from sqlalchemy.dialects import postgresql
import uuid

uuids = sorted(uuid.UUID(bytes=bytes(x)) for x in itertools.product((0, 1), repeat=16))
engine = create_engine(
    "postgresql+pg8000://postgres:postgres@localhost/postgres", echo=True
)
metadata = MetaData()
table = Table(
    "a", metadata, Column("u", postgresql.UUID(as_uuid=True), primary_key=True)
)
metadata.create_all(engine)
with engine.connect() as conn:
    conn.execute(
        insert(table),
        [{"u": u} for u in uuids],
    )
    for row, u in zip(conn.execute(select(table.c.u).order_by(table.c.u)).all(), uuids):
        print(row[0], u)
        assert row[0] == u
