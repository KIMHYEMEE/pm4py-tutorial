# pm4py-tutorial

본 글은 [PY4PM의 Documentation](https://pm4py.fit.fraunhofer.de/static/assets/api/2.5.0/index.html#)을 참고하여 작성 및 인용되었습니다.

## Process
프로세스 마이닝에서 `프로세스`의 정의는 다음과 같다.
> A process represents a collection of activities that we execute to achieve a certain goal
- 프로세스는 어떤 목표를 달성하기 위해 수행하는 액티비티의 모음이다.

## Data for py4pm
- file type: csv and xes(eXtensible Event Strem)
- component
  - the case for which the event occured (case ID)
  - activity
  - timestamp
  - resource executing the activity
  - etc

## 이벤트로그 읽기
### csv 읽기
- `format_dataframe`: dataframe을 pm4py에서 읽을 수 있는 형태로 설정. 이 때, case id, activity, timestamp 등의 요소를 컬럼명을 활용하여 할당하여야 함. 할당 시 해당 컬럼명은 pm4py에서 설정된 컬럼명으로 변경됨. (예, case:concept:name, concept:name, time:timestamp) 
  - 2023-02-16: 3.0 버전에서는 사용하지 않는다는 경고문 발생. 현재 관련 자료 확인 불가

1. pandas를 활용하여 dataframe으로 읽기 (df를 처리하는 방식이므로, xlsx 파일도 가능할 것으로 추정 ~ 확인 필요)
2. `format_dataframe`으로 dataframe을 이벤트로그 형태로 변환

### xes 읽기
- `read_xes`: xes파일을 읽는 함수. xes는 이벤트를 표현하는 형식의 파일이므로, 별도의 파라미터 등을 통한 구성요소 설정 작업을 필요로하지 않음

1. `read_xes`으로 xes파일 읽기

## 이벤트로그 저장하기
### csv로 저장하기
- `convert_to_dataframe`: 이벤트로그를 dataframe으로 변환

1. [선택] xes 파일로 만들어진 이벤트로그인 경우, `convert_to_dataframe`을 활용하여 dataframe 형태로 전환
   - 해당작업을 수행하지않고 이벤트로그를 바로 저장할 경우, 문제없이 저장됨
2. 일반 데이터프레임을 저장하는 것과 같이 `df.to_csv`를 활용하여 파일 저장

### xes로 저장하기
- `write_xes`: dataframe 또는 xes 에서 얻어진 이벤트로그를 xes로 저장

1. `write_xes`를 활용하여 이벤트로그를 xes로 저장

## 이벤트로그 현황 확인
- `get_start_activities` (`get_end_activities`): 이벤트로그 내 각 trace의 시작(끝)에 발생하는 activity를 빈도수와 함께 표현

## 이벤트로그 필터

- **filter_start_activities(log, activities, retrain=True)**: 
  ```
  filtered = pm4py.filter_start_activities(event_log, {'register request'})
  ```
  ```
  filtered = pm4py.filter_start_activities(event_log, {'register request TYPO!'})
  ```
- **filter_end_activities(log, activities, retrain=True)**: 
  ```
  filtered = pm4py.filter_end_activities(event_log, 'pay compensation')
  ```
- **filter_event_attribute_values(log, attribute_key, values, level='case', retain=True)**: 
  ```
  filtered = pm4py.filter_event_attribute_values(log, 'org:resource',{'Pete','Mike'})
  ```
  ```
  filtered = pm4py.filter_event_attribute_values(log, 'org:resource',{'Pete','Mike'}, level='event')
  ```
- **filter_trace_attribute_values(log, attribute_key, values, retain=True)**: 
  ```
  filtered = pm4py.filter_trace_attribute_values(log, 'org:resource',{'3','4'})
  ```
  ```
  filtered = pm4py.filter_trace_attribute_values(log, 'org:resource',{'3','4'}, retain=False)
  ```
- **filter_variants(log, variants, retrain=True)**: 
  ``` 
  filtered = pm4py.filter_variants(log,[['register request','check ticket','examine casually','decide','pay compensation']])
  ```
  ``` 
  filtered = pm4py.filter_variants(log,[['register request','check ticket','examine casually','decide','reject request']])
  ```
- **filter_directly_follows_relation(log, relations, retrain=True)**: 
  ```
  filtered = pm4py.filter_directly_follows_relation(log, [('check ticket','examin casually')])
  ```
- **filter_eventually_follows_relation(log, relations, retrain=True)**: 
  ```
  filtered = pm4py.filter_eventually_follows_relation(log,[('examine casually','reject request')])
  ```
- **filter_time_range(log, dt1, dt2, mode='events')**: 
  ```
  filtered = pm4py.filter_time_range(evet_log, dt.datetime(2010,12,30), dt.datetime(2010,12,31), mode='events')
  ```