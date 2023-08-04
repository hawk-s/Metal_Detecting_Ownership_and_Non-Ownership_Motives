###reduced dataset

from functions.N_fctn_load_excel import load_excel_to_dataframe
from functions.N_fctn_subset_non_none import subset_non_none_values
from functions.P_fctn_fill_missing_values import fill_missing_values
from functions.B_fctn_drop_columns import drop_columns
import warnings
#suppress the warning:
warnings.filterwarnings("ignore", category=Warning)

daf = load_excel_to_dataframe('P_FINAL_DATA.xlsx')
daf_reduced = subset_non_none_values(daf, 'real_net_monetary_index')


daf_reduced_copy = daf_reduced.copy()

#nans in coins and artifs filled:
daf_reduced_with_none_being_zero = fill_missing_values(daf_reduced_copy, {'artifs_rate':0, 'coins_rate':0, 'rate_artifs_dummy':0, 'rate_coins_dummy':0}) 

daf_reduced_with_none_being_zero = drop_columns(daf_reduced_with_none_being_zero, ['number_artifs','submitted_number_artifs', 'number_coins', 'submitted_number_coins'],)

#print(daf_reduced_with_none_being_zero)

#print(daf_reduced_with_none_being_zero['artifacts'] )
daf_reduced_with_none_being_zero = subset_non_none_values(daf_reduced_with_none_being_zero, 'artifacts')

daf_artif_or_coin_uploaded = daf_reduced_with_none_being_zero.copy()

'''
daf_reduced_with_none_being_zero = daf_reduced_with_none_being_zero[daf_reduced_with_none_being_zero['artifacts'] != 0]

print(daf_reduced_with_none_being_zero['artifacts'] )
'''

from functions.R_fctn_subset_dataframe import subset_dataframe
daf_reduced_with_none_being_zero = subset_dataframe(daf_artif_or_coin_uploaded, 'uploaded_at_least_one_artif_or_coin_dummy')
#print(daf_reduced_with_none_being_zero['artifacts'] )

#keep artif or coin uploaded.

#now correlation matrix:
from functions.Q_fctn_create_correlation_matrix import create_correlation_matrix


create_correlation_matrix(daf_reduced_with_none_being_zero,['link',                                        
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
'localities_rate'],'Correlation Matrix Reduced - Artifacts - 4160 Observations')






#############->>>>>>>so from the correlation matrix, only slight changes so we keep the same variables as in the 1st non-reduced dataset:
daf_reduced_with_none_being_zero = drop_columns(daf_reduced_with_none_being_zero, ['area_municipality',                           
'municipality_type',                           
'population_density',
'average_age',                                                        
'uploaded_at_least_one_artif_or_coin_dummy',   
'men_proportion',                              
'65+_proportion'])

#->here we drop also the dummies for rate artifs a rate_coins since those will be used in Logit/Probit only.

#############2. ! summary statistics:
from functions.Q_fction_get_summary_statistics import get_summary_statistics
from functions.Q_fction_get_summary_statistics import get_extended_summary_statistics
summary_reduced_1 = get_summary_statistics(daf_reduced_with_none_being_zero)
print(summary_reduced_1 )

summary_reduced_1_ext = get_extended_summary_statistics(daf_reduced_with_none_being_zero)
print(summary_reduced_1_ext)

                                                                                                                                #C) LOG TRANSFORMATION


from functions.E_fctn_display_unique_values import display_unique_values

#print(display_unique_values(daf_non_reduced_with_none_being_zero, 'municipal_office'))



