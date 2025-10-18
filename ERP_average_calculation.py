#!/usr/bin/env python
# coding: utf-8

# In[ ]:
    
def calculate_mean_ERP(EEG_signal, range_constr, no_latency_blinking_line, start_time_of_onsetTime_, end_time_of_onsetTime_):
    all_smoothed_data = np.zeros((3000, len(range_constr)))
    mean_count = 0
    print(range_constr)
    for n in range_constr:
        starting_point = int(start_time_of_onsetTime_[n])
        ending_point_of_event = int(end_time_of_onsetTime_[n])
        ending_point = ending_point_of_event + event_length
        print(starting_point, ending_point)
        y_ = EEG_signal[channel_to_be_checked, starting_point:ending_point]
        x = np.linspace(0, len(y_)/samp_rate_EEG, len(y_))

        get_ipython().run_line_magic('run', "-i 'calculate_ICA.py'")
        blink_part = no_latency_blinking_line[starting_point:ending_point] # (**)
        components, EEG_tr, ica = apply_ICA(EEG_signal, starting_point, ending_point)
    #     visualize_ICA(components, blink_part)

        get_ipython().run_line_magic('run', "-i 'calculate_fm.py'")
        print(len(blink_part), len(components[:, 0]))
        X_current = calculate_feature_matrix(components, blink_part)

        # Predict the label of the components by using the saved model
        preds = rf_classifier.predict(X_current)
        for i in range(0, len(preds)):
            if preds[i] == '1.0':
                pred_comp = i
                components[:, pred_comp] = 0
        restored = ica.inverse_transform(components)
        y_rest = restored[:, channel_to_be_checked-1]

        get_ipython().run_line_magic('run', "-i 'apply_Kalman.py'")
        smoother = apply_Kalman_Smoother(y_rest)
        print(n, len(smoother.smooth_data[0]))
    #     visualize_Smoothed_Signal(smoother=smoother, no_latency_blinking_line=no_latency_blinking_line1, starting_point=starting_point, ending_point=ending_point)

        all_smoothed_data[:, mean_count] = smoother.smooth_data[0]
        mean_count += 1

    # Calculate the mean
    mean_smoothed_data = np.zeros((len(smoother.smooth_data[0]), 1))
    for i in range(0, len(mean_smoothed_data[:, 0])):
        mean_smoothed_data[i, 0] = np.mean(all_smoothed_data[i, :])

    return mean_smoothed_data, all_smoothed_data

def visualize_mean_ERP(mean_smoothed_data_all, mean_smoothed_data_with, mean_smoothed_data_without, xlim_start, xlim_end, ylim_start, ylim_end): 
    plt.figure(figsize=(10, 6))
    plt.plot(mean_smoothed_data_all[:, 0], linewidth=2, color='black', label='Mean ERP of all events')
    plt.plot(mean_smoothed_data_with[:, 0], linewidth=2, color='olive', label='Mean ERP with responses')
    plt.plot(mean_smoothed_data_without[:, 0], linewidth=2, color='navy', label='Mean ERP without responses')
    plt.title("ERP for DRT Events - Subject 139", fontsize=18);
    plt.legend(loc="lower left")
    plt.xlabel('Time [seconds]', fontsize=14)
    plt.xlim([xlim_start, xlim_end])
    plt.ylim([ylim_start, ylim_end])
    plt.figure(figsize=(10, 5))
    plt.show()