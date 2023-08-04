
import warnings

# Suppress the warning
warnings.filterwarnings("ignore", category=Warning)



###2. create non-reduced dataset - fill in 1s for none values in the index column (and also average for other demo columns)
from functions.N_fctn_load_excel import load_excel_to_dataframe
daf = load_excel_to_dataframe('ANALYSIS/MAIN_DATA.xlsx')

#####how many missing values there are:

#summary_missing = daf.describe(include='all')
#print(summary_missing)

from functions.Q_fction_get_summary_statistics import get_summary_statistics

summary1 = get_summary_statistics(daf)
print(summary1)
'''
from Q_fction_get_summary_statistics import get_extended_summary_statistics

summary1_ext = get_extended_summary_statistics(daf)
print(summary1_ext)
'''


#...we need to find out the averages first - doing it for pous..., an average of CR

from functions.A_fctn_join_dataframes import join_dataframes

#join_dataframes('summed_areas.xlsx', 'archeo_pocet_pou_na_join.xlsx', 'all_pous_archeo_rate+area_for_average_cration.xlsx', 'pou',)

dataframe_for_average = load_excel_to_dataframe('ANALYSIS/additional_data/for_average_fill_dfs/all_pous_archeo_rate+area_for_average_cration.xlsx')


dataframe_for_average['pou_loc_rate'] = (dataframe_for_average['pocet_lokalit']*100)/dataframe_for_average['vymera']
#print(dataframe_for_average['pou_loc_rate'].mean())

#so the average of localities rate is: 0.021478453745227236


#howeverstill area_municipality a population_density

#lets assume density of cr 135 in 2018... calculated as the # of inhbitants/area of cr...

#area_municipality:
dataframe_for_average_vymera_municipality = load_excel_to_dataframe('ANALYSIS/additional_data/for_average_fill_dfs/pocet_a_rozloha.xlsx')
#print((dataframe_for_average_vymera_municipality['vymera']/100).mean())

#...hence, average area_municipality is 12.603110956375838




#finally we can fill-in the values...:
from functions.P_fctn_fill_missing_values import fill_missing_values

daf_non_reduced = fill_missing_values(daf,{'real_net_monetary_index':1, 
                                           'average_age':42.4734915211329, 
                                           'men_proportion':0.497149745062897, 
                                           '65+_proportion':0.197914581620951, 
                                           'localities_rate': 0.021478453745227236, 
                                           'population_density': 135, 
                                           'area_municipality':12.603110956375838     })
daf_non_reduced = fill_missing_values(daf_non_reduced, {'artifs_rate':0, 'coins_rate':0, 'rate_artifs_dummy':0, 'rate_coins_dummy':0}) 
#print(daf_non_reduced)

#great, but still need to think about the people that did not upload anything -- i divide it again into two datasets, and do the analyses...
from functions.R_fctn_subset_dataframe import subset_dataframe
from functions.N_fctn_subset_non_none import subset_non_none_values
from functions.B_fctn_drop_columns import drop_columns
daf_non_reduced_with_none_being_zero = daf_non_reduced.copy()
daf_non_reduced_with_none_being_zero = drop_columns(daf_non_reduced_with_none_being_zero, ['number_artifs','submitted_number_artifs', 'number_coins', 'submitted_number_coins'],)


daf_non_reduced_with_none_being_zero = subset_dataframe(daf_non_reduced_with_none_being_zero, 'uploaded_at_least_one_artif_or_coin_dummy') #DATASET 1., we have a considerable 7622 rows


#print(daf_non_reduced_with_none_being_zero)

daf_non_reduced_copy_2 = daf_non_reduced.copy()
daf_non_reduced_copy_3 = daf_non_reduced.copy()



#daf_non_reduced_with_artif_none_deleted = subset_non_none_values(daf_non_reduced_copy_2, 'number_artifs') #using 'number_artifs' since artifs rate is imprecise---includes 0s even if one have 0 artifacts sometimess, the same for coins:
daf_non_reduced_with_coin_none_deleted = subset_non_none_values(daf_non_reduced_copy_3, 'number_coins') ####DATASET 2.

