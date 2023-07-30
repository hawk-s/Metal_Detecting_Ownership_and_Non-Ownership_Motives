import numpy as np
import pandas as pd
from N_fctn_load_excel import load_excel_to_dataframe
import warnings
# Suppress the warning
warnings.filterwarnings("ignore", category=Warning)




daf_non_reduced_with_coin_none_deleted = load_excel_to_dataframe('df_nonreduced_coins.xlsx')
daf_non_reduced_with_coin_none_deleted = daf_non_reduced_with_coin_none_deleted[daf_non_reduced_with_coin_none_deleted['coins'] != 0]

#coins specific analysis:
                                                                                                                               #a) CORREL.MATRIX
from Q_fctn_create_correlation_matrix import create_correlation_matrix
create_correlation_matrix(daf_non_reduced_with_coin_none_deleted,['link',                                        
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
'localities_rate'],'Correlation Matrix Non Reduced - Coins - 5323 Obs.')

#we choose the same variables:
#from the correlation matrix we chose 10 variables with the strongest correlation to rates and that are subject to the main hypotheses:
from B_fctn_drop_columns import drop_columns
daf_non_reduced_with_coin_none_deleted = drop_columns(daf_non_reduced_with_coin_none_deleted, ['area_municipality',                           
'municipality_type',                           
'population_density',
'average_age',                            
'uploaded_at_least_one_artif_or_coin_dummy',   
'men_proportion',                              
'65+_proportion'])

#B) SUMMARY STATS
from Q_fction_get_summary_statistics import get_extended_summary_statistics
from Q_fction_get_summary_statistics import get_summary_statistics
summary_non_reduced_1_coins = get_summary_statistics(daf_non_reduced_with_coin_none_deleted)
print(summary_non_reduced_1_coins)


summary_non_reduced_1_ext_coins = get_extended_summary_statistics(daf_non_reduced_with_coin_none_deleted)
print(summary_non_reduced_1_ext_coins)

                                                                                                                                #C) LOG TRANSFORMATION

df_log_coins = daf_non_reduced_with_coin_none_deleted[['artifs_rate', 'experience','contributions',               
'comments',                    
'artifacts',                   
'coins',                                      
'real_net_monetary_index',                 
'coins_rate',                    
'localities_rate','rate_artifs_dummy',                           
'rate_coins_dummy', 'link', 'residence_additional_info', 'detector_expensive_dummy']]


df_log_coins['log_experience'] = np.log(df_log_coins['experience'].values + 1)
df_log_coins['log_contributions'] = np.log(df_log_coins['contributions'].values + 1)
df_log_coins['log_comments'] = np.log(df_log_coins['comments'].values + 1)
df_log_coins['log_artifacts'] = np.log(df_log_coins['artifacts'].values + 1)
df_log_coins['log_coins'] = np.log(df_log_coins['coins'].values + 1)
df_log_coins['log_coins_rate'] = np.log(df_log_coins['coins_rate'].values + 1)
df_log_coins['log_artifs_rate'] = np.log(df_log_coins['artifs_rate'].values + 1)
df_log_coins['reverse_coins_rate'] = (1 - df_log_coins['coins_rate'].values) 



                                                                                                                                    #D) HISTOGRAMS: 
#******************************************************
#HISTOGRAMS for the ind. variables (non-dummies):
from S_fctn_plot_histograms import create_histograms_with_zeros
from S_fctn_create_combined_hist import create_histograms_all
from S_fctn_create_combined_hist import create_log_transformed_histograms

create_histograms_all(df_log_coins, [                        
'experience',                  
'contributions',               
'comments',                                       
'coins',                                      
'real_net_monetary_index',                    
'localities_rate', 'artifs_rate', 'coins_rate'])

create_log_transformed_histograms(df_log_coins, [                        
'experience',                  
'contributions',               
'comments',                                    
'coins',                                                          
'artifs_rate', 'coins_rate'])

#histograms for the dependent variable with log transformation:
from S_fctn_plot_histograms import generate_histograms_w_log

#generate_histograms_w_log(df_log_coins, ['artifs_rate', 'coins_rate'])
#********************************************************



#********************************************************
#'PLOT INITIAL SCATTER PLOTS
from Q_fctn_plot_scatter import plot_scatter_all
plot_scatter_all(df_log_coins, 'coins_rate', ['experience', 'contributions',
                                     'comments', 'coins',
                                     'real_net_monetary_index', 'artifs_rate', 'localities_rate','link','detector_expensive_dummy'])

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

from V_fct_OLS_REGRESSION import ols_regression


