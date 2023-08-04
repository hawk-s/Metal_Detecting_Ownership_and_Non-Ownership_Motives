from functions.N_fctn_load_excel import load_excel_to_dataframe
from functions.Z_fctn_concat_df import concat_dataframes
import pandas as pd


df1 = load_excel_to_dataframe('artefakty_doba_bronzova.xlsx')
df2 = load_excel_to_dataframe('artefakty_doba_zelezna.xlsx')
df3 = load_excel_to_dataframe('artefakty_doba_rimska.xlsx')
df4 = load_excel_to_dataframe('artefakty_stehovani_narodu.xlsx')
df5 = load_excel_to_dataframe('artefakty_slovane.xlsx')
df6 = load_excel_to_dataframe('artefakty_rany_stredovek.xlsx')
df7 = load_excel_to_dataframe('artefakty_stredovek.xlsx')

df = concat_dataframes([df1,df2,df3,df4,df5,df6,df7])



from functions.B_fctn_rename_columns import rename_columns

df = rename_columns(df, {3:'profile'})
#print(df)
from functions.Z_fctn_merge_dfs import merge_dataframes
daf = load_excel_to_dataframe('P_FINAL_DATA.xlsx')
df_fin = merge_dataframes(df, daf, 'profile')

df_fin = rename_columns(df_fin, {'Unnamed: 0':'artif_name', 0:'likes', 1:'viewed', 2:'comments_under', 4:'photograph', 5:'uploaded', 6:'region_of_find', 7:'soil_state', 8:'depth_of_find', 9:'detector_used', 10: 'submitted_to'})



#extracting numbers from variables:
#*********************************************************************************
from functions.Z_fctn_extract_numbers import extract_numbers

df_fin = extract_numbers(df_fin, ['likes', 'viewed', 'comments_under', 'depth_of_find'])
#print(df)
#print(df_fin.columns)
from functions.B_fctn_drop_columns import drop_columns

df_fin = drop_columns(df_fin, ['area_municipality',
       'municipality_type', 'population_density','photograph',
       'region_of_find', 'soil_state', 'submitted_number_artifs','number_artifs','number_coins','submitted_number_coins','rate_artifs_dummy', 'rate_coins_dummy','uploaded_at_least_one_artif_or_coin_dummy'])
#***************************************************************************************




#creating the year variable:
#*************************************************************************************
from functions.Z_fctn_create_year_column import create_new_column

df_fin = create_new_column(df_fin, 'uploaded')



from functions.Z_fctn_assign_year_number import assign_year_numbers

df_fin = assign_year_numbers(df_fin, 'uploaded', 'uploaded_year')

#print(df_fin[['uploaded', 'uploaded_year']])
from functions.C_fctn_create_dummy import create_dummy_variable

df_fin = create_dummy_variable(df_fin, 'submitted_to', replace= False) #creation of the main dependent variable

#print(df_fin[['submitted_to', 'submitted_to_dummy']])
#********************************************************************************************





#searching for expensive detectors:
#**************************************************************************************************************
detectors_to_search = pd.DataFrame([
"Manticore",
"CTX 3030",
"GPX 5000",
"Excalibur II",
"Standard MP V2",
"Standard MP V3",
"Spectra V3i",
"GTI 2500",
"Axiom MS2",
"Axiom MS3",
"GPX 6000",
"GPZ 7000",
"SDC 2300",
"ATX",
"SSP-5100",
"UPEX ONE 2",
"GPX 4500",
"Invenio PRO"
])

'''Manticore, CTX 3030, GPX 5000, Excalibur II, Standard MP V2, Standard MP V3, Spectra V3i, GTI 2500, Axiom MS2, Axiom MS3,
GPX 6000, GPZ 7000, SDC 2300, ATX, SSP-5100, UPEX ONE 2, GPX 4500, Invenio PRO'''



#convert the above list to lower and without spaces:
from functions.A_fctn_replace_and_lowercase import replace_special_characters
from functions.E_fctn_remove_spaces import remove_spaces
#print(detectors_to_search)

detectors_to_search = replace_special_characters(detectors_to_search, 0)
#print(detectors_to_search)

detectors_to_search = remove_spaces(detectors_to_search, 0)
#print(detectors_to_search)
#data on metal detectors and their prices obtained from website lovecpokladu.cz and revisited on heureka.cz and via google search.

df_fin_copy = df_fin.copy()


#convert the dectors of people to lower and without spaces:
dfc = replace_special_characters(df_fin_copy, 'detector_used', new_column='detector_lower' )

#print(dfc['detektor_lower'])



dfc = remove_spaces(dfc, 'detector_lower')

#print(dfc['detector_lower'])



#create dummy whenever the detector is above 30k czk, i.e. above the average income at about the year 2018:
from functions.E_fctn_check_values_dummy import check_values

dfc = check_values(dfc, detectors_to_search, 'detector_lower', 'detector_exp_dummy')

print('++++++++++++++++++++++++++++++++++++++++++++++++++ ')
#print(dfc['detector_exp_dummy'])

from functions.E_fctn_display_unique_values import display_unique_values
display_unique_values_obj = display_unique_values(dfc, 'detector_exp_dummy')
#print(display_unique_values_obj)

#output:
'''
++++++++++++++++++++++++++++++++++++++++++++++++++ 
   Value  Count
0      0  12821
1      1    137

'''

#print(dfc)
#*********************************************************************************************************************************************************

df_fin['detector_exp_dummy'] = dfc['detector_exp_dummy']

df_fin['detector_expensive_dummy'] = df_fin['detector_exp_dummy'] + df_fin['detector_expensive_dummy']

df_fin = create_dummy_variable(df_fin, 'detector_expensive_dummy', 0) #creation of detector expensive dummy out of the original and newly matched expensive metal detectors!







from functions.P_fctn_fill_missing_values import fill_missing_values
df_fin = fill_missing_values(df_fin,{'real_net_monetary_index':1, 
                                           'average_age':42.4734915211329, 
                                           'localities_rate': 0.021478453745227236}) 




#********************************************ANALYSIS*****************************************************************************************************
from functions.Q_fctn_create_correlation_matrix import create_correlation_matrix

create_correlation_matrix(df_fin,['submitted_to_dummy','period','uploaded_year', 'likes', 'viewed','comments_under', 'depth_of_find', 'link',                                        
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
'localities_rate'],'Correlation Matrix Reduced - Ancient Artifacts')


#based on the corr matrix we drop the following variables:

df_fin = drop_columns(df_fin, ['depth_of_find',
       'coins', 'coins_rate',
       'men_proportion', '65+_proportion', 'detector_exp_dummy'])




from functions.Q_fction_get_summary_statistics import get_summary_statistics
from functions.Q_fction_get_summary_statistics import get_extended_summary_statistics
summary_reduced_1 = get_summary_statistics(df_fin)
print(summary_reduced_1 )

summary_reduced_1_ext = get_extended_summary_statistics(df_fin)
print(summary_reduced_1_ext)



#VARIABLES FOR MODELS:
#dep var:'submitted_to_dummy'
#indep vars:
'''
['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate']
'''




from functions.S_fctn_create_combined_hist import create_histograms_all
create_histograms_all(df_fin, ['period','uploaded_year', 'likes', 'viewed','comments_under',                                                                          
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                                                                           
'localities_rate'])


import numpy as np
df_log = df_fin.copy()
df_log['log_likes'] = np.log(df_log['likes'].values + 1)
df_log['log_viewed'] = np.log(df_log['viewed'].values + 1)
df_log['log_comments_under'] = np.log(df_log['comments_under'].values + 1)
df_log['log_experience'] = np.log(df_log['experience'].values + 1)
df_log['log_contributions'] = np.log(df_log['contributions'].values + 1)
df_log['log_comments'] = np.log(df_log['comments'].values + 1)
df_log['log_artifacts'] = np.log(df_log['artifacts'].values + 1)
df_log['log_artifs_rate'] = np.log(df_log['artifs_rate'].values + 1)



#LOG VARIABLES:
#'log_likes','log_viewed','log_comments_under','log_experience','log_contributions','log_comments','log_artifacts','log_artifs_rate'




from functions.S_fctn_create_combined_hist import create_log_transformed_histograms
create_log_transformed_histograms(df_log, ['likes', 'viewed','comments_under','experience',                                                                          
'contributions',
'comments',                                                                  
'artifacts',                                                                                    
'artifs_rate'])

#outliers:


from functions.W_fctn_print_top import print_top_observations
df_log_2 = df_log.copy()

df_log_2 = df_log_2[df_log_2['experience'] != 498425] #ok
df_log_2 = df_log_2[df_log_2['contributions'] != 1489] #ok
df_log_2 = df_log_2[df_log_2['comments'] != 24463] #ok
df_log_2 = df_log_2[df_log_2['artifacts'] != 3332] #ok



df_log_3 = df_log_2.copy()

print_top_observations(df_log_3, columns=['likes', 'viewed', 'comments_under','experience','contributions',               
'comments',                    
'artifacts'], num_observations=10)
#LIKES VIEWED AND COMMENTS_UNDER ARE OK CLOSE TO EACH OTHER