from functions.F_fctn_save_df_to_excel import save_dataframe_to_excel

#save_dataframe_to_excel(daf_non_reduced_with_coin_none_deleted, 'df_nonreduced_coins.xlsx')



#save_dataframe_to_excel(daf_non_reduced_with_none_being_zero,'daf_non_reduced_with_none_being_zero.xlsx')
#save_dataframe_to_excel(daf_non_reduced_with_artif_none_deleted,'daf_non_reduced_with_artif_none_deleted.xlsx')
#save_dataframe_to_excel(daf_non_reduced_with_coin_none_deleted,'daf_non_reduced_with_coin_none_deleted.xlsx')
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


####descriptive stats:


#1. ! correlation matrix:
from functions.Q_fctn_create_correlation_matrix import create_correlation_matrix




create_correlation_matrix(daf_non_reduced_with_none_being_zero,['link',                                        
'experience',                                  
'contributions',                               
'comments',                                    
'artifacts',                                   
'coins',                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                 
'coins_rate',                                  
'average_age',   
'men_proportion',                              
'65+_proportion',                              
'detector_expensive_dummy',                    
'area_municipality',                           
'municipality_type',                           
'population_density',                         
'localities_rate'],'Correlation Matrix Non Reduced 7622 Obs.')





#from the correlation matrix we chose 10 variables with the strongest correlation to rates and that are subject to the main hypothesis:

daf_non_reduced_with_none_being_zero = drop_columns(daf_non_reduced_with_none_being_zero, ['area_municipality',                           
'municipality_type',                           
'population_density',
'average_age',                            
'uploaded_at_least_one_artif_or_coin_dummy',   
'men_proportion',                              
'65+_proportion'])

#->the dummies for rate artifs and rate_coins will be used in Logit/Probit only.




#############2. ! summary statistics:
from functions.Q_fction_get_summary_statistics import get_summary_statistics
from functions.Q_fction_get_summary_statistics import get_extended_summary_statistics
summary_non_reduced_1 = get_summary_statistics(daf_non_reduced_with_none_being_zero)
print(summary_non_reduced_1 )

summary_non_reduced_1_ext = get_extended_summary_statistics(daf_non_reduced_with_none_being_zero)
print(summary_non_reduced_1_ext)


from functions.E_fctn_display_unique_values import display_unique_values

#print(display_unique_values(daf_non_reduced_with_none_being_zero, 'municipal_office'))



import numpy as np
df_log = daf_non_reduced_with_none_being_zero[['artifs_rate', 'experience','contributions',               
'comments',                    
'artifacts',                   
'coins',                                      
'real_net_monetary_index',                 
'coins_rate',                    
'localities_rate','rate_artifs_dummy',                           
'rate_coins_dummy', 'link', 'residence_additional_info', 'detector_expensive_dummy']]


df_log['log_experience'] = np.log(df_log['experience'].values + 1)
df_log['log_contributions'] = np.log(df_log['contributions'].values + 1)
df_log['log_comments'] = np.log(df_log['comments'].values + 1)
df_log['log_artifacts'] = np.log(df_log['artifacts'].values + 1)
df_log['log_artifs_rate'] = np.log(df_log['artifs_rate'].values + 1)
df_log['log_coins'] = np.log(df_log['coins'].values + 1)
df_log['log_coins_rate'] = np.log(df_log['coins_rate'].values + 1)
df_log['log_localities_rate'] = np.log(df_log['localities_rate'].values + 1)
#print(df_log)

#******************************************************
#HISTOGRAMS for the ind. variables (non-dummies):
from functions.S_fctn_plot_histograms import create_histograms_with_zeros

