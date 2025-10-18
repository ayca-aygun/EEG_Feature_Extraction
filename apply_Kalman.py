#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def apply_Kalman_Smoother(y_rest):
    # Define the smoother from tsmoothie
    # smoother = KalmanSmoother(component='level_trend', component_noise={'level':0.00001, 'trend':0.00025})
    smoother = KalmanSmoother(component='level_trend', component_noise={'level':0.00001, 'trend':0.00005})
    smoother.smooth(y_rest)
    return smoother
    
def visualize_Smoothed_Signal(**kwargs):
    parameter_list = {}; count = 0
    for k,v in kwargs.items():
        parameter_list[k] = v
        if k == "x_lim_start":
            count += 1
    smoother = parameter_list["smoother"]
    no_latency_blinking_line = parameter_list["no_latency_blinking_line"]
    starting_point = parameter_list["starting_point"]
    ending_point = parameter_list["ending_point"]
    # fix_counts = parameter_list["fix_counts"]
    fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=False, sharey=False, gridspec_kw={'height_ratios': [4, 1]})
    fig.subplots_adjust(hspace = .25, wspace = .1)
    #plt.suptitle("BLINK ARTIFACT REMOVAL (CP1)", fontsize='16')
    axs = axs.ravel()

    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel('Time [seconds]', fontsize=14, labelpad=15)
    axs[0].plot(y_[0:ending_point-starting_point-1], linewidth=2, color='olive', label='Raw EEG')
    axs[0].plot(smoother.smooth_data[0, 0:ending_point-starting_point-1], color='navy', label='Cleaned EEG')
    axs[0].set_title("Raw EEG vs Clean EEG", fontsize=18)
    # axs[1].plot(fix_counts)
    # axs[1].set_title("Fixation Count (per sec)", fontsize=18)
    axs[1].plot(no_latency_blinking_line[starting_point:ending_point], color='brown')
    axs[1].set_title("Blink Info", fontsize=18)
    axs[0].legend(); axs[1].legend();
    if count > 0:
        x_lim_start = parameter_list["x_lim_start"]
        x_lim_end = parameter_list["x_lim_end"]
        axs[0].set_xlim(x_lim_start, x_lim_end)
        axs[1].set_xlim(x_lim_start, x_lim_end)
    axs[1].set_ylim(0, 10)
    plt.xlabel('Time (ms)')

