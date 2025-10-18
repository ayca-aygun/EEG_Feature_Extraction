#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def apply_ICA(EEG_signal, starting_point, ending_point):
    # Apply FastICA --> To change EEG1 and EEG2, change (*) and (**)
    ica = FastICA(n_components=8, random_state=0, tol=0.05, max_iter=2000)
    EEG_tr = EEG_signal[1:9, starting_point:ending_point].T # (*)
    components = ica.fit_transform(EEG_tr)
    return components, EEG_tr, ica
    
def visualize_ICA(components, blink_part):
    # Visualize the components for labeling
    fig, axs = plt.subplots(9, 1, figsize=(12, 14), sharex=True, gridspec_kw={'height_ratios': [4, 4, 4, 4, 4, 4, 4, 4, 2]})
    fig.subplots_adjust(hspace = .1, wspace=0)
    axs = axs.ravel()

    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel('Time [samples]', fontsize=14, labelpad=15)

    for i in range(9):
        if i < 8:
            axs[i].plot(components[:, i], color='black', label='Component '+ str(i+1))
        else:
            axs[i].plot(blink_part, color='brown', label='Blink Info')

    axs[0].legend(); axs[1].legend(); axs[2].legend(); axs[3].legend(); 
    axs[4].legend(); axs[5].legend(); axs[6].legend(); axs[7].legend(); 

