from biogeme import *
from headers import *
from nested import *
from loglikelihood import *
from statistics import *
#import random


cons_work= Beta('cons for work', 0,-10,10,0)
cons_edu = Beta('cons for education',0,-50,10,0)
cons_shopping = Beta('cons for shopping',0,-10,10,0)
cons_other=Beta('cons for other',0,-10,10,0)
cons_Q = Beta('cons for quit',0,-10,10,1)

beta_first_work = Beta('beta for first work tour dummy for the person',0,-10,10,0)
beta_2plus_work = Beta('beta for 2+ work tours dummy for the person',0,-10,10,0)
beta_not_usual = Beta('beta for the location is not primary work location dummy',0,-10,10,0)
beta_no_car= Beta('No car is available in household',0,-10,10,0)

beta_female_work = Beta('female dummy for work',0,-10,10,0)
beta_female_edu = Beta('female dummy for edu',0,-10,10,1)
beta_female_shopping = Beta('female dummy for shopping',0,-10,10,1)
beta_female_other = Beta('female dummy for other',0,-10,10,0)

beta_PT_shopping = Beta('PT dummy for shopping',0,-10,10,1)

MU1 = Beta('MU for non-quit nest',1,1,100,0)
MU2 = Beta('MU for quit nest', 1,1,100,1)

first_work_dummy=1*(first_of_multiple==1)
sub_work_dummy=1*(subsequent_of_multiple==1)
not_usual_dummy=1-go_to_primary_work_location
no_car_dummy=1*(zero_car==0)

PT_dummy=1*(choice_new==1 or choice_new==2)

#V for work
V_work= cons_work + beta_female_work * Female_dummy
#V for education
V_edu = cons_edu + beta_female_edu * Female_dummy
#V for shopping
V_shopping = cons_shopping + beta_female_shopping * Female_dummy + beta_PT_shopping * PT_dummy
#V for other
V_other=cons_other + beta_female_other * Female_dummy
#V for quit
V_quit= cons_Q + beta_first_work * first_work_dummy + beta_2plus_work * sub_work_dummy + beta_not_usual*not_usual_dummy + beta_no_car *no_car_dummy

a=motor_avail_dummy_all
V = {1:V_work,2: V_edu,3:V_shopping,4:V_other,5:V_quit}
av= {1:a,2:a,3:a,4:a,5:a}

nonquit = MU1,[1,2,3,4]
quit =  MU2,[5] 
nests=nonquit,quit
prob = nested(V,av,nests,subtour_choice_4)
#prob = bioLogit(V,av,subtour_choice)
rowIterator('obsIter') 
BIOGEME_OBJECT.ESTIMATE = Sum(log(prob),'obsIter')

exclude = ((choice==0)+(PrimaryActivityIndex not in [1,2])+(IncomeIndex==12)) > 0

BIOGEME_OBJECT.EXCLUDE = exclude
nullLoglikelihood(av,'obsIter')
choiceSet = [1,2,3,4,5]
cteLoglikelihood(choiceSet,subtour_choice_4,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"
BIOGEME_OBJECT.PARAMETERS['checkDerivatives'] = "1"
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = "4"
