#!/usr/bin/nix-shell
#!nix-shell -i python3 -p "pkgs.python3.withPackages(ps: [ps.cassandra-driver])"
from cassandra.cluster import Cluster
import itertools
import uuid
uuids = sorted(uuid.UUID(bytes=bytes(x)) for x in itertools.product((0, 1), repeat=16))
cluster = Cluster()
conn = cluster.connect()
conn.execute("CREATE TABLE a (u uuid PRIMARY KEY)")
for u in uuids:
    conn.execute("INSERT INTO a (u) VALUES (%s)", (u,))
for row, u in zip(conn.execute("SELECT u FROM a ORDER BY u"), uuids):
    print(row[0], u)
    assert row[0] == u