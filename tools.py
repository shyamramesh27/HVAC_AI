import pickle
def log_cont():
    f=open('logging.log','r')
    return f.read()

def load_model(result):
    Hl=pickle.load(open('heatload_model.pkl','rb'))
    y = str(round(Hl.predict(result), 2))
    CL=pickle.load(open('coolingload_model.pkl','rb'))
    y_2=str(round(CL.predict(result), 2))
    return y,y_2

def open_log():
    try:
        f= open('logging.log','r')
        data=f.readlines()
        flag=1

        return data,flag
    except:
        data='LOG FILE ERROR: Could not open the log file in the location'
        flag=0
        return data,flag