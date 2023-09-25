# main.py
from db_manager import insert_incident
import db_manager
import threat_detection
import soar_integration
import report_generator
import client_info
import pandas as pd
import matplotlib.pyplot as mp


def dict_to_list(dict_sent):
    result_list = []

    for key in dict_sent.keys():
        result_list.append([key, dict_sent[key]])

    # Total amounts of protocols found
    # print(result_list)
    return result_list


def show_chart(amount_found_dict):
    # data to be plotted
    data = dict_to_list(amount_found_dict)

    # form dataframe from data
    df = pd.DataFrame(data, columns=["Protocol", "Amount"])

    # plot multiple columns such as population and year from dataframe
    df.plot(
        x="Protocol",
        y="Amount",
        kind="barh",
        figsize=(10, 7),
        title="Sniff Result Chart",
    )

    # Window icon and name
    fig = mp.gcf()
    mp.Figure()
    fig_manager = mp.get_current_fig_manager()
    fig_manager.window.wm_iconbitmap("C:\C Program\SentinelFusion\SentinelFusion.ico")
    fig.canvas.manager.set_window_title("Sentinel Fusion")

    # display plot
    mp.show()


def main():
    # Main function to orchestrate other modules

    # Start network monitor
    threat_detection.start_network_monitor()

    # clint_info gets client ip address
    client_ip_address = client_info.get_ip_address()
    # print(client_ip_address)

    show_chart(threat_detection.times_found_dict)

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
