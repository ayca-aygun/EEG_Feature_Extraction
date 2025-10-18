#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def take_onset_times(DRT_onset_time, EEG, samp_DRT, samp_rate_EEG):
    onsetTime = []
    start_index_of_onsetTime = []
    for i in range(0, len(DRT_onset_time)):
        if DRT_onset_time[i] == 1:
            onsetTime.append(i)

    start_index_of_onsetTime.append(onsetTime[0])
    for j in range(1, len(onsetTime)):
        if onsetTime[j] - onsetTime[j-1] > 1:
            start_index_of_onsetTime.append(onsetTime[j])

    start_time_of_onsetTime_ = [round(i / samp_DRT * samp_rate_EEG) for i in start_index_of_onsetTime] # start index of DRT in EEG signal
    end_time_of_onsetTime_ = [i + event_length for i in start_time_of_onsetTime_]
    # Create an array which have values 1 when signal is on (in EEG) -- the length is the same with EEG
    onsetTime_onEEG = np.zeros((len(EEG[0, :]), 1))
    for k in range(0, len(start_time_of_onsetTime_)):
        onsetTime_onEEG[start_time_of_onsetTime_[k]:end_time_of_onsetTime_[k], 0] = 1
    return onsetTime_onEEG, start_time_of_onsetTime_, end_time_of_onsetTime_
    
def take_response_times(DRT_response_time, EEG, samp_DRT, samp_rate_EEG):
    responseTime = []
    start_index_of_responseTime = []
    for i in range(0, len(DRT_response_time)):
        if DRT_response_time[i] == 1:
            responseTime.append(i)

    start_index_of_responseTime.append(responseTime[0])
    for j in range(1, len(responseTime)):
        if responseTime[j] - responseTime[j-1] > 1:
            start_index_of_responseTime.append(responseTime[j])

    start_time_of_responseTime_ = [round(i / samp_DRT * samp_rate_EEG) for i in start_index_of_responseTime] # start index of DRT in EEG signal
    end_time_of_responseTime_ = [round(i + event_length/4) for i in start_time_of_responseTime_]
    # Create an array which have values 1 when signal is on (in EEG) -- the length is the same with EEG
    responseTime_onEEG = np.zeros((len(EEG[0, :]), 1))
    for k in range(0, len(start_time_of_responseTime_)):
        responseTime_onEEG[start_time_of_responseTime_[k]:end_time_of_responseTime_[k], 0] = 1
    return responseTime_onEEG, start_time_of_responseTime_, end_time_of_responseTime_
