import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random

dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
standered_deviasion = st.stdev(dice_result)
median = st.median(dice_result)
mode = st.mode(dice_result)

first_standered_deviasion_start,first_standered_deviasion_end = mean - standered_deviasion, mean + standered_deviasion
second_standered_deviasion_start,second_standered_deviasion_end = mean - (2*standered_deviasion), mean + (2*standered_deviasion)
third_standered_deviasion_start,third_standered_deviasion_end = mean - (3*standered_deviasion), mean + (3*standered_deviasion)

fig = ff.create_distplot([dice_result],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,5],mode = "curveline",name = "Mean"))
fig.add_trace(go.Scatter(x=[first_standered_deviasion_start,first_standered_deviasion_start],y=[0,5],mode = "curveline",name = "standered_deviation_1"))
fig.add_trace(go.Scatter(x=[first_standered_deviasion_end,first_standered_deviasion_end],y=[0,5],mode = "curvelines",name = "standered_deviation_1"))
fig.add_trace(go.Scatter(x=[second_standered_deviasion_start,second_standered_deviasion_start],y=[0,5],mode = "curvelines",name = "standered_deviation_2"))
fig.add_trace(go.Scatter(x=[second_standered_deviasion_end,second_standered_deviasion_end],y=[0,5],mode = "curvelines",name = "standered_deviation_2"))
fig.show()
