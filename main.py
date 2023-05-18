# main.py
from db_manager import insert_incident
import db_manager
import threat_detection
import soar_integration
import report_generator


def main():
    # Main function to orchestrate other modules

    # Start network monitor
    threat_detection.start_network_monitor()

    # Get all incidents from the database
    print("Getting all incidents...")
    incidents = db_manager.get_all_incidents()
    # test
    incident_details = {"status": "open", "details": "example.com"}
    insert_incident(incident_details)
    print(incidents)

    # Get threat intelligence for each incident
    # limit for 1 incidents and add threat intelligence to the incident, stop the loop
    for incident in incidents:
        threat_intelligence = soar_integration.get_threat_intelligence(
            incident["details"]
        )
        incident["threat_intelligence"] = threat_intelligence
        break

    # Generate PDF report in the current directory
    print("Generating PDF report...")
    report_generator.generate_pdf_report(incident_details)


if __name__ == "__main__":
    main()