create_histograms_with_zeros(daf_non_reduced_with_none_being_zero, [                        
'experience',                  
'contributions',               
'comments',                    
'artifacts',                   
'coins',                                      
'real_net_monetary_index',                    
'localities_rate'])

#histograms for the dependent variable with log transformation:
from functions.S_fctn_plot_histograms import generate_histograms_w_log

generate_histograms_w_log(df_log, ['artifs_rate', 'coins_rate'])
#********************************************************



#********************************************************
#'PLOT INITIAL SCATTER PLOTS
from functions.Q_fctn_plot_scatter import plot_scatter
plot_scatter(df_log, 'artifs_rate', ['experience', 'contributions',
                                     'comments', 'artifacts',
                                     'real_net_monetary_index', 'coins_rate', 'localities_rate'])
#*********************************************************


'''
from U_fctn_plot_residuals import plot_residuals
plot_residuals(df_log, 'artifs_rate', ['experience', 'log_experience', 'contributions', 'log_contributions', 
                                     'comments', 'log_comments', 'artifacts', 'log_artifacts',
                                     'real_net_monetary_index', 'coins_rate', 'localities_rate'])
plot_residuals(df_log, 'log_artifs_rate', ['experience', 'log_experience', 'contributions', 'log_contributions', 
                                     'comments', 'log_comments', 'artifacts', 'log_artifacts',
                                     'real_net_monetary_index', 'coins_rate', 'localities_rate'])
'''





#############################################################################################################################################################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###############################################################################################################################################################################
#OLS_REGRESSION:
#
from functions.V_fct_OLS_REGRESSION import ols_regression


#**THE FINAL ANALYSIS**#
#*******************************************************************************************************************************************************************************************
#deletion of the outliers and then ols base, ols all log, ols_wls_base, ols_wls_log, logit, probit.
#********************************************************************************************************************************************************************************************
from functions.W_fctn_print_top import print_top_observations

print_top_observations(df_log, columns=[ 'experience','contributions',               
'comments',                    
'artifacts'])
'''
Top 5 observations for column 'experience':
      experience  contributions  comments  artifacts
4216      498425             75     16255        331
4217      235138             20      9632        903
4218      209125            119     17572         77
119       207830             25      3085        735
4219      161310             25      4455        219

Top 5 observations for column 'contributions':
      experience  contributions  comments  artifacts
61           604           1489      8964        125
5252          88            502      2554         61
1580          74            395     24463       3332
4911         225            273      4139          1
4682         506            256      4554         36

Top 5 observations for column 'comments':
      experience  contributions  comments  artifacts
1580          74            395     24463       3332
4221       99725              7     18608         83
4218      209125            119     17572         77
4216      498425             75     16255        331
4253       22958             62     12380        491

Top 5 observations for column 'artifacts':
      experience  contributions  comments  artifacts
1580          74            395     24463       3332
4243       30126             46      6471       1324
1664       92662             56      3044        939
6891           0              1       982        916
4217      235138             20      9632        903
'''

df_log_2 = df_log.copy()




df_log_2 = df_log_2[df_log_2['experience'] != 498425]
df_log_2 = df_log_2[df_log_2['contributions'] != 1489]
df_log_2 = df_log_2[df_log_2['comments'] != 24463]
df_log_2 = df_log_2[df_log_2['artifacts'] != 3332] #DELETE THE MOST SIGNIFICANT OUTLIERS

df_log_3 = df_log_2.copy()


df_log_2 = df_log_2[df_log_2['artifs_rate'] != 1]  #DELETE THE ONES

