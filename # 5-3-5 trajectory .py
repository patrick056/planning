# 5-3-5 trajectory 
 


import math
import datetime as datetime
import os 
import apscheduler.schedulers.background as BackgroundScheduler




def tarjectory():
     global tim
     t=datetime.now().time()
     print(t)
     if tim in range(0,0.25):
        q=q1+a1*tim+a2*(tim**2)+a3*(tim**3)+a4*(tim**4)+a5*(tim**5)
        botspeed=a1+a2*(tim)*2+3*a3*(tim**2)+a4*4*(tim**3)+a5*5*(tim**4)
        tim += 0.02
     elif tim in range (0.25,0.5)                                
        q=b+b1*tim+b2*(tim**2)+b3*(tim**3)
        botspeed=b1+b2*tim+b3*i*tim+b4*3*(tim**2)
        tim += 0.02
    elif tim in range (0.5,0.75)
        q=c+c1*tim+c2*(tim**2)+c3*(tim**3)+c4*(tim**4)+c5*(tim**5)
        botspeed=c1+c2*(tim)*2+c3*3*(tim**2)+c4*4*(tim**3)+c5*5*(tim**4)
        tim += 0.02
    print(botspeed)
    
 if __name__='__main__':

      sch=BackgroundScheduler():
      Q1,Q2=raw_input('enter initial and final angle').split()

      q1=Q1*3.14/180
      q2=Q2*3.14/180

    sch.add_job(lambda:calc_angle(t,pos),'interval',seconds = 0.02,id='job_id')
    
    if flag==0:
	    sch.start()

    while True:
	    
	    time.sleep(10)