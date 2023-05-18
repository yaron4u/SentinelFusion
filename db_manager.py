# db_manager.py
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine("sqlite:///incidents.db", echo=True)
meta = MetaData()

incidents = Table(
    "incidents",
    meta,
    Column("id", Integer, primary_key=True),
    Column("status", String),
    Column("details", String),
)
meta.create_all(engine)


def insert_incident(incident_details):
    # Function to insert a new incident into the database

    # Create a connection to the database
    conn = engine.connect()

    # Insert the incident into the database
    conn.execute(
        incidents.insert(),
        [
            {
                "status": incident_details["status"],
                "details": incident_details["details"],
            }
        ],
    )

    # Close the connection to the database
    conn.close()


def get_all_incidents():
    # Function to retrieve all incidents from the database
    try:
        # Create a connection to the database
        conn = engine.connect()

        # Retrieve all incidents from the database
        query = incidents.select()
        result_proxy = conn.execute(query)
        result_set = result_proxy.fetchall()

        # Close the connection to the database
        conn.close()

        # Return the result set
        return result_set
    except Exception as e:
        print("Error while getting incidents: ", str(e))