import numpy as np
df_log = daf_reduced_with_none_being_zero[['artifs_rate', 'experience','contributions',               
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
from functions.S_fctn_create_combined_hist import create_histograms_all
from functions.S_fctn_create_combined_hist import create_log_transformed_histograms
from functions.S_fctn_plot_histograms import create_histograms_with_zeros
create_histograms_all(df_log, [                        
'experience',                  
'contributions',               
'comments',                                       
'artifacts',                                      
'real_net_monetary_index',                    
'localities_rate', 'artifs_rate', 'coins_rate'])

create_log_transformed_histograms(df_log, [                        
'experience',                  
'contributions',               
'comments',                                    
'artifacts',                                                          
'artifs_rate', 'coins_rate'])

#histograms for the dependent variable with log transformation:
from functions.S_fctn_plot_histograms import generate_histograms_w_log

#generate_histograms_w_log(df_log_coins, ['artifs_rate', 'coins_rate'])
#********************************************************



#********************************************************
#'PLOT INITIAL SCATTER PLOTS
from functions.Q_fctn_plot_scatter import plot_scatter_all
plot_scatter_all(df_log, 'artifs_rate', ['experience', 'contributions',
                                     'comments', 'artifacts',
                                     'real_net_monetary_index', 'coins_rate', 'localities_rate','link','detector_expensive_dummy'])


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
#********************************************************************************************************************************************************************************************
from functions.W_fctn_print_top import print_top_observations

print_top_observations(df_log, columns=[ 'experience','contributions',               
'comments',                    
'artifacts'])
'''
Top 5 observations for column 'experience':
      experience  contributions  comments  artifacts
119       207830             25      3085        735
1262      145348              2     11539        724
2615      137050              3      3371        355
1664       92662             56      3044        939
120        88322              3      1432         52

Top 5 observations for column 'contributions':
      experience  contributions  comments  artifacts
61           604           1489      8964        125
1580          74            395     24463       3332
851           80            215      2005          0
756        16429            164      1175        309
2252          30            149      2023          1

Top 5 observations for column 'comments':
      experience  contributions  comments  artifacts
1580          74            395     24463       3332
1262      145348              2     11539        724
4030        7914             20     10105         15
128         2795              6      9250        293
61           604           1489      8964        125

Top 5 observations for column 'artifacts':
      experience  contributions  comments  artifacts
1580          74            395     24463       3332
1664       92662             56      3044        939
2683       17075             13      1044        798
119       207830             25      3085        735
1262      145348              2     11539        724

'''

df_log_2 = df_log.copy()


df_log_2 = df_log_2[df_log_2['experience'] != 207830]
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
#for coins we use the plot_scatter_all only


#first model, without log transform:
model1 = ols_regression(df_log_2, 'artifs_rate', [ 'experience', 'contributions', 'comments', 'artifacts',
                                      'real_net_monetary_index', 'coins_rate', 'localities_rate', 'link', 'residence_additional_info', 'detector_expensive_dummy'])




'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:            artifs_rate   R-squared:                       0.050
Model:                            OLS   Adj. R-squared:                  0.048
Method:                 Least Squares   F-statistic:                     21.96
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           1.75e-40
Time:                        13:06:58   Log-Likelihood:                 6298.9
No. Observations:                4142   AIC:                        -1.258e+04
Df Residuals:                    4131   BIC:                        -1.251e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0077      0.012      0.665      0.506      -0.015       0.030
experience                  1.48e-07   2.36e-07      0.628      0.530   -3.14e-07     6.1e-07
contributions                 0.0002   9.85e-05      1.778      0.075   -1.79e-05       0.000
comments                   2.067e-06    2.5e-06      0.828      0.408   -2.83e-06    6.96e-06
artifacts                  2.445e-05   2.38e-05      1.028      0.304   -2.22e-05    7.11e-05
real_net_monetary_index      -0.0018      0.012     -0.156      0.876      -0.025       0.021
coins_rate                    0.2924      0.023     12.748      0.000       0.247       0.337
localities_rate               0.0400      0.049      0.824      0.410      -0.055       0.135
link                          0.0167      0.005      3.314      0.001       0.007       0.027
residence_additional_info    -0.0086      0.009     -0.926      0.355      -0.027       0.010
detector_expensive_dummy      0.0176      0.006      2.728      0.006       0.005       0.030
==============================================================================
Omnibus:                     5503.500   Durbin-Watson:                   2.014
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           913686.791
Skew:                           7.624   Prob(JB):                         0.00
Kurtosis:                      74.145   Cond. No.                     2.60e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.6e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

Breusch-Pagan Test for Heteroskedasticity:
(155.06372878271034, 3.37863357669873e-28, 16.066679275156783, 9.334314383213594e-29)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  197.220048
1                  experience    1.560085
2               contributions    1.198370
3                    comments    1.747128
4                   artifacts    1.613971
5     real_net_monetary_index    1.072771
6                  coins_rate    1.015129
7             localities_rate    1.070238
8                        link    1.018411
9   residence_additional_info    1.013058
10   detector_expensive_dummy    1.020230

Hausman Test for Endogeneity:
None
'''

#->The initial model before as well as after deleting the outliers do not perform very well due to the 'numerical issues' so we create a logarithmic model


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
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:        log_artifs_rate   R-squared:                       0.072
Model:                            OLS   Adj. R-squared:                  0.070
Method:                 Least Squares   F-statistic:                     32.04
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           2.09e-60
Time:                        13:06:58   Log-Likelihood:                 7116.3
No. Observations:                4142   AIC:                        -1.421e+04
Df Residuals:                    4131   BIC:                        -1.414e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0016      0.010      0.171      0.864      -0.017       0.020
log_experience                0.0019      0.000      4.890      0.000       0.001       0.003
log_contributions             0.0012      0.001      1.078      0.281      -0.001       0.004
log_comments                 -0.0001      0.001     -0.169      0.866      -0.001       0.001
log_artifacts                 0.0009      0.001      1.167      0.243      -0.001       0.002
real_net_monetary_index      -0.0015      0.010     -0.155      0.877      -0.020       0.017
log_coins_rate                0.3439      0.025     13.805      0.000       0.295       0.393
localities_rate               0.0329      0.040      0.826      0.409      -0.045       0.111
link                          0.0129      0.004      3.110      0.002       0.005       0.021
residence_additional_info    -0.0081      0.008     -1.049      0.294      -0.023       0.007
detector_expensive_dummy      0.0106      0.005      2.003      0.045       0.000       0.021
==============================================================================
Omnibus:                     5226.033   Durbin-Watson:                   2.032
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           669506.132
Skew:                           7.021   Prob(JB):                         0.00
Kurtosis:                      63.681   Cond. No.                         278.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Breusch-Pagan Test for Heteroskedasticity:
(160.91219641512728, 2.1001133859693647e-29, 16.69715203950839, 5.208679088321964e-30)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  199.866225
1              log_experience    1.986325
2           log_contributions    1.411086
3                log_comments    2.850073
4               log_artifacts    2.270130
5     real_net_monetary_index    1.073633
6              log_coins_rate    1.023360
7             localities_rate    1.070840
8                        link    1.016890
9   residence_additional_info    1.030200
10   detector_expensive_dummy    1.023625

Hausman Test for Endogeneity:
None
'''







#->DUE TO HETEROSKEDASTICITY (B-P TEST) WE DO HETEROSKEDASTICITY ROBUST REGRESSION, WLS:
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
Dep. Variable:        log_artifs_rate   R-squared:                       0.072
Model:                            OLS   Adj. R-squared:                  0.070
Method:                 Least Squares   F-statistic:                     10.56
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           7.16e-18
Time:                        13:06:58   Log-Likelihood:                 7116.3
No. Observations:                4142   AIC:                        -1.421e+04
Df Residuals:                    4131   BIC:                        -1.414e+04
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         0.0016      0.009      0.182      0.856      -0.016       0.019
log_experience                0.0019      0.000      4.563      0.000       0.001       0.003
log_contributions             0.0012      0.001      0.835      0.404      -0.002       0.004
log_comments                 -0.0001      0.001     -0.149      0.881      -0.002       0.001
log_artifacts                 0.0009      0.001      1.276      0.202      -0.000       0.002
real_net_monetary_index      -0.0015      0.009     -0.166      0.868      -0.019       0.016
log_coins_rate                0.3439      0.124      2.768      0.006       0.100       0.588
localities_rate               0.0329      0.035      0.941      0.347      -0.036       0.102
link                          0.0129      0.006      2.130      0.033       0.001       0.025
residence_additional_info    -0.0081      0.003     -2.767      0.006      -0.014      -0.002
detector_expensive_dummy      0.0106      0.009      1.210      0.226      -0.007       0.028
==============================================================================
Omnibus:                     5226.033   Durbin-Watson:                   2.032
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           669506.132
Skew:                           7.021   Prob(JB):                         0.00
Kurtosis:                      63.681   Cond. No.                         278.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(160.91219641512728, 2.1001133859693647e-29, 16.69715203950839, 5.208679088321964e-30)

White's Test for Heteroskedasticity:
(309.4934926373229, 2.7300555899263997e-35, 5.4926757942287745, 5.257397945162682e-37)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  199.866225
1              log_experience    1.986325
2           log_contributions    1.411086
3                log_comments    2.850073
4               log_artifacts    2.270130
5     real_net_monetary_index    1.073633
6              log_coins_rate    1.023360
7             localities_rate    1.070840
8                        link    1.016890
9   residence_additional_info    1.030200
10   detector_expensive_dummy    1.023625
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
Dep. Variable:        log_artifs_rate   R-squared:                       0.726
Model:                            WLS   Adj. R-squared:                  0.725
Method:                 Least Squares   F-statistic:                     1094.
Date:                Thu, 13 Jul 2023   Prob (F-statistic):               0.00
Time:                        13:06:59   Log-Likelihood:                 18181.
No. Observations:                4142   AIC:                        -3.634e+04
Df Residuals:                    4131   BIC:                        -3.627e+04
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0004   7.76e-05     -4.671      0.000      -0.001      -0.000
log_experience                0.0017   2.55e-05     65.329      0.000       0.002       0.002
log_contributions             0.0014   7.27e-05     19.381      0.000       0.001       0.002
log_comments               2.386e-05   4.99e-06      4.782      0.000    1.41e-05    3.36e-05
log_artifacts                 0.0001   2.47e-05      5.904      0.000    9.72e-05       0.000
real_net_monetary_index       0.0003   7.52e-05      4.401      0.000       0.000       0.000
log_coins_rate                0.3827      0.012     30.754      0.000       0.358       0.407
localities_rate              -0.0063      0.001     -6.563      0.000      -0.008      -0.004
link                         -0.0009      0.001     -0.815      0.415      -0.003       0.001
residence_additional_info    -0.0068      0.000    -47.749      0.000      -0.007      -0.007
detector_expensive_dummy      0.0004      0.001      0.279      0.780      -0.002       0.003
==============================================================================
Omnibus:                     4616.683   Durbin-Watson:                   1.405
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          1148266.095
Skew:                           5.273   Prob(JB):                         0.00
Kurtosis:                      83.884   Cond. No.                     1.32e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.32e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  199.866225
1              log_experience    1.986325
2           log_contributions    1.411086
3                log_comments    2.850073
4               log_artifacts    2.270130
5     real_net_monetary_index    1.073633
6              log_coins_rate    1.023360
7             localities_rate    1.070840
8                        link    1.016890
9   residence_additional_info    1.030200
10   detector_expensive_dummy    1.023625
#->>>>>>>>>>>>>>>>>>>This model has relatively large R2 0.966. This together with many variables significant  at 5% sign.level might...
# indicate over-fitting or some other issue. 
'''





#now LPM:
model2_LPM = ols_regression_robust(df_log_3, 'rate_artifs_dummy', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'])
'''
Regression Summary:
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   R-squared:                       0.151
Model:                            OLS   Adj. R-squared:                  0.149
Method:                 Least Squares   F-statistic:                     25.13
Date:                Sat, 15 Jul 2023   Prob (F-statistic):           8.97e-47
Time:                        16:18:32   Log-Likelihood:                 382.59
No. Observations:                4157   AIC:                            -743.2
Df Residuals:                    4146   BIC:                            -673.5
Df Model:                          10
Covariance Type:                  HC1
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0454      0.048     -0.949      0.343      -0.139       0.048
log_experience                0.0115      0.002      5.213      0.000       0.007       0.016
log_contributions             0.0159      0.009      1.821      0.069      -0.001       0.033
log_comments                  0.0070      0.004      1.822      0.068      -0.001       0.015
log_artifacts                 0.0324      0.004      7.421      0.000       0.024       0.041
real_net_monetary_index      -0.0047      0.048     -0.097      0.923      -0.099       0.090
log_coins_rate                1.4684      0.336      4.373      0.000       0.810       2.127
localities_rate               0.3139      0.197      1.592      0.111      -0.073       0.700
link                          0.0273      0.027      1.013      0.311      -0.026       0.080
residence_additional_info     0.0113      0.047      0.239      0.811      -0.081       0.104
detector_expensive_dummy      0.0288      0.035      0.835      0.404      -0.039       0.097
==============================================================================
Omnibus:                     2633.902   Durbin-Watson:                   2.015
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            23765.645
Skew:                           3.027   Prob(JB):                         0.00
Kurtosis:                      13.028   Cond. No.                         278.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(465.8956625389168, 8.479203157342855e-94, 52.33131443298611, 1.1940961249430637e-99)

White's Test for Heteroskedasticity:
(592.7116453939552, 1.1882348064055834e-88, 11.352181501609437, 7.228447713855621e-97)

Variance Inflation Factor (VIF):
                     Variable         VIF
0                       const  199.758721
1              log_experience    1.981962
2           log_contributions    1.419487
3                log_comments    2.848256
4               log_artifacts    2.264387
5     real_net_monetary_index    1.073085
6              log_coins_rate    1.025105
7             localities_rate    1.070405
8                        link    1.021462
9   residence_additional_info    1.031470
10   detector_expensive_dummy    1.020800
'''


#>>>>>>>>>>now LOGIT:
from functions.V_fctn_LOGIT import logit_regression_roc_wald
model2_LOGIT = logit_regression_roc_wald(df_log_3, dependent_var='rate_artifs_dummy', independent_vars=['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'],
                                     pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                     ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                     hypotheses_variables=['real_net_monetary_index',  'localities_rate'])


'''
Optimization terminated successfully.
         Current function value: 0.177048
         Iterations 8
Logit Regression Summary:
                           Logit Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   No. Observations:                 4157
Model:                          Logit   Df Residuals:                     4146
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.2302
Time:                        13:07:00   Log-Likelihood:                -735.99
converged:                       True   LL-Null:                       -956.06
Covariance Type:            nonrobust   LLR p-value:                 2.642e-88
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -4.8348      1.000     -4.835      0.000      -6.795      -2.875
log_experience                0.1572      0.040      3.976      0.000       0.080       0.235
log_contributions            -0.0066      0.086     -0.076      0.939      -0.176       0.163
log_comments                  0.1618      0.067      2.415      0.016       0.030       0.293
log_artifacts                 0.4623      0.078      5.957      0.000       0.310       0.614
real_net_monetary_index      -0.2618      1.004     -0.261      0.794      -2.229       1.705
log_coins_rate               10.2656      1.874      5.478      0.000       6.593      13.938
localities_rate               7.3308      4.061      1.805      0.071      -0.629      15.290
link                          0.2322      0.334      0.696      0.486      -0.422       0.886
residence_additional_info     0.5290      0.660      0.801      0.423      -0.765       1.823
detector_expensive_dummy      0.4769      0.425      1.123      0.262      -0.356       1.309
=============================================================================================

Area Under the Curve (AUC): 0.8406384347998007
'''

#now PROBIT:
from functions.V_fctn_PROBIT import probit_regression_roc_wald


model2_PROBIT = probit_regression_roc_wald(df_log_3, dependent_var='rate_artifs_dummy', independent_vars=['log_experience', 'log_contributions', 
                                     'log_comments', 'log_artifacts',
                                     'real_net_monetary_index', 'log_coins_rate', 'localities_rate','link', 'residence_additional_info', 'detector_expensive_dummy'],
                                     pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                     ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                     hypotheses_variables=['real_net_monetary_index',  'localities_rate'])


'''
Optimization terminated successfully.
         Current function value: 0.176846
         Iterations 7
Probit Regression Summary:
                          Probit Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   No. Observations:                 4157
Model:                         Probit   Df Residuals:                     4146
Method:                           MLE   Df Model:                           10
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.2311
Time:                        13:05:07   Log-Likelihood:                -735.15
converged:                       True   LL-Null:                       -956.06
Covariance Type:            nonrobust   LLR p-value:                 1.156e-88
=============================================================================================
                                coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -2.5384      0.499     -5.088      0.000      -3.516      -1.561
log_experience                0.0825      0.019      4.303      0.000       0.045       0.120
log_contributions             0.0171      0.047      0.368      0.713      -0.074       0.108
log_comments                  0.0692      0.033      2.084      0.037       0.004       0.134
log_artifacts                 0.2427      0.039      6.182      0.000       0.166       0.320
real_net_monetary_index      -0.1503      0.503     -0.299      0.765      -1.136       0.836
log_coins_rate                4.9539      0.758      6.535      0.000       3.468       6.440
localities_rate               3.4668      2.048      1.693      0.091      -0.548       7.482
link                          0.1150      0.179      0.643      0.520      -0.236       0.466
residence_additional_info     0.3310      0.325      1.018      0.308      -0.306       0.968
detector_expensive_dummy      0.2556      0.223      1.146      0.252      -0.181       0.693
=============================================================================================

Area Under the Curve (AUC): 0.8410863034895426
'''