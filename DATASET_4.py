###3.then create reduced dataset, i.e. delete nans 10mins
import numpy as np
from functions.N_fctn_load_excel import load_excel_to_dataframe
from functions.N_fctn_subset_non_none import subset_non_none_values
from functions.P_fctn_fill_missing_values import fill_missing_values
from functions.B_fctn_drop_columns import drop_columns
import warnings
# Suppress the warning
warnings.filterwarnings("ignore", category=Warning)

daf = load_excel_to_dataframe('P_FINAL_DATA.xlsx')
daf_reduced = subset_non_none_values(daf, 'real_net_monetary_index')


daf_reduced_copy = daf_reduced.copy()

#nans in coins and artifs filled:
daf_reduced_with_none_being_zero = fill_missing_values(daf_reduced_copy, {'artifs_rate':0, 'coins_rate':0, 'rate_artifs_dummy':0, 'rate_coins_dummy':0}) 

daf_reduced_with_none_being_zero = drop_columns(daf_reduced_with_none_being_zero, ['number_artifs','submitted_number_artifs', 'number_coins', 'submitted_number_coins'],)


daf_reduced_with_none_being_zero = daf_reduced_with_none_being_zero[daf_reduced_with_none_being_zero['coins'] != 0]
#print(daf_reduced_with_none_being_zero)



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
'localities_rate'],'Correlation Matrix Reduced - Coins - 2774 Observations')






#############->so from the correlation matrix, slight changes so we keep the same variables as in the 1sst non-reduced dataset...:
daf_reduced_with_none_being_zero = drop_columns(daf_reduced_with_none_being_zero, ['area_municipality',                           
'municipality_type',                           
'population_density',
'average_age',                                                             
'uploaded_at_least_one_artif_or_coin_dummy',   
'men_proportion',                              
'65+_proportion'])

#->>>>>>>here we drop also the dummies for rate artifs a rate_coins since those will be used in Logit/Probit only.

#############2. ! summary statistics:
from functions.Q_fction_get_summary_statistics import get_summary_statistics
from functions.Q_fction_get_summary_statistics import get_extended_summary_statistics
summary_reduced_1 = get_summary_statistics(daf_reduced_with_none_being_zero)
print(summary_reduced_1 )

summary_reduced_1_ext = get_extended_summary_statistics(daf_reduced_with_none_being_zero)
print(summary_reduced_1_ext)


                                                                                                                               #C) LOG TRANSFORMATION

