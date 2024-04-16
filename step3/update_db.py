import os.path

import psycopg2

table_names = ['maps', 'users', 'capitals', 'regions', 'accesses', 'route_types', 'routes', 'places', 'trip_statuses', 'trips', 'comments', 'photos', 'trip_routes', 'route_places', 'participation', 'visited', 'friends']


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="host",
        database="database",
        user="user",
        password="password",
        port=port
    )
    with conn.cursor() as curs:
        curs.execute(open(f"./sql2/triggers.sql", "r").read())
    conn.commit()

    for name in table_names:
        with conn.cursor() as curs:
            print(f"Current table: {name}")
            curs.execute(f"DROP TABLE IF EXISTS {name} CASCADE;")
            curs.execute(open(f"./sql/{name}.schema.sql", "r").read())


            if os.path.exists(f"./sql/{name}.data.sql"):
                curs.execute(open(f"./sql/{name}.data.sql", "r").read())
                conn.commit()