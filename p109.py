import statistics
import random
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
data1=pd.read_csv('StudentsPerformance.csv')
listdata=data1['math_score'].tolist()
mean=statistics.mean(listdata)
median=statistics.median(listdata)
mode=statistics.mode(listdata)
deviation=statistics.stdev(listdata)
firstStandardDeviationStart,firstStandardDeviationEnd=mean-deviation,mean+deviation
secondStandardDeviationStart,secondStandardDeviationEnd=mean-(2*deviation),mean+(2*deviation)
thirdStandardDeviationStart,thirdStandardDeviationEnd=mean-(3*deviation),mean+(3*deviation)
data_within_1_std_deviation = [result for result in listdata if result > firstStandardDeviationStart and result < firstStandardDeviationEnd]
data_within_2_std_deviation = [result for result in listdata if result > secondStandardDeviationStart and result < secondStandardDeviationEnd]
data_within_3_std_deviation = [result for result in listdata if result > thirdStandardDeviationStart and result < thirdStandardDeviationEnd]
print(deviation,median,mode)
print("{}% of data lies within 1 standard deviation".format(len(data_within_1_std_deviation)*100.0/len(listdata)))
print("{}% of data lies within 2 standard deviation".format(len(data_within_2_std_deviation)*100.0/len(listdata)))
print("{}% of data lies within 3 standard deviation".format(len(data_within_3_std_deviation)*100.0/len(listdata)))
data1=ff.create_distplot([listdata],['Random Dice'],show_hist=False)
data1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
data1.add_trace(go.Scatter(x=[firstStandardDeviationStart,firstStandardDeviationStart],y=[0,0.17],mode='lines',name='First Standard Deviation'))
data1.add_trace(go.Scatter(x=[firstStandardDeviationEnd,firstStandardDeviationEnd],y=[0,0.17],mode='lines',name='First Standard Deviation'))
data1.show()