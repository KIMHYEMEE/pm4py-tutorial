import pandas as pd
import pm4py

from path import *

file_name = path_data + '/' +file_csv


def import_csv(file_name):
    # Loading CSV files
    event_log = pd.read_csv(file_name, sep=';')
    n_events = len(event_log)
    n_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(n_events, n_cases))

    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity',
                                       timestamp_key='timestamp') # 데이터의 컬럼 명을 파라미터로 할당
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    return event_log

if __name__ == "__main__":
    event_log = import_csv(file_name)
    event_log.to_csv(path_data+'/test.csv') # store as csv file
    pm4py.write_xes(event_log, path_data+'/test.xes') # store as xes file
