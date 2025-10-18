#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_feature_matrix(components, blink_part):
    # FEATURE EXTRACTION
    # Calculate the features for different components of ICA

    def mutual_info(x, y, bins):
        c_xy = np.histogram2d(x, y, bins)[0]
        mi = metrics.mutual_info_score(None, None, contingency=c_xy)
        return mi

    def manhattan(a, b):
        return sum(abs(val1-val2) for val1, val2 in zip(a,b))

    # Kurtosis
    for i in range(0, 8):
        summ = len(components[:, i])
        if i == 0:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt1 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 1:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt2 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 2:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt3 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 3:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt4 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 4:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt5 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 5:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt6 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 6:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt7 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2)
        if i == 7:
            mean_x = components[:, i].mean()
            summ_1 = 0; summ_2 = 0
            for j in range(0, summ):
                summ_1 += (components[j, i] - mean_x)**4
                summ_2 += (components[j, i] - mean_x)**2
            kurt8 = ((1 / summ) * summ_1) / (((1 / summ) * summ_2)**2) 

    # Skewness
    skew1 = abs(skew(components[:, 0])); skew2 = abs(skew(components[:, 1])); skew3 = abs(skew(components[:, 2]))
    skew4 = abs(skew(components[:, 3])); skew5 = abs(skew(components[:, 4])); skew6 = abs(skew(components[:, 5]))
    skew7 = abs(skew(components[:, 6])); skew8 = abs(skew(components[:, 7]))

    # Range between min and max
    range1 = np.max(components[:, 0]) - np.min(components[:, 0]); range2 = np.max(components[:, 1]) - np.min(components[:, 1])
    range3 = np.max(components[:, 2]) - np.min(components[:, 2]); range4 = np.max(components[:, 3]) - np.min(components[:, 3])
    range5 = np.max(components[:, 4]) - np.min(components[:, 4]); range6 = np.max(components[:, 5]) - np.min(components[:, 5])
    range7 = np.max(components[:, 6]) - np.min(components[:, 6]); range8 = np.max(components[:, 7]) - np.min(components[:, 7])

    # Max. amplitude
    max1 = max(abs(np.max(components[:, 0])), abs(np.min(components[:, 0]))); max2 = max(abs(np.max(components[:, 1])), abs(np.min(components[:, 1])));
    max3 = max(abs(np.max(components[:, 2])), abs(np.min(components[:, 2]))); max4 = max(abs(np.max(components[:, 3])), abs(np.min(components[:, 3])));
    max5 = max(abs(np.max(components[:, 4])), abs(np.min(components[:, 4]))); max6 = max(abs(np.max(components[:, 5])), abs(np.min(components[:, 5])));
    max7 = max(abs(np.max(components[:, 6])), abs(np.min(components[:, 6]))); max8 = max(abs(np.max(components[:, 7])), abs(np.min(components[:, 7])));

    # Pearson Correlation Coefficient
    corr1 = abs(np.correlate(components[:, 0], blink_part)[0]); corr2 = abs(np.correlate(components[:, 1], blink_part)[0]) 
    corr3 = abs(np.correlate(components[:, 2], blink_part)[0]); corr4 = abs(np.correlate(components[:, 3], blink_part)[0])
    corr5 = abs(np.correlate(components[:, 4], blink_part)[0]); corr6 = abs(np.correlate(components[:, 5], blink_part)[0])
    corr7 = abs(np.correlate(components[:, 6], blink_part)[0]); corr8 = abs(np.correlate(components[:, 7], blink_part)[0])

    # Spearman Correlation Coefficient
    spearcorr1 = abs(spearmanr(components[:, 0], blink_part)[0]); spearcorr2 = abs(spearmanr(components[:, 1], blink_part)[0])
    spearcorr3 = abs(spearmanr(components[:, 2], blink_part)[0]); spearcorr4 = abs(spearmanr(components[:, 3], blink_part)[0])
    spearcorr5 = abs(spearmanr(components[:, 4], blink_part)[0]); spearcorr6 = abs(spearmanr(components[:, 5], blink_part)[0])
    spearcorr7 = abs(spearmanr(components[:, 6], blink_part)[0]); spearcorr8 = abs(spearmanr(components[:, 7], blink_part)[0])
    
    if np.isnan(spearcorr1):
        spearcorr1 = 0.0
    if np.isnan(spearcorr2):
        spearcorr2 = 0.0
    if np.isnan(spearcorr3):
        spearcorr3 = 0.0
    if np.isnan(spearcorr4):
        spearcorr4 = 0.0
    if np.isnan(spearcorr5):
        spearcorr5 = 0.0
    if np.isnan(spearcorr6):
        spearcorr6 = 0.0
    if np.isnan(spearcorr7):
        spearcorr7 = 0.0
    if np.isnan(spearcorr8):
        spearcorr8 = 0.0

    # Kendall Correlation Coefficient
    kendallcorr1 = abs(kendalltau(components[:, 0], blink_part)[0]); kendallcorr2 = abs(kendalltau(components[:, 1], blink_part)[0]);
    kendallcorr3 = abs(kendalltau(components[:, 2], blink_part)[0]); kendallcorr4 = abs(kendalltau(components[:, 3], blink_part)[0]);
    kendallcorr5 = abs(kendalltau(components[:, 4], blink_part)[0]); kendallcorr6 = abs(kendalltau(components[:, 5], blink_part)[0]);
    kendallcorr7 = abs(kendalltau(components[:, 6], blink_part)[0]); kendallcorr8 = abs(kendalltau(components[:, 7], blink_part)[0]);
    if np.isnan(kendallcorr1):
        kendallcorr1 = 0.0
    if np.isnan(kendallcorr2):
        kendallcorr2 = 0.0
    if np.isnan(kendallcorr3):
        kendallcorr3 = 0.0
    if np.isnan(kendallcorr4):
        kendallcorr4 = 0.0
    if np.isnan(kendallcorr5):
        kendallcorr5 = 0.0
    if np.isnan(kendallcorr6):
        kendallcorr6 = 0.0
    if np.isnan(kendallcorr7):
        kendallcorr7 = 0.0
    if np.isnan(kendallcorr8):
        kendallcorr8 = 0.0
        
    # Mutual Information
    mutual_info1 = mutual_info(components[:, 0], blink_part, 2); mutual_info2 = mutual_info(components[:, 1], blink_part, 2); 
    mutual_info3 = mutual_info(components[:, 2], blink_part, 2); mutual_info4 = mutual_info(components[:, 3], blink_part, 2);
    mutual_info5 = mutual_info(components[:, 4], blink_part, 2); mutual_info6 = mutual_info(components[:, 5], blink_part, 2);  
    mutual_info7 = mutual_info(components[:, 6], blink_part, 2); mutual_info8 = mutual_info(components[:, 7], blink_part, 2);

    max_corr = max(corr1, corr2, corr3, corr4, corr5, corr6, corr7, corr8); pole = 1
    for i in range(0, len(components[0, :])):
        if np.correlate(components[:, i], blink_part)[0] == -max_corr:
            pole = -1

    if pole == -1:
        components_pole = -components
    else:
        components_pole = components

    # Euclidean Distance
    euc_dist1 = np.linalg.norm(components_pole[:, 0] - blink_part); euc_dist2 = np.linalg.norm(components_pole[:, 1] - blink_part)
    euc_dist3 = np.linalg.norm(components_pole[:, 2] - blink_part); euc_dist4 = np.linalg.norm(components_pole[:, 3] - blink_part)
    euc_dist5 = np.linalg.norm(components_pole[:, 4] - blink_part); euc_dist6 = np.linalg.norm(components_pole[:, 5] - blink_part)
    euc_dist7 = np.linalg.norm(components_pole[:, 6] - blink_part); euc_dist8 = np.linalg.norm(components_pole[:, 7] - blink_part)

    # Manhattan Distance
    man_dist1 = manhattan(components_pole[:, 0], blink_part); man_dist2 = manhattan(components_pole[:, 1], blink_part)
    man_dist3 = manhattan(components_pole[:, 2], blink_part); man_dist4 = manhattan(components_pole[:, 3], blink_part)
    man_dist5 = manhattan(components_pole[:, 4], blink_part); man_dist6 = manhattan(components_pole[:, 5], blink_part)
    man_dist7 = manhattan(components_pole[:, 6], blink_part); man_dist8 = manhattan(components_pole[:, 7], blink_part)

    data_kurtosis = {'CP1':kurt1, 'CP2':kurt2, 'CP3':kurt3, 'CP4':kurt4, 'CP5':kurt5, 'CP6':kurt6, 'CP7':kurt7, 'CP8':kurt8}
    data_skew = {'CP1':skew1, 'CP2':skew2, 'CP3':skew3, 'CP4':skew4, 'CP5':skew5, 'CP6':skew6, 'CP7':skew7, 'CP8':skew8}
    data_range = {'CP1':range1, 'CP2':range2, 'CP3':range3, 'CP4':range4, 'CP5':range5, 'CP6':range6, 'CP7':range7, 'CP8':range8}
    data_max = {'CP1':max1, 'CP2':max2, 'CP3':max3, 'CP4':max4, 'CP5':max5, 'CP6':max6, 'CP7':max7, 'CP8':max8}
    data_corr = {'CP1':corr1, 'CP2':corr2, 'CP3':corr3, 'CP4':corr4, 'CP5':corr5, 'CP6':corr6, 'CP7':corr7, 'CP8':corr8}
    data_spearcorr = {'CP1':spearcorr1, 'CP2':spearcorr2, 'CP3':spearcorr3, 'CP4':spearcorr4, 'CP5':spearcorr5, 'CP6':spearcorr6, 'CP7':spearcorr7, 'CP8':spearcorr8}
    data_kendallcorr = {'CP1':kendallcorr1, 'CP2':kendallcorr2, 'CP3':kendallcorr3, 'CP4':kendallcorr4, 'CP5':kendallcorr5, 'CP6':kendallcorr6, 'CP7':kendallcorr7, 'CP8':kendallcorr8}
    data_mutualInfo = {'CP1':mutual_info1, 'CP2':mutual_info2, 'CP3':mutual_info3, 'CP4':mutual_info4, 'CP5':mutual_info5, 'CP6':mutual_info6, 'CP7':mutual_info7, 'CP8':mutual_info8}
    data_eucDist = {'CP1':euc_dist1, 'CP2':euc_dist2, 'CP3':euc_dist3, 'CP4':euc_dist4, 'CP5':euc_dist5, 'CP6':euc_dist6, 'CP7':euc_dist7, 'CP8':euc_dist8}
    data_manDist = {'CP1':man_dist1, 'CP2':man_dist2, 'CP3':man_dist3, 'CP4':man_dist4, 'CP5':man_dist5, 'CP6':man_dist6, 'CP7':man_dist7, 'CP8':man_dist8}

    comps_kurtosis = list(data_kurtosis.keys()); values_kurtosis = list(data_kurtosis.values())
    comps_skew = list(data_skew.keys()); values_skew = list(data_skew.values())
    comps_range = list(data_range.keys()); values_range = list(data_range.values())
    comps_max = list(data_max.keys()); values_max = list(data_max.values())
    comps_corr = list(data_corr.keys()); values_corr = list(data_corr.values())
    comps_spearcorr = list(data_spearcorr.keys()); values_spearcorr = list(data_spearcorr.values())
    comps_kendallcorr = list(data_kendallcorr.keys()); values_kendallrcorr = list(data_kendallcorr.values())
    comps_mutualInfo = list(data_mutualInfo.keys()); values_mutualInfo = list(data_mutualInfo.values())
    comps_eucDist = list(data_eucDist.keys()); values_eucDist = list(data_eucDist.values())
    comps_manDist = list(data_manDist.keys()); values_manDist = list(data_manDist.values())

    # Add features to the feature matrix X
    X_current = [[kurt1, skew1, range1, max1, corr1, spearcorr1, kendallcorr1, mutual_info1, euc_dist1, man_dist1],
                 [kurt2, skew2, range2, max2, corr2, spearcorr2, kendallcorr2, mutual_info2, euc_dist2, man_dist2],
                 [kurt3, skew3, range3, max3, corr3, spearcorr3, kendallcorr3, mutual_info3, euc_dist3, man_dist3],
                 [kurt4, skew4, range4, max4, corr4, spearcorr4, kendallcorr4, mutual_info4, euc_dist4, man_dist4],
                 [kurt5, skew5, range5, max5, corr5, spearcorr5, kendallcorr5, mutual_info5, euc_dist5, man_dist5],
                 [kurt6, skew6, range6, max6, corr6, spearcorr6, kendallcorr6, mutual_info6, euc_dist6, man_dist6],
                 [kurt7, skew7, range7, max7, corr7, spearcorr7, kendallcorr7, mutual_info7, euc_dist7, man_dist7],
                 [kurt8, skew8, range8, max8, corr8, spearcorr8, kendallcorr8, mutual_info8, euc_dist8, man_dist8]]
    return X_current