#**FINALLY THE FINAL ANALYSIS**#
#*******************************************************************************************************************************************************************************************

#********************************************************************************************************************************************************************************************
from W_fctn_print_top import print_top_observations

print_top_observations(df_log_coins, columns=[ 'experience','contributions',               
'comments',                    
'coins'])
'''
Top 5 observations for column 'experience':
      experience  contributions  comments  coins
2765      498425             75     16255    176
2766      235138             20      9632    324
2767      209125            119     17572     85
71        207830             25      3085    282
2768      161310             25      4455    142

Top 5 observations for column 'contributions':
      experience  contributions  comments  coins
36           604           1489      8964     54
3729          88            502      2554      7
1034          74            395     24463    257
3203         506            256      4554     31
557           80            215      2005     12

Top 5 observations for column 'comments':
      experience  contributions  comments  coins
1034          74            395     24463    257
2770       99725              7     18608     14
2767      209125            119     17572     85
2765      498425             75     16255    176
2801       22958             62     12380    272

Top 5 observations for column 'coins':
      experience  contributions  comments  coins
2858        7882             28      1716    713
2824       13484             57      3148    553
2775       71293             11       609    490
501        16429            164      1175    472
824       145348              2     11539    463
'''

df_log_2 = df_log_coins.copy()



df_log_2 = df_log_2[df_log_2['experience'] != 498425]
df_log_2 = df_log_2[df_log_2['contributions'] != 1489]
df_log_2 = df_log_2[df_log_2['comments'] != 24463]
                                                    #DELETE THE MOST SIGNIFICANT OUTLIERS

df_log_3 = df_log_2.copy()                        #DF_LOG_3 USED JUST FOR THE BINARY DEPENDENT MODELS
df_log_2 = df_log_2[df_log_2['coins_rate'] != 1]  #DELETE THE ONES

#********************************************************************
#plot scatter plots after log transform and without outliers:
from Q_fctn_plot_scatter import plot_scatter_all
plot_scatter_all(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                      'log_comments', 'log_coins', 
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link','detector_expensive_dummy'])
#********************************************************************
#for coins we use the plot_scatter_all only...


#first model, without log transform:
model1 = ols_regression(df_log_2, 'coins_rate', [ 'experience', 'contributions', 'comments', 'coins',
                                      'real_net_monetary_index', 'log_artifs_rate', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:             coins_rate   R-squared:                       0.156
Model:                            OLS   Adj. R-squared:                  0.154
Method:                 Least Squares   F-statistic:                     97.84
Date:                Thu, 13 Jul 2023   Prob (F-statistic):          1.28e-186
Time:                        09:23:21   Log-Likelihood:                 10792.
No. Observations:                5313   AIC:                        -2.156e+04
Df Residuals:                    5302   BIC:                        -2.149e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0044      0.008     -0.517      0.605      -0.021       0.012
experience                 4.841e-08   6.54e-08      0.740      0.459   -7.98e-08    1.77e-07
contributions               1.66e-05   3.14e-05      0.528      0.597    -4.5e-05    7.82e-05
comments                   7.958e-07   6.81e-07      1.169      0.242   -5.38e-07    2.13e-06
coins                     -2.572e-05   1.55e-05     -1.664      0.096    -5.6e-05    4.59e-06
real_net_monetary_index       0.0054      0.009      0.627      0.531      -0.012       0.022
log_artifs_rate               0.2475      0.008     29.848      0.000       0.231       0.264
localities_rate              -0.0261      0.036     -0.733      0.464      -0.096       0.044
link                          0.0031      0.003      1.176      0.239      -0.002       0.008
residence_additional_info     0.0017      0.004      0.443      0.658      -0.006       0.009
detector_expensive_dummy      0.0168      0.003      5.115      0.000       0.010       0.023
==============================================================================
Omnibus:                     9601.534   Durbin-Watson:                   2.014
Prob(Omnibus):                  0.000   Jarque-Bera (JB):         14105462.299
Skew:                          13.109   Prob(JB):                         0.00
Kurtosis:                     254.058   Cond. No.                     6.72e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.72e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

Breusch-Pagan Test for Heteroskedasticity:
(367.1584803732472, 9.060375598014958e-73, 39.359818854160665, 1.725425644014011e-75)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  380.230793
1                  experience    1.488646
2               contributions    1.236040
3                    comments    1.762037
4                       coins    1.305829
5     real_net_monetary_index    1.065795
6             log_artifs_rate    1.025199
7             localities_rate    1.064167
8                        link    1.031681
9   residence_additional_info    1.020807
10   detector_expensive_dummy    1.015079

Hausman Test for Endogeneity:
None
'''




model2 = ols_regression(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])






'''
model2_without_coins = ols_regression(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
#***********************************************************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************************************************************

'''
#MODEL2:
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:         log_coins_rate   R-squared:                       0.164
Model:                            OLS   Adj. R-squared:                  0.162
Method:                 Least Squares   F-statistic:                     104.0
Date:                Thu, 13 Jul 2023   Prob (F-statistic):          8.59e-198
Time:                        09:23:21   Log-Likelihood:                 11904.
No. Observations:                5313   AIC:                        -2.379e+04
Df Residuals:                    5302   BIC:                        -2.371e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0041      0.007     -0.585      0.558      -0.018       0.010
log_experience               -0.0001      0.000     -0.548      0.584      -0.000       0.000
log_contributions             0.0006      0.000      1.226      0.220      -0.000       0.001
log_comments                  0.0004      0.000      1.275      0.202      -0.000       0.001
log_coins                 -9.932e-05      0.000     -0.211      0.833      -0.001       0.001
real_net_monetary_index       0.0040      0.007      0.564      0.573      -0.010       0.018
log_artifs_rate               0.2052      0.007     30.291      0.000       0.192       0.218
localities_rate              -0.0182      0.029     -0.630      0.529      -0.075       0.038
link                          0.0026      0.002      1.217      0.223      -0.002       0.007
residence_additional_info     0.0006      0.003      0.179      0.858      -0.006       0.007
detector_expensive_dummy      0.0137      0.003      5.178      0.000       0.009       0.019
==============================================================================
Omnibus:                     8889.148   Durbin-Watson:                   2.018
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          7654627.239
Skew:                          11.286   Prob(JB):                         0.00
Kurtosis:                     187.576   Cond. No.                         478.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Breusch-Pagan Test for Heteroskedasticity:
(418.0971983151484, 1.3196971712556254e-83, 45.28693286215813, 3.4849892104988695e-87)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  384.210623
1              log_experience    2.128533
2           log_contributions    1.494346
3                log_comments    2.842563
4                   log_coins    2.280516
5     real_net_monetary_index    1.065963
6             log_artifs_rate    1.039461
7             localities_rate    1.064005
8                        link    1.019536
9   residence_additional_info    1.030262
10   detector_expensive_dummy    1.009787

Hausman Test for Endogeneity:
None
'''
#BETTER R2 COMPARED TO THE ARTIFS RATE SAMPLE... DETECTOR DUMMY EXCEPT FROM WLS SIGNIFICANT









#->DUE TO HETEROSKEDASTICITY (B-P TEST) WE DO HETEROSKEDASTICITY ROBUST REGRESSION, I.E. WLS:
from V_fctn_OLS_ROBUST import ols_regression_robust
'''
model4_ROBUST = ols_regression_robust(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''


model2_ROBUST = ols_regression_robust(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:         log_coins_rate   R-squared:                       0.164
Model:                            OLS   Adj. R-squared:                  0.162
Method:                 Least Squares   F-statistic:                     7.314
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           1.33e-11
Time:                        09:23:21   Log-Likelihood:                 11904.
No. Observations:                5313   AIC:                        -2.379e+04
Df Residuals:                    5302   BIC:                        -2.371e+04
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0041      0.008     -0.522      0.601      -0.019       0.011
log_experience               -0.0001      0.000     -0.483      0.629      -0.001       0.000
log_contributions             0.0006      0.001      1.045      0.296      -0.001       0.002
log_comments                  0.0004      0.000      1.564      0.118      -0.000       0.001
log_coins                 -9.932e-05      0.000     -0.210      0.834      -0.001       0.001
real_net_monetary_index       0.0040      0.008      0.487      0.626      -0.012       0.020
log_artifs_rate               0.2052      0.039      5.273      0.000       0.129       0.281
localities_rate              -0.0182      0.025     -0.735      0.463      -0.067       0.030
link                          0.0026      0.004      0.728      0.467      -0.004       0.010
residence_additional_info     0.0006      0.006      0.096      0.923      -0.011       0.012
detector_expensive_dummy      0.0137      0.006      2.117      0.034       0.001       0.026
==============================================================================
Omnibus:                     8889.148   Durbin-Watson:                   2.018
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          7654627.239
Skew:                          11.286   Prob(JB):                         0.00
Kurtosis:                     187.576   Cond. No.                         478.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(418.0971983151484, 1.3196971712556254e-83, 45.28693286215813, 3.4849892104988695e-87)

White's Test for Heteroskedasticity:
(760.6865277136018, 6.8581589313656426e-121, 14.149502774120121, 5.969151735747907e-132)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  384.210623
1              log_experience    2.128533
2           log_contributions    1.494346
3                log_comments    2.842563
4                   log_coins    2.280516
5     real_net_monetary_index    1.065963
6             log_artifs_rate    1.039461
7             localities_rate    1.064005
8                        link    1.019536
9   residence_additional_info    1.030262
10   detector_expensive_dummy    1.009787
'''




#->>>>>>>>>now WLS:
from V_fctn_OLS_WLS import ols_regression_wls
'''
model1_WLS = ols_regression_wls(df_log_2, 'artifs_rate', [ 'experience', 'contributions', 'comments', 'artifacts',
                                      'real_net_monetary_index', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])



model4_WLS = ols_regression_wls(df_log_2, 'log_artifs_rate', ['log_experience', 'log_contributions', 
                                     'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''
model2_WLS = ols_regression_wls(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])


'''
Regression Summary:
                            WLS Regression Results
==============================================================================
Dep. Variable:         log_coins_rate   R-squared:                       0.914
Model:                            WLS   Adj. R-squared:                  0.914
Method:                 Least Squares   F-statistic:                     5659.
Date:                Thu, 13 Jul 2023   Prob (F-statistic):               0.00
Time:                        09:23:21   Log-Likelihood:                 36655.
No. Observations:                5313   AIC:                        -7.329e+04
Df Residuals:                    5302   BIC:                        -7.322e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0003   2.41e-05    -13.005      0.000      -0.000      -0.000
log_experience             -8.07e-06   6.01e-07    -13.432      0.000   -9.25e-06   -6.89e-06
log_contributions          5.261e-05   3.69e-06     14.243      0.000    4.54e-05    5.98e-05
log_comments               3.078e-05   2.26e-06     13.608      0.000    2.63e-05    3.52e-05
log_coins                 -7.412e-06   6.48e-07    -11.447      0.000   -8.68e-06   -6.14e-06
real_net_monetary_index       0.0003   2.36e-05     12.933      0.000       0.000       0.000
log_artifs_rate               0.2175      0.001    232.852      0.000       0.216       0.219
localities_rate              -0.0014      0.000    -13.306      0.000      -0.002      -0.001
link                      -2.624e-05   9.88e-05     -0.266      0.791      -0.000       0.000
residence_additional_info   4.08e-05   8.71e-06      4.687      0.000    2.37e-05    5.79e-05
detector_expensive_dummy      0.0004      0.001      0.639      0.523      -0.001       0.002
==============================================================================
Omnibus:                     9881.766   Durbin-Watson:                   1.904
Prob(Omnibus):                  0.000   Jarque-Bera (JB):         63159792.946
Skew:                          13.255   Prob(JB):                         0.00
Kurtosis:                     536.483   Cond. No.                     2.36e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.36e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  384.210623
1              log_experience    2.128533
2           log_contributions    1.494346
3                log_comments    2.842563
4                   log_coins    2.280516
5     real_net_monetary_index    1.065963
6             log_artifs_rate    1.039461
7             localities_rate    1.064005
8                        link    1.019536
9   residence_additional_info    1.030262
10   detector_expensive_dummy    1.009787
#->>>>>>>>>>>>>>>>>>>This model has relatively large R2 0.914. This together with many variables significant  at 5% sign.level might...
# indicate over-fitting or some other issue. 
'''




#now LPM:
model2_LPM = ols_regression_robust(df_log_3, 'rate_coins_dummy', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   R-squared:                       0.194
Model:                            OLS   Adj. R-squared:                  0.193
Method:                 Least Squares   F-statistic:                     18.11
Date:                Sat, 15 Jul 2023   Prob (F-statistic):           5.55e-33
Time:                        16:04:48   Log-Likelihood:                 2699.5
No. Observations:                5319   AIC:                            -5377.
Df Residuals:                    5308   BIC:                            -5305.
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0390      0.033     -1.188      0.235      -0.103       0.025
log_experience                0.0005      0.001      0.417      0.676      -0.002       0.003
log_contributions             0.0170      0.004      3.963      0.000       0.009       0.025
log_comments                  0.0009      0.002      0.493      0.622      -0.003       0.004
log_coins                     0.0174      0.003      5.094      0.000       0.011       0.024
real_net_monetary_index       0.0060      0.033      0.181      0.857      -0.060       0.072
log_artifs_rate               1.0789      0.116      9.319      0.000       0.852       1.306
localities_rate               0.0949      0.148      0.643      0.520      -0.195       0.384
link                          0.0230      0.018      1.261      0.207      -0.013       0.059
residence_additional_info     0.0108      0.032      0.338      0.736      -0.052       0.074
detector_expensive_dummy      0.0603      0.027      2.230      0.026       0.007       0.113
==============================================================================
Omnibus:                     4927.055   Durbin-Watson:                   2.033
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           182356.044
Skew:                           4.514   Prob(JB):                         0.00
Kurtosis:                      30.227   Cond. No.                         478.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(743.0435553370152, 3.58555444268654e-153, 86.19127475150947, 2.9371387953827167e-165)

White's Test for Heteroskedasticity:
(1080.2824032348506, 9.907928234605495e-186, 21.605607698101643, 2.4195634450917713e-210)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  384.021385
1              log_experience    2.127189
2           log_contributions    1.495900
3                log_comments    2.843294
4                   log_coins    2.271146
5     real_net_monetary_index    1.066197
6             log_artifs_rate    1.039400
7             localities_rate    1.064306
8                        link    1.021151
9   residence_additional_info    1.029948
10   detector_expensive_dummy    1.009560
'''


#>>>>>>>>>>now LOGIT:
from V_fctn_LOGIT import logit_regression_roc_wald
model2_LOGIT = logit_regression_roc_wald(df_log_3, dependent_var='rate_coins_dummy', independent_vars=['log_experience', 'log_contributions', 
                                        'log_comments', 'log_coins',
                                        'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'],
                                        pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                        ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                        hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])


'''
Optimization terminated successfully.
         Current function value: 0.081343
         Iterations 9
Logit Regression Summary:
                           Logit Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   No. Observations:                 5319
Model:                          Logit   Df Residuals:                     5308
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.3462
Time:                        09:42:20   Log-Likelihood:                -432.66
converged:                       True   LL-Null:                       -661.76
Covariance Type:            nonrobust   LLR p-value:                 3.721e-92
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -7.0666      2.112     -3.346      0.001     -11.206      -2.927
log_experience                0.0426      0.051      0.840      0.401      -0.057       0.142
log_contributions             0.1143      0.085      1.341      0.180      -0.053       0.281
log_comments                  0.2522      0.084      2.986      0.003       0.087       0.418
log_coins                     0.5661      0.112      5.037      0.000       0.346       0.786
real_net_monetary_index      -0.1142      2.133     -0.054      0.957      -4.295       4.067
log_artifs_rate              11.4004      0.844     13.513      0.000       9.747      13.054
localities_rate               9.3570      8.544      1.095      0.273      -7.388      26.102
link                         -0.0816      0.403     -0.202      0.840      -0.872       0.708
residence_additional_info     0.1827      0.612      0.299      0.765      -1.016       1.382
detector_expensive_dummy      1.4639      0.411      3.563      0.000       0.659       2.269
=============================================================================================

Area Under the Curve (AUC): 0.9007320182501342

'''

#now PROBIT:
from V_fctn_PROBIT import probit_regression_roc_wald


model2_PROBIT = probit_regression_roc_wald(df_log_3, dependent_var='rate_coins_dummy', independent_vars=['log_experience', 'log_contributions', 
                                            'log_comments', 'log_coins',
                                            'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'],
                                            pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                            ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                            hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])


'''
Optimization terminated successfully.
         Current function value: 0.081356
         Iterations 8
Probit Regression Summary:
                          Probit Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   No. Observations:                 5319
Model:                         Probit   Df Residuals:                     5308
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.3461
Time:                        09:42:21   Log-Likelihood:                -432.73
converged:                       True   LL-Null:                       -661.76
Covariance Type:            nonrobust   LLR p-value:                 3.992e-92
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -3.5581      0.966     -3.682      0.000      -5.452      -1.664
log_experience                0.0199      0.023      0.861      0.389      -0.025       0.065
log_contributions             0.0601      0.042      1.416      0.157      -0.023       0.143
log_comments                  0.1056      0.040      2.663      0.008       0.028       0.183
log_coins                     0.2437      0.052      4.726      0.000       0.143       0.345
real_net_monetary_index       0.1528      0.974      0.157      0.875      -1.755       2.061
log_artifs_rate               5.6698      0.407     13.930      0.000       4.872       6.468
localities_rate               2.3490      3.937      0.597      0.551      -5.367      10.065
link                          0.0412      0.202      0.204      0.839      -0.355       0.437
residence_additional_info     0.0066      0.290      0.023      0.982      -0.562       0.575
detector_expensive_dummy      0.6621      0.210      3.150      0.002       0.250       1.074
=============================================================================================

Area Under the Curve (AUC): 0.9028884863123994
'''

