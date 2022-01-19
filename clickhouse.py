#!/usr/bin/nix-shell
#!nix-shell -i python3 -p "pkgs.python3.withPackages(ps: [ps.clickhouse-driver])"
from clickhouse_driver import Client
import itertools
import uuid

uuids = sorted(uuid.UUID(bytes=bytes(x)) for x in itertools.product((0, 1), repeat=16))
conn = Client("localhost")
conn.execute("CREATE TABLE a (u UUID) ENGINE = MergeTree() ORDER BY u")
conn.execute("INSERT INTO a (u) VALUES", [{"u": u} for u in uuids])
rows = list(row[0] for row in conn.execute("SELECT u FROM a ORDER BY u"))
for u in rows:
    print(u)
assert rows == uuids
