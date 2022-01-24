import timeit
import time
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

import smbus
import math
#from datetime import datetime
bus = smbus.SMBus(0) 

address = 0x68 #I2C device MPU6050
PWR_MGMT_1 = 0x6B

ScaleFactor_A=float(8192)
ScaleFactor_G=float(32.8)



def read_raw_data(addr):
	high=bus.read_byte_data(address,addr)
	low=bus.read_byte_data(address,addr+1)

	value=((high << 8) | low)

	if(value > 32768):
		value=value - 65536
	return value


print("Enter file name:")
filename=raw_input()

led_inaction=port.PG6
led_inaction_ir=port.PG7
led_standy=connector.LEDp2
gpio.init()
gpio.setcfg(led_inaction, gpio.OUTPUT)
gpio.setcfg(led_inaction_ir, gpio.OUTPUT)
gpio.setcfg(led_standy, gpio.OUTPUT)
ACCEL_XOUT_H=0x3B

#t_end = time.time() + 60(saniye)*1(dakika katsayisi)



try:

    gpio.output(led_standy,0)
    gpio.output(led_inaction,0)
    gpio.output(led_inaction_ir,0)
    
    Sample=0
    f = open(filename+'.txt',"w")
    bus.write_byte_data(address, PWR_MGMT_1, 0x01)
    time.sleep(0.5)
    

    start_time = timeit.default_timer()
    gpio.output(led_inaction,1)
    gpio.output(led_inaction_ir,1)
    while True:
        sensor_data = []
        result = bus.read_i2c_block_data(address, ACCEL_XOUT_H, 20)
        for jj in range(0, 14, 2):
            hibyte = result[jj]
            hibyte = hibyte - 256 if hibyte > 127 else hibyte
            lobyte = result[jj + 1]
            sensor_data.append((hibyte << 8) + lobyte)
            #print(jj)
            
                
        for ii in range(14, 20, 2):
            lowbyte = result[ii]
            highbyte = result[ii + 1]
            highbyte = highbyte - 256 if highbyte > 127 else highbyte
            sensor_data.append((highbyte << 8) | lowbyte)
            #print(ii)
                
        
        ax="%.2f" %(sensor_data[0]/ScaleFactor_A)
        ay="%.2f" %(sensor_data[1]/ScaleFactor_A)
        az="%.2f" %(sensor_data[2]/ScaleFactor_A)
        gx="%.2f" %(sensor_data[4]/ScaleFactor_G)
        gy="%.2f" %(sensor_data[5]/ScaleFactor_G)
        gz="%.2f" %(sensor_data[6]/ScaleFactor_G)
        
        #SCALE FACTOR 0.15 FOR 16BITS
        #SENSOR_DATA*ASAX*SCALE
        
        mx=sensor_data[7]
        my=sensor_data[8]
        mz=sensor_data[9]
        
        ASA_X=((178.00-128.00)/256.00)+1.00 
        ASA_Y=((180.00-128.00)/256.00)+1.00
        ASA_Z=((169.00-128.00)/256.00)+1.00
        
        mx=mx*ASA_X
        mx=mx*0.15
        mx="%.2f" %(mx)
        
        my=my*ASA_Y
        my=my*0.15
        my="%.2f" %(my)
        
        mz=mz*ASA_Z
        mz=mz*0.15
        mz="%.2f" %(mz)
        #print(ax+","+ay+","+az+","+gx+","+gy+","+gz+","+mx+","+my+","+mz+"\n");
        f.write(ax+","+ay+","+az+","+gx+","+gy+","+gz+","+mx+","+my+","+mz+"\n");

        #f.write(ax+","+ay+","+az+","+gx+","+gy+","+gz+"\n");
        Sample=Sample+1
except KeyboardInterrupt:
	print("Aborted") 


gpio.output(led_inaction,0)
gpio.output(led_inaction_ir,0)
elapsed = timeit.default_timer() - start_time

print("Sample Number : "+str(Sample)+";Time Elapsed : "+str(elapsed)+";Hertz : "+str(Sample/elapsed)+"\n")
f.write("Sample Number : "+str(Sample)+";Time Elapsed : "+str(elapsed)+";Hertz : "+str(Sample/elapsed)+"\n")
f.close()