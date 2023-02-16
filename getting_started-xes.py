import pandas as pd
import pm4py

from path import *

file_name = path_data + '/' +file_xes


def import_xes(file_name):
    # Loading XES files
    event_log = pm4py.read_xes(file_name)
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    return event_log    

if __name__ == "__main__":
    event_log = import_xes(file_name)
    df = pm4py.convert_to_dataframe(event_log)
    df.to_csv(path_data+'/test.csv') # store as csv file
    pm4py.write_xes(event_log, path_data+'/test.xes') # store as xes file