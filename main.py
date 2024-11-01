import logging
import numpy as np
import sys
import multidict
logging.basicConfig(filename='logging.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

clog=logging.StreamHandler(sys.stderr)
formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
clog.setFormatter(formatter)
clog.setLevel(logging.INFO)
l= ([('relative_compactness', '33'), ('surface_area', '55'), ('wall_area', '42'), ('roof_area', '38'), ('overall_height', '52'), ('orientation', '14'), ('glazing_area', '4'), ('glazing_area_distribution', '47')])



def getvalues(result):
    input = []
    result=list(result.items())
    print(result,file=sys.stderr)
    flag = 1
    logging.info("starting data validation...")
    for i in result:

        if(i==''):
            ans='missing value {}'.format(i[0])
            logging.error(ans)
            flag=0
        try:
            x = float(i[1])

            if(x<=0):
                ans='Value of {} cannot be negative or zero'.format(i[0])
                logging.error(ans)
                flag=0
            if(x>10000):
                ans="value of {} is found to be too high".format(i[0])
                logging.warning(ans)

        except:
            ans = "Unknown datatype exception at {} ".format(i[0])
            logging.error(ans)
            logging.critical("Process terminated due to occurrence of exception")
            flag=0
            return ans, flag

        if(flag):
            input.append(x)

    if flag:
        logging.info("Input datas are validated")
        input_arr = np.array(input)
        return input_arr,flag
    logging.critical("Process terminated due to occurrence of error")
    return ans,flag

