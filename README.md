# my-uuid-bullshit

i'm back on my bullshit

summer 2021 at @getsentry i discovered that clickhouse orders uuids in a non-obvious way

i decided to bother a bunch of databases to see if anything else does

## results so far

everything is tested in github actions, green means ordering is what i expect, red is not

[![ClickHouse](https://github.com/Michcioperz/my-uuid-bullshit/actions/workflows/clickhouse.yaml/badge.svg?branch=main)](https://github.com/Michcioperz/my-uuid-bullshit/actions/workflows/clickhouse.yaml)
[![PostgreSQL](https://github.com/Michcioperz/my-uuid-bullshit/actions/workflows/postgresql.yaml/badge.svg?branch=main)](https://github.com/Michcioperz/my-uuid-bullshit/actions/workflows/postgresql.yaml)