df_log_coins = daf_reduced_with_none_being_zero[['artifs_rate', 'experience','contributions',               
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
#HISTOOGRAAMS for the ind. variables (non-dummies):
from functions.S_fctn_plot_histograms import create_histograms_with_zeros
from functions.S_fctn_create_combined_hist import create_histograms_all
from functions.S_fctn_create_combined_hist import create_log_transformed_histograms

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
from functions.S_fctn_plot_histograms import generate_histograms_w_log

#generate_histograms_w_log(df_log_coins, ['artifs_rate', 'coins_rate'])
#********************************************************

#here should be the group of histograms such as for scatters below:

#********************************************************
#'PLOT INITIAL SCATTER PLOTS
from functions.Q_fctn_plot_scatter import plot_scatter_all
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

from functions.V_fct_OLS_REGRESSION import ols_regression


#**THE FINAL ANALYSIS**#
#*******************************************************************************************************************************************************************************************

#********************************************************************************************************************************************************************************************
from functions.W_fctn_print_top import print_top_observations

print_top_observations(df_log_coins, columns=[ 'experience','contributions',               
'comments',                    
'coins'])
'''
Top 5 observations for column 'experience':
      experience  contributions  comments  coins
119       207830             25      3085    282
1262      145348              2     11539    463
2615      137050              3      3371    154
1664       92662             56      3044    138
120        88322              3      1432      8

Top 5 observations for column 'contributions':
      experience  contributions  comments  coins
61           604           1489      8964     54
1580          74            395     24463    257
851           80            215      2005     12
756        16429            164      1175    472
2252          30            149      2023      3

Top 5 observations for column 'comments':
      experience  contributions  comments  coins
1580          74            395     24463    257
1262      145348              2     11539    463
4030        7914             20     10105      8
128         2795              6      9250    175
61           604           1489      8964     54

Top 5 observations for column 'coins':
      experience  contributions  comments  coins
756        16429            164      1175    472
1262      145348              2     11539    463
3900       18594              5       821    314
119       207830             25      3085    282
1580          74            395     24463    257
'''

df_log_2 = df_log_coins.copy()




df_log_2 = df_log_2[df_log_2['experience'] != 207830]
df_log_2 = df_log_2[df_log_2['contributions'] != 1489]
df_log_2 = df_log_2[df_log_2['comments'] != 24463]
                                                    #DELETE THE MOST SIGNIFICANT OUTLIERS
df_log_3 = df_log_2.copy()

df_log_2 = df_log_2[df_log_2['coins_rate'] != 1]  #DELETE THE ONES
#********************************************************************
#plot scatter plots after log transform and without outliers:
from functions.Q_fctn_plot_scatter import plot_scatter_all
plot_scatter_all(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                      'log_comments', 'log_coins', 
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link','detector_expensive_dummy'])
#********************************************************************
#for coins we use the plot_scatter_all only...


#first model, without log transform:
model1 = ols_regression(df_log_2, 'coins_rate', [ 'experience', 'contributions', 'comments', 'coins',
                                      'real_net_monetary_index', 'log_artifs_rate', 'localities_rate', 'link', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:             coins_rate   R-squared:                       0.161
Model:                            OLS   Adj. R-squared:                  0.158
Method:                 Least Squares   F-statistic:                     58.85
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           9.04e-99
Time:                        17:55:04   Log-Likelihood:                 5927.3
No. Observations:                2767   AIC:                        -1.183e+04
Df Residuals:                    2757   BIC:                        -1.178e+04
Df Model:                           9
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -0.0058      0.008     -0.764      0.445      -0.021       0.009
experience                2.453e-09   1.24e-07      0.020      0.984   -2.41e-07    2.46e-07
contributions            -5.882e-05   5.81e-05     -1.012      0.311      -0.000    5.51e-05
comments                  3.657e-07   1.35e-06      0.271      0.787   -2.28e-06    3.01e-06
coins                    -1.066e-05   2.75e-05     -0.388      0.698   -6.46e-05    4.33e-05
real_net_monetary_index      0.0064      0.008      0.831      0.406      -0.009       0.022
log_artifs_rate              0.2117      0.010     20.499      0.000       0.191       0.232
localities_rate             -0.0222      0.032     -0.697      0.486      -0.085       0.040
link                         0.0077      0.003      2.523      0.012       0.002       0.014
detector_expensive_dummy     0.0302      0.004      7.734      0.000       0.023       0.038
==============================================================================
Omnibus:                     4717.632   Durbin-Watson:                   2.014
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          4043916.726
Skew:                          11.576   Prob(JB):                         0.00
Kurtosis:                     188.848   Cond. No.                     3.16e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.16e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

Breusch-Pagan Test for Heteroskedasticity:
(344.29422072384386, 1.0146885253750726e-68, 43.53347285663755, 1.635377671951719e-73)

Variance Inflation Factor (VIF):
                   Variable         VIF
0                     const  198.388471
1                experience    1.489270
2             contributions    1.219127
3                  comments    1.718209
4                     coins    1.488820
5   real_net_monetary_index    1.066416
6           log_artifs_rate    1.022844
7           localities_rate    1.064584
8                      link    1.028736
9  detector_expensive_dummy    1.012950

Hausman Test for Endogeneity:
None

'''

#->The initial model before as well as after deleting the outliers do not perform very well due to the 'numerical issues' so we create a logarithmic model


model2 = ols_regression(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'])


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
Method:                 Least Squares   F-statistic:                     60.22
Date:                Thu, 13 Jul 2023   Prob (F-statistic):          5.49e-101
Time:                        17:55:04   Log-Likelihood:                 6444.2
No. Observations:                2767   AIC:                        -1.287e+04
Df Residuals:                    2757   BIC:                        -1.281e+04
Df Model:                           9
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -0.0052      0.006     -0.815      0.415      -0.018       0.007
log_experience               0.0002      0.000      0.839      0.402      -0.000       0.001
log_contributions           -0.0005      0.001     -0.805      0.421      -0.002       0.001
log_comments                 0.0007      0.000      1.708      0.088      -0.000       0.002
log_coins                   -0.0006      0.001     -0.966      0.334      -0.002       0.001
real_net_monetary_index      0.0044      0.006      0.690      0.490      -0.008       0.017
log_artifs_rate              0.1747      0.009     20.197      0.000       0.158       0.192
localities_rate             -0.0157      0.026     -0.595      0.552      -0.067       0.036
link                         0.0053      0.003      2.091      0.037       0.000       0.010
detector_expensive_dummy     0.0244      0.003      7.529      0.000       0.018       0.031
==============================================================================
Omnibus:                     4505.266   Durbin-Watson:                   2.016
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          2816874.945
Skew:                          10.625   Prob(JB):                         0.00
Kurtosis:                     157.858   Cond. No.                         311.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Breusch-Pagan Test for Heteroskedasticity:
(341.68761579326684, 3.638027939924491e-68, 43.15745344239691, 7.013041612406115e-73)

Variance Inflation Factor (VIF):
                   Variable         VIF
0                     const  202.505982
1            log_experience    2.023773
2         log_contributions    1.360198
3              log_comments    2.482002
4                 log_coins    2.109237
5   real_net_monetary_index    1.066892
6           log_artifs_rate    1.041851
7           localities_rate    1.064153
8                      link    1.021617
9  detector_expensive_dummy    1.014608

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


model2_ROBUST = ols_regression_robust(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:         log_coins_rate   R-squared:                       0.164
Model:                            OLS   Adj. R-squared:                  0.162
Method:                 Least Squares   F-statistic:                     4.867
Date:                Thu, 13 Jul 2023   Prob (F-statistic):           1.73e-06
Time:                        17:55:04   Log-Likelihood:                 6444.2
No. Observations:                2767   AIC:                        -1.287e+04
Df Residuals:                    2757   BIC:                        -1.281e+04
Df Model:                           9
Covariance Type:                  HC1
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -0.0052      0.007     -0.695      0.487      -0.020       0.009
log_experience               0.0002      0.000      0.860      0.390      -0.000       0.001
log_contributions           -0.0005      0.001     -0.863      0.388      -0.002       0.001
log_comments                 0.0007      0.000      2.205      0.028    7.74e-05       0.001
log_coins                   -0.0006      0.001     -0.907      0.365      -0.002       0.001
real_net_monetary_index      0.0044      0.008      0.554      0.579      -0.011       0.020
log_artifs_rate              0.1747      0.049      3.591      0.000       0.079       0.270
localities_rate             -0.0157      0.025     -0.630      0.529      -0.065       0.033
link                         0.0053      0.005      1.072      0.284      -0.004       0.015
detector_expensive_dummy     0.0244      0.011      2.263      0.024       0.003       0.046
==============================================================================
Omnibus:                     4505.266   Durbin-Watson:                   2.016
Prob(Omnibus):                  0.000   Jarque-Bera (JB):          2816874.945
Skew:                          10.625   Prob(JB):                         0.00
Kurtosis:                     157.858   Cond. No.                         311.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(341.68761579326684, 3.638027939924491e-68, 43.15745344239691, 7.013041612406115e-73)

White's Test for Heteroskedasticity:
(945.1176396172448, 2.9148428248188333e-164, 27.07522270645819, 1.9928026388409667e-205)

Variance Inflation Factor (VIF):
                   Variable         VIF
0                     const  202.505982
1            log_experience    2.023773
2         log_contributions    1.360198
3              log_comments    2.482002
4                 log_coins    2.109237
5   real_net_monetary_index    1.066892
6           log_artifs_rate    1.041851
7           localities_rate    1.064153
8                      link    1.021617
9  detector_expensive_dummy    1.014608
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
model2_WLS = ols_regression_wls(df_log_2, 'log_coins_rate', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'])


'''
Regression Summary:
                            WLS Regression Results
==============================================================================
Dep. Variable:         log_coins_rate   R-squared:                       0.381
Model:                            WLS   Adj. R-squared:                  0.379
Method:                 Least Squares   F-statistic:                     188.2
Date:                Thu, 13 Jul 2023   Prob (F-statistic):          5.00e-279
Time:                        17:55:04   Log-Likelihood:                 19426.
No. Observations:                2767   AIC:                        -3.883e+04
Df Residuals:                    2757   BIC:                        -3.877e+04
Df Model:                           9
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                     7.649e-06   2.66e-05      0.287      0.774   -4.45e-05    5.98e-05
log_experience           -3.095e-07   1.07e-06     -0.290      0.772    -2.4e-06    1.78e-06
log_contributions         8.062e-07   2.77e-06      0.291      0.771   -4.63e-06    6.24e-06
log_comments              -1.03e-06   3.52e-06     -0.292      0.770   -7.94e-06    5.88e-06
log_coins                 8.929e-07   3.12e-06      0.286      0.775   -5.22e-06       7e-06
real_net_monetary_index  -6.501e-06   2.28e-05     -0.285      0.776   -5.12e-05    3.82e-05
log_artifs_rate              0.0995      0.003     35.481      0.000       0.094       0.105
localities_rate           2.295e-05   7.99e-05      0.287      0.774      -0.000       0.000
link                         0.0002      0.000      0.998      0.319      -0.000       0.000
detector_expensive_dummy     0.0134      0.001     19.072      0.000       0.012       0.015
==============================================================================
Omnibus:                     3046.844   Durbin-Watson:                   2.018
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           481178.810
Skew:                           5.285   Prob(JB):                         0.00
Kurtosis:                      66.733   Cond. No.                     1.14e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.14e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

Variance Inflation Factor (VIF):
                   Variable         VIF
0                     const  202.505982
1            log_experience    2.023773
2         log_contributions    1.360198
3              log_comments    2.482002
4                 log_coins    2.109237
5   real_net_monetary_index    1.066892
6           log_artifs_rate    1.041851
7           localities_rate    1.064153
8                      link    1.021617
9  detector_expensive_dummy    1.014608
#->>>>>>>>>>>>>>>>>>>This model has relatively large R2 0.966. This together with many variables significant  at 5% sign.level might...
# indicate over-fitting or some other issue. 
'''




#now LPM:
model2_LPM = ols_regression_robust(df_log_3, 'rate_coins_dummy', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'])
'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   R-squared:                       0.190
Model:                            OLS   Adj. R-squared:                  0.187
Method:                 Least Squares   F-statistic:                     8.435
Date:                Sat, 15 Jul 2023   Prob (F-statistic):           1.59e-12
Time:                        16:21:06   Log-Likelihood:                 1769.3
No. Observations:                2771   AIC:                            -3519.
Df Residuals:                    2761   BIC:                            -3459.
Df Model:                           9
Covariance Type:                  HC1
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -0.0399      0.033     -1.225      0.221      -0.104       0.024
log_experience               0.0008      0.001      0.505      0.613      -0.002       0.004
log_contributions            0.0137      0.006      2.115      0.035       0.001       0.026
log_comments                 0.0036      0.002      1.623      0.105      -0.001       0.008
log_coins                    0.0115      0.005      2.311      0.021       0.002       0.021
real_net_monetary_index      0.0094      0.033      0.283      0.777      -0.055       0.074
log_artifs_rate              0.9125      0.153      5.960      0.000       0.612       1.213
localities_rate              0.1048      0.147      0.714      0.475      -0.183       0.393
link                         0.0284      0.020      1.396      0.163      -0.011       0.068
detector_expensive_dummy     0.1053      0.041      2.567      0.010       0.025       0.186
==============================================================================
Omnibus:                     2894.038   Durbin-Watson:                   2.036
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           165692.576
Skew:                           5.244   Prob(JB):                         0.00
Kurtosis:                      39.402   Cond. No.                         312.
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity robust (HC1)

Breusch-Pagan Test for Heteroskedasticity:
(387.8098024653139, 5.457039037258278e-78, 49.92108037529656, 3.5690023155326827e-84)

White's Test for Heteroskedasticity:
(663.9002092405344, 5.081202112931881e-107, 16.46887033861199, 1.2611633308773446e-124)

Variance Inflation Factor (VIF):
                   Variable         VIF
0                     const  202.428240
1            log_experience    2.020913
2         log_contributions    1.364659
3              log_comments    2.484052
4                 log_coins    2.091897
5   real_net_monetary_index    1.066964
6           log_artifs_rate    1.044159
7           localities_rate    1.064463
8                      link    1.025671
9  detector_expensive_dummy    1.014114
'''


#>>>>>>>>>>now LOGIT:
from functions.V_fctn_LOGIT import logit_regression_roc_wald
model2_LOGIT = logit_regression_roc_wald(df_log_3, dependent_var='rate_coins_dummy', independent_vars=['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'],
                                     pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                     ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                     hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])



#HERE we MUST DELETE 'residence_additional_info' since it is almost perfectly predicted... there is a low number of dummy values - (we have values for all the municipalities thus there is almost no residence additional info)


'''
Optimization terminated successfully.
         Current function value: 0.062739
         Iterations 9
Logit Regression Summary:
                           Logit Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   No. Observations:                 2771
Model:                          Logit   Df Residuals:                     2761
Method:                           MLE   Df Model:                            9
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.3742
Time:                        17:55:17   Log-Likelihood:                -173.85
converged:                       True   LL-Null:                       -277.79
Covariance Type:            nonrobust   LLR p-value:                 7.344e-40
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -7.6755      2.202     -3.485      0.000     -11.992      -3.359
log_experience               0.0621      0.086      0.722      0.470      -0.107       0.231
log_contributions           -0.0253      0.151     -0.168      0.866      -0.321       0.270
log_comments                 0.4411      0.140      3.156      0.002       0.167       0.715
log_coins                    0.4013      0.176      2.274      0.023       0.055       0.747
real_net_monetary_index     -0.0216      2.190     -0.010      0.992      -4.313       4.270
log_artifs_rate             11.1976      1.275      8.785      0.000       8.699      13.696
localities_rate             10.4593      8.912      1.174      0.241      -7.009      27.927
link                        -0.0537      0.598     -0.090      0.928      -1.226       1.119
detector_expensive_dummy     2.1507      0.519      4.145      0.000       1.134       3.168
============================================================================================

Area Under the Curve (AUC): 0.9055579257650389
'''

#now PROBIT:
from functions.V_fctn_PROBIT import probit_regression_roc_wald


model2_PROBIT = probit_regression_roc_wald(df_log_3, 'rate_coins_dummy', ['log_experience', 'log_contributions', 
                                     'log_comments', 'log_coins',
                                     'real_net_monetary_index', 'log_artifs_rate', 'localities_rate','link', 'detector_expensive_dummy'],
                                     pev_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'], 
                                     ape_vars=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'],
                                     hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])


'''
Optimization terminated successfully.
         Current function value: 0.062980
         Iterations 9
Probit Regression Summary:
                          Probit Regression Results
==============================================================================
Dep. Variable:       rate_coins_dummy   No. Observations:                 2771
Model:                         Probit   Df Residuals:                     2761
Method:                           MLE   Df Model:                            9
Date:                Thu, 13 Jul 2023   Pseudo R-squ.:                  0.3718
Time:                        17:55:28   Log-Likelihood:                -174.52
converged:                       True   LL-Null:                       -277.79
Covariance Type:            nonrobust   LLR p-value:                 1.401e-39
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                       -3.7709      1.009     -3.738      0.000      -5.748      -1.794
log_experience               0.0271      0.038      0.720      0.472      -0.047       0.101
log_contributions           -0.0017      0.073     -0.023      0.982      -0.145       0.142
log_comments                 0.1938      0.064      3.006      0.003       0.067       0.320
log_coins                    0.1584      0.078      2.034      0.042       0.006       0.311
real_net_monetary_index      0.1808      1.001      0.181      0.857      -1.781       2.142
log_artifs_rate              5.4585      0.592      9.216      0.000       4.298       6.619
localities_rate              2.4676      4.085      0.604      0.546      -5.539      10.475
link                         0.0193      0.304      0.063      0.949      -0.576       0.614
detector_expensive_dummy     0.9749      0.266      3.664      0.000       0.453       1.496
============================================================================================

Area Under the Curve (AUC): 0.9092231315207695
'''