#********************************************************************
#plot scatter plots after log transform and without outliers:
from functions.Q_fctn_plot_scatter import plot_scatter_all
plot_scatter_all(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                      'log_comments', 'log_artifacts', 
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link','detector_expensive_dummy'])
#********************************************************************
#for coins we use the plot_scatter_all only...


#first model, without log transform:
model1 = ols_regression(df_log_2, 'artifs_rate', [ 'experience', 'contributions', 'comments', 'artifacts',
                                      'real_net_monetary_index', 'log_coins_rate', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:            artifs_rate   R-squared:                       0.094
Model:                            OLS   Adj. R-squared:                  0.092
Method:                 Least Squares   F-statistic:                     78.37
Date:                Mon, 10 Jul 2023   Prob (F-statistic):          7.42e-154
Time:                        20:16:52   Log-Likelihood:                 11261.
No. Observations:                7598   AIC:                        -2.250e+04
Df Residuals:                    7587   BIC:                        -2.242e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0094      0.012      0.782      0.434      -0.014       0.033
experience                -1.075e-07   1.14e-07     -0.947      0.344    -3.3e-07    1.15e-07
contributions                 0.0002   5.08e-05      3.744      0.000    9.07e-05       0.000
comments                   1.401e-06   1.19e-06      1.176      0.240   -9.35e-07    3.74e-06
artifacts                  2.676e-05   1.21e-05      2.210      0.027    3.02e-06    5.05e-05
real_net_monetary_index      -0.0032      0.012     -0.259      0.796      -0.027       0.021
log_coins_rate                0.5670      0.022     25.887      0.000       0.524       0.610
localities_rate               0.0363      0.050      0.722      0.471      -0.062       0.135
link                          0.0131      0.004      3.259      0.001       0.005       0.021
residence_additional_info     0.0136      0.006      2.191      0.028       0.001       0.026
detector_expensive_dummy      0.0113      0.005      2.229      0.026       0.001       0.021
==============================================================================
Omnibus:                     9660.827   Durbin-Watson:                   1.986
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1505715.416
Skew:                           7.092   Prob(JB):                         0.00
Kurtosis:                      70.490   Cond. No.                     5.51e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 5.51e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

Breusch-Pagan Test for Heteroskedasticity:
(480.41765268439224, 6.730367651987109e-97, 51.210208088300746, 3.452773252733972e-100)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  360.295661
1                  experience    1.512822
2               contributions    1.231935
3                    comments    1.842023
4                   artifacts    1.440940
5     real_net_monetary_index    1.070975
6              log_coins_rate    1.009974
7             localities_rate    1.069959
8                        link    1.026483
9   residence_additional_info    1.018931
10   detector_expensive_dummy    1.015542

'''




model2 = ols_regression(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])





'''
model2_without_coins = ols_regression(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
#***********************************************************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************************************************************

'''
#MODEL2:
None
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:        log_artifs_rate   R-squared:                       0.103
Model:                            OLS   Adj. R-squared:                  0.102
Method:                 Least Squares   F-statistic:                     86.96
Date:                Mon, 10 Jul 2023   Prob (F-statistic):          1.63e-170
Time:                        11:53:17   Log-Likelihood:                 12770.
No. Observations:                7598   AIC:                        -2.552e+04
Df Residuals:                    7587   BIC:                        -2.544e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0020      0.010      0.200      0.841      -0.017       0.021
log_experience                0.0014      0.000      4.984      0.000       0.001       0.002
log_contributions             0.0018      0.001      2.395      0.017       0.000       0.003
log_comments              -8.053e-05      0.000     -0.165      0.869      -0.001       0.001
log_artifacts                 0.0018      0.001      3.143      0.002       0.001       0.003
real_net_monetary_index      -0.0028      0.010     -0.275      0.783      -0.022       0.017
log_coins_rate                0.4447      0.018     24.720      0.000       0.409       0.480
localities_rate               0.0335      0.041      0.812      0.417      -0.047       0.114
link                          0.0106      0.003      3.238      0.001       0.004       0.017
residence_additional_info     0.0091      0.005      1.772      0.076      -0.001       0.019
detector_expensive_dummy      0.0095      0.004      2.276      0.023       0.001       0.018
==============================================================================
Omnibus:                     9175.324   Durbin-Watson:                   2.002
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1086109.874
Skew:                           6.555   Prob(JB):                         0.00
Kurtosis:                      60.086   Cond. No.                         420.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Breusch-Pagan Test for Heteroskedasticity:
(435.0857222158272, 3.1646522124667595e-87, 46.084529933431476, 6.704904881411239e-90)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  363.019066
1              log_experience    2.154567
2           log_contributions    1.551537
3                log_comments    3.160793
4               log_artifacts    2.373210
5     real_net_monetary_index    1.071449
6              log_coins_rate    1.013526
7             localities_rate    1.070111
8                        link    1.016569
9   residence_additional_info    1.031733
10   detector_expensive_dummy    1.012028

Hausman Test for Endogeneity:
None
'''








#->>>>>>DUE TO HETEROSKEDASTICITY (B-P TEST) WE DO HETEROSKEDASTICITY ROBUST REGRESSION, I.E. WLS:
from functions.V_fctn_OLS_ROBUST import ols_regression_robust
'''
model4_ROBUST = ols_regression_robust(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''


model2_ROBUST = ols_regression_robust(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:        log_artifs_rate   R-squared:                       0.103
Model:                            OLS   Adj. R-squared:                  0.102
Method:                 Least Squares   F-statistic:                     21.00
Date:                Mon, 10 Jul 2023   Prob (F-statistic):           4.88e-39
Time:                        20:15:56   Log-Likelihood:                 12770.
No. Observations:                7598   AIC:                        -2.552e+04
Df Residuals:                    7587   BIC:                        -2.544e+04
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0020      0.009      0.221      0.825      -0.016       0.019
log_experience                0.0014      0.000      5.243      0.000       0.001       0.002
log_contributions             0.0018      0.001      1.846      0.065      -0.000       0.004
log_comments              -8.053e-05      0.001     -0.158      0.875      -0.001       0.001
log_artifacts                 0.0018      0.001      3.566      0.000       0.001       0.003
real_net_monetary_index      -0.0028      0.009     -0.304      0.761      -0.020       0.015
log_coins_rate                0.4447      0.097      4.568      0.000       0.254       0.636
localities_rate               0.0335      0.035      0.954      0.340      -0.035       0.102
link                          0.0106      0.005      2.309      0.021       0.002       0.020
residence_additional_info     0.0091      0.008      1.139      0.255      -0.007       0.025
detector_expensive_dummy      0.0095      0.006      1.570      0.116      -0.002       0.021
==============================================================================
Omnibus:                     9175.324   Durbin-Watson:                   2.002
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1086109.874
Skew:                           6.555   Prob(JB):                         0.00
Kurtosis:                      60.086   Cond. No.                         420.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(435.0857222158272, 3.1646522124667595e-87, 46.084529933431476, 6.704904881411239e-90)

White's Test for Heteroskedasticity:
(604.3849327083649, 6.159726646741204e-90, 10.502760718951535, 2.242970257489869e-94)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  363.019066
1              log_experience    2.154567
2           log_contributions    1.551537
3                log_comments    3.160793
4               log_artifacts    2.373210
5     real_net_monetary_index    1.071449
6              log_coins_rate    1.013526
7             localities_rate    1.070111
8                        link    1.016569
9   residence_additional_info    1.031733
10   detector_expensive_dummy    1.012028
'''


#->>>>>>>>>now WLS:
from functions.V_fctn_OLS_WLS import ols_regression_wls
'''
model1_WLS = ols_regression_wls(df_log_2, 'artifs_rate', [ 'experience', 'contributions', 'comments', 'artifacts',
                                      'real_net_monetary_index', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])



model4_WLS = ols_regression_wls(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''
model2_WLS = ols_regression_wls(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])


'''
Regression Summary:
                            WLS Regression Results
==============================================================================
Dep. Variable:        log_artifs_rate   R-squared:                       0.966
Model:                            WLS   Adj. R-squared:                  0.966
Method:                 Least Squares   F-statistic:                 2.180e+04
Date:                Mon, 10 Jul 2023   Prob (F-statistic):               0.00
Time:                        20:45:57   Log-Likelihood:                 30996.
No. Observations:                7598   AIC:                        -6.197e+04
Df Residuals:                    7587   BIC:                        -6.189e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0005   3.49e-05     15.328      0.000       0.000       0.001
log_experience                0.0019   1.75e-05    108.321      0.000       0.002       0.002
log_contributions             0.0025   4.47e-05     56.365      0.000       0.002       0.003
log_comments              -2.192e-05   3.78e-06     -5.796      0.000   -2.93e-05   -1.45e-05
log_artifacts                 0.0005   2.48e-05     19.987      0.000       0.000       0.001
real_net_monetary_index      -0.0008   4.39e-05    -17.099      0.000      -0.001      -0.001
log_coins_rate                0.4685      0.013     35.194      0.000       0.442       0.495
localities_rate               0.0093      0.000     19.501      0.000       0.008       0.010
link                          0.0002      0.001      0.172      0.863      -0.002       0.002
residence_additional_info     0.0022      0.001      1.785      0.074      -0.000       0.005
detector_expensive_dummy     -0.0019      0.001     -1.680      0.093      -0.004       0.000
==============================================================================
Omnibus:                     7451.871   Durbin-Watson:                   0.949
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1882758.407
Skew:                           4.190   Prob(JB):                         0.00
Kurtosis:                      79.661   Cond. No.                     2.08e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.08e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  363.019066
1              log_experience    2.154567
2           log_contributions    1.551537
3                log_comments    3.160793
4               log_artifacts    2.373210
5     real_net_monetary_index    1.071449
6              log_coins_rate    1.013526
7             localities_rate    1.070111
8                        link    1.016569
9   residence_additional_info    1.031733
10   detector_expensive_dummy    1.012028
#->>>>>>>>>>>>>>>>>>>This model has relatively large R2 0.966. This together with many variables significant  at 5% sign.level might...
# indicate over-fitting or some other issue. 
'''





#now LPM:
model2_LPM = ols_regression_robust(df_log_3, 'rate_artifs_dummy', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   R-squared:                       0.183
Model:                            OLS   Adj. R-squared:                  0.182
Method:                 Least Squares   F-statistic:                     65.29
Date:                Sat, 15 Jul 2023   Prob (F-statistic):          3.35e-128
Time:                        16:13:12   Log-Likelihood:                 170.96
No. Observations:                7619   AIC:                            -319.9
Df Residuals:                    7608   BIC:                            -243.6
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0570      0.048     -1.199      0.231      -0.150       0.036
log_experience                0.0109      0.002      6.848      0.000       0.008       0.014
log_contributions             0.0260      0.006      4.385      0.000       0.014       0.038
log_comments                  0.0055      0.003      1.975      0.048    4.21e-05       0.011
log_artifacts                 0.0416      0.003     13.144      0.000       0.035       0.048
real_net_monetary_index      -0.0080      0.048     -0.166      0.868      -0.102       0.086
log_coins_rate                1.4722      0.233      6.321      0.000       1.016       1.929
localities_rate               0.3305      0.198      1.673      0.094      -0.057       0.718
link                          0.0195      0.022      0.869      0.385      -0.024       0.063
residence_additional_info     0.0728      0.040      1.838      0.066      -0.005       0.150
detector_expensive_dummy      0.0346      0.027      1.284      0.199      -0.018       0.087
==============================================================================
Omnibus:                     3975.979   Durbin-Watson:                   1.996
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            24089.944
Skew:                           2.521   Prob(JB):                         0.00
Kurtosis:                      10.104   Cond. No.                         419.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(1083.6204123162174, 1.7914589864155838e-226, 126.14698176733783, 1.2789816542872652e-244)

White's Test for Heteroskedasticity:
(1252.6598048269063, 3.09096365909923e-221, 23.979689740964012, 5.354299313994446e-244)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  362.616715
1              log_experience    2.152850
2           log_contributions    1.557501
3                log_comments    3.161273
4               log_artifacts    2.369945
5     real_net_monetary_index    1.070944
6              log_coins_rate    1.014035
7             localities_rate    1.069685
8                        link    1.018130
9   residence_additional_info    1.033605
10   detector_expensive_dummy    1.011361
'''


#>>>>>>>>>>now LOGIT:
from functions.V_fctn_LOGIT import logit_regression_roc_wald
model2_LOGIT = logit_regression_roc_wald(df_log_3, dependent_var='rate_artifs_dummy', independent_vars=['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'], 
                                     pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                     ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                     hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])




'''
Optimization terminated successfully.
         Current function value: 0.194088
         Iterations 8
Logit Regression Summary:
                           Logit Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   No. Observations:                 7619
Model:                          Logit   Df Residuals:                     7608
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.2646
Time:                        06:43:57   Log-Likelihood:                -1478.8
converged:                       True   LL-Null:                       -2010.9
Covariance Type:            nonrobust   LLR p-value:                2.700e-222
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -4.9257      1.008     -4.885      0.000      -6.902      -2.950
log_experience                0.1260      0.026      4.895      0.000       0.076       0.176
log_contributions             0.0670      0.052      1.286      0.198      -0.035       0.169
log_comments                  0.1602      0.044      3.605      0.000       0.073       0.247
log_artifacts                 0.5192      0.052     10.034      0.000       0.418       0.621
real_net_monetary_index      -0.2855      1.019     -0.280      0.779      -2.283       1.712
log_coins_rate               10.6671      1.313      8.123      0.000       8.093      13.241
localities_rate               7.7846      4.093      1.902      0.057      -0.238      15.808
link                          0.0248      0.245      0.101      0.919      -0.456       0.505
residence_additional_info     0.8341      0.327      2.551      0.011       0.193       1.475
detector_expensive_dummy      0.6023      0.310      1.944      0.052      -0.005       1.210
=============================================================================================

Area Under the Curve (AUC): 0.8577823182592699
Optimization terminated successfully.
'''

#now PROBIT:
from functions.V_fctn_PROBIT import probit_regression_roc_wald


model2_PROBIT = probit_regression_roc_wald(df_log_3, dependent_var='rate_artifs_dummy', independent_vars=['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'], 
                                      pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                      ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                      hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])
'''
model3_PROBIT = probit_regression_roc(df_log_3, 'rate_artifs_dummy', [ 'experience', 'contributions', 'comments', 'artifacts',
                                      'real_net_monetary_index', 'log_coins_rate', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
'''
Probit Regression Summary:
                          Probit Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   No. Observations:                 7619
Model:                         Probit   Df Residuals:                     7608
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.2656
Time:                        06:34:55   Log-Likelihood:                -1476.8
converged:                       True   LL-Null:                       -2010.9
Covariance Type:            nonrobust   LLR p-value:                3.720e-223
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -2.6005      0.503     -5.168      0.000      -3.587      -1.614
log_experience                0.0686      0.013      5.215      0.000       0.043       0.094
log_contributions             0.0514      0.029      1.782      0.075      -0.005       0.108
log_comments                  0.0689      0.023      3.019      0.003       0.024       0.114
log_artifacts                 0.2762      0.027     10.304      0.000       0.224       0.329
real_net_monetary_index      -0.1665      0.510     -0.327      0.744      -1.165       0.832
log_coins_rate                5.2977      0.554      9.561      0.000       4.212       6.384
localities_rate               3.7713      2.063      1.828      0.068      -0.273       7.815
link                          0.0225      0.132      0.171      0.864      -0.236       0.281
residence_additional_info     0.4576      0.182      2.518      0.012       0.101       0.814
detector_expensive_dummy      0.2999      0.167      1.795      0.073      -0.028       0.627
=============================================================================================

Area Under the Curve (AUC): 0.8579348683846776

'''