#SO WE TRY MODELS WITH (DF_LOG) AND WITHOUT (DF_LOG_3) THE POTENTIAL OUTLIERS... AND WITH AND WITHOUT LOGS

#*****#Finally Models:
from functions.V_fctn_OLS_ROBUST import ols_regression_robust
from functions.V_fct_OLS_REGRESSION import ols_regression
#now LPM:
'''
model2_LPM = ols_regression_robust(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''
'''
print('/WITHOUT OUTLIERS:/')
model2_LPM = ols_regression_robust(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''

#print('/WITH LOG VARIABLES:/')
model2_LPM = ols_regression_robust(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])

'''
model2_LPM = ols_regression(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''

'''
Regression Summary:
                            OLS Regression Results
==============================================================================
Dep. Variable:      rate_artifs_dummy   R-squared:                       0.151
Model:                            OLS   Adj. R-squared:                  0.149
Method:                 Least Squares   F-statistic:                     73.73
Date:                Thu, 13 Jul 2023   Prob (F-statistic):          1.75e-139
Time:                        13:06:59   Log-Likelihood:                 382.59
No. Observations:                4157   AIC:                            -743.2
Df Residuals:                    4146   BIC:                            -673.5
Df Model:                          10
Covariance Type:            nonrobust
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.0454      0.048     -0.937      0.349      -0.140       0.050
log_experience                0.0115      0.002      5.776      0.000       0.008       0.015
log_contributions             0.0159      0.006      2.714      0.007       0.004       0.027
log_comments                  0.0070      0.003      2.067      0.039       0.000       0.014
log_artifacts                 0.0324      0.004      8.039      0.000       0.024       0.040
real_net_monetary_index      -0.0047      0.049     -0.095      0.924      -0.101       0.091
log_coins_rate                1.4684      0.115     12.718      0.000       1.242       1.695
localities_rate               0.3139      0.202      1.554      0.120      -0.082       0.710
link                          0.0273      0.021      1.305      0.192      -0.014       0.068
residence_additional_info     0.0113      0.038      0.296      0.767      -0.063       0.086
detector_expensive_dummy      0.0288      0.027      1.079      0.281      -0.024       0.081
==============================================================================
Omnibus:                     2633.902   Durbin-Watson:                   2.015
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            23765.645
Skew:                           3.027   Prob(JB):                         0.00
Kurtosis:                      13.028   Cond. No.                         278.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Breusch-Pagan Test for Heteroskedasticity:
(465.8956625389168, 8.479203157342855e-94, 52.33131443298611, 1.1940961249430637e-99)

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

Hausman Test for Endogeneity:
None

'''


#>>>>>>>>>>now LOGIT:

from functions.V_fctn_LOGIT import logit_regression_roc_wald
'''
model2_LOGIT = logit_regression_roc(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''
'''
print('/WITHOUT OUTLIERS:/')
model2_LOGIT = logit_regression_roc(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions',
'comments',                                                                  
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''

#print('/WITH LOG VARIABLES:/')
model2_LOGIT = logit_regression_roc_wald(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'], hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])

'''
model2_LOGIT = logit_regression_roc(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''



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

'''
model2_PROBIT = probit_regression_roc(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                                  
'contributions', 
'comments',                                                                 
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''
'''
print('/WITHOUT OUTLIERS:/')
model2_PROBIT = probit_regression_roc(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'likes', 'viewed','comments_under', 'link',                                        
'experience',                
'contributions', 
'comments',                                                                     
'artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''

#print('/WITH LOG VARIABLES:/')
model2_PROBIT = probit_regression_roc_wald(df_log_3, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'],
hypotheses_variables=['real_net_monetary_index', 'detector_expensive_dummy', 'localities_rate'])
'''
model2_PROBIT = probit_regression_roc(df_log, 'submitted_to_dummy', ['period','uploaded_year', 'log_likes', 'log_viewed','log_comments_under', 'link',                                        
'log_experience',                                  
'log_contributions',
'log_comments',                                                                  
'log_artifacts',                                                                       
'residence_additional_info','real_net_monetary_index',                     
'log_artifs_rate',                                                               
'average_age',                                                               
'detector_expensive_dummy',                                            
'localities_rate'])
'''


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



model_simple = ols_regression_robust(df_log_3, 'detector_expensive_dummy', ['experience', 'contributions', 'real_net_monetary_index'])

model_simple2 = probit_regression_roc_wald(df_log_3, 'detector_expensive_dummy', ['experience', 'contributions', 'real_net_monetary_index'])
