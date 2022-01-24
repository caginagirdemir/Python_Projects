import smbus
import time
bus = smbus.SMBus(0)
address = 0x68


f = open('mpu2950_reg_init.txt',"w")

PWR_MGMT_1 = 0x6B
bus.write_byte_data(address, PWR_MGMT_1, 0x00)
#0x08 temp_dis
#0x80 device_reset
time.sleep(0.1)
var1=bus.read_byte_data(address, PWR_MGMT_1)
time.sleep(0.1)
f.write("Power Management : "+hex(var1)+'\n')


GYRO_CONFIG=0x1B
bus.write_byte_data(address, GYRO_CONFIG, 0x08) #500dps 500deg/s
#0x08 500dps
#0x10 1000dps
#0x18 2000dps
time.sleep(0.1)
var1=bus.read_byte_data(address, GYRO_CONFIG)
time.sleep(0.1)
f.write("GYRO_CONFIG(0x1B) : "+hex(var1)+'\n')

ACCEL_CONFIG=0x1C
bus.write_byte_data(address, ACCEL_CONFIG, 0x00) #500dps 4g
#0x00 2G
#0x08 4G
#0x10 8G
#0x18 16G
time.sleep(0.1)
var1=bus.read_byte_data(address, ACCEL_CONFIG)
time.sleep(0.1)
f.write("ACCEL_CONFIG(0x1C) : "+hex(var1)+'\n')

ACCEL_CONFIG_2=0x1D
bus.write_byte_data(address, ACCEL_CONFIG_2, 0x00) #SET ACCELEROMETER RATE TO 1KHZ AND BANDWIDTH TO 10.2HZ
time.sleep(0.1)
var1=bus.read_byte_data(address, ACCEL_CONFIG_2)
time.sleep(0.1)
f.write("DLPF FOR ACCEL ACCEL_CONFIG_2(0x1D) : "+hex(var1)+'\n')

DLPF_CFG=0x1A
bus.write_byte_data(address, DLPF_CFG, 0x01) 
time.sleep(0.1)
var1=bus.read_byte_data(address, DLPF_CFG) #SET GYRO RATE TO 1KHZ AND BANDWIDTH TO 102HZ
time.sleep(0.1)
f.write("DLPF FOR GYRO(0x1A) : "+hex(var1)+'\n')


SMPRT_DIV=0x19
bus.write_byte_data(address, SMPRT_DIV, 0x03)
time.sleep(0.1)
var1=bus.read_byte_data(address, SMPRT_DIV)
time.sleep(0.1)
f.write("SMPRT_DIV(0x19) : "+hex(var1)+'\n')


INT_PIN_CFG=0x37
#bus.write_byte_data(address, INT_PIN_CFG, 0x10) #INT is 50 microsecond pulse and any read to clear  
#time.sleep(0.1)
var1=bus.read_byte_data(address, INT_PIN_CFG)
time.sleep(0.1)
f.write("INT_PIN_CFG(0x37) : "+hex(var1)+'\n')

INT_ENABLE=0x38
bus.write_byte_data(address, INT_ENABLE, 0x01) #Enable data ready (bit 0) interrupt
time.sleep(0.1)
var1=bus.read_byte_data(address, INT_ENABLE)
time.sleep(0.1)
f.write("INT_ENABLE(0x38) : "+hex(var1)+'\n')

I2C_MASTER_CONTROL=0x24
var1=bus.read_byte_data(address, I2C_MASTER_CONTROL)
time.sleep(0.1)
f.write("I2C_MASTER_CONTROL(0x24) : "+hex(var1)+'\n')


# 
USER_CTRL=0x6A
bus.write_byte_data(address, USER_CTRL, 0x20) #enable i2c master mode
time.sleep(0.1)
var1=bus.read_byte_data(address, USER_CTRL)
time.sleep(0.1)
f.write("USER_CTRL(0x6A) : "+hex(var1)+'\n')
# 
I2C_MST_CTRL=0x24
bus.write_byte_data(address, I2C_MST_CTRL, 0x0D) #I2C configuration multi-master I2C 400KHz
time.sleep(0.1)
var1=bus.read_byte_data(address, I2C_MST_CTRL)
time.sleep(0.1)
f.write("I2C_MST_CTRL(0x24) : "+hex(var1)+'\n')
# 
I2C_MST_DELAY_CTRL=0x67
# bus.write_byte_data(address, I2C_MST_DELAY_CTRL, 0x81) #Use blocking data retreival and enable delay for mag sample rate mismatch
# time.sleep(0.1)
var1=bus.read_byte_data(address, I2C_MST_DELAY_CTRL)
time.sleep(0.1)
f.write("I2C_MST_DELAY_CTRL(0x67) : "+hex(var1)+'\n')
# 
I2C_SLV4_CTRL=0x34
# bus.write_byte_data(address, I2C_SLV4_CTRL, 0x01) #Delay mag data retrieval to once every other accel/gyro data sample
# time.sleep(0.1)
var1=bus.read_byte_data(address, I2C_SLV4_CTRL)
time.sleep(0.1)
f.write("I2C_SLV4_CTRL(0x34) : "+hex(var1)+'\n')
# 
# 
FIFO_EN=0x23
# bus.write_byte_data(address, FIFO_EN, 0x00)
# time.sleep(0.1)
var1=bus.read_byte_data(address, FIFO_EN)
time.sleep(0.1)
f.write("FIFO_EN(0x23) : "+hex(var1)+'\n')
# 

#*****************
# I2C_SLV0_ADDR=0x25
# bus.write_byte_data(address, I2C_SLV0_ADDR, 0x0C)
# time.sleep(0.1)
# 
# AK8963_CNTL2=0x0B #reset
# I2C_SLV0_REG=0x26
# bus.write_byte_data(address, I2C_SLV0_REG, AK8963_CNTL2)
# time.sleep(0.1)
# 
# I2C_SLV0_DO=0x63
# bus.write_byte_data(address, I2C_SLV0_DO, 0x01) #reset
# time.sleep(0.1)
# 
# I2C_SLV0_CTRL=0x27
# bus.write_byte_data(address, I2C_SLV0_CTRL, 0x81) #do it
# time.sleep(0.5)
#*****************

#*****************
I2C_SLV0_ADDR=0x25
bus.write_byte_data(address, I2C_SLV0_ADDR, 0x0C)
time.sleep(0.1)

AK8963_CNTL=0x0A #Power down (0000), single-measurement (0001), self-test (1000) and Fuse ROM (1111) modes on bits 3:0
I2C_SLV0_REG=0x26
bus.write_byte_data(address, I2C_SLV0_REG, AK8963_CNTL)
time.sleep(0.1)

I2C_SLV0_DO=0x63
bus.write_byte_data(address, I2C_SLV0_DO, 0x16) #0001 16bit 0110 continous measurement mode 2 100Hz  
time.sleep(0.1)

I2C_SLV0_CTRL=0x27
bus.write_byte_data(address, I2C_SLV0_CTRL, 0x81) #do it
time.sleep(0.5)
#*****************

#-------------

#*****************
I2C_SLV0_ADDR=0x25
bus.write_byte_data(address, I2C_SLV0_ADDR, 0x8C)
time.sleep(0.1)

AK8963_XOUT_L=0x03 
I2C_SLV0_REG=0x26
bus.write_byte_data(address, I2C_SLV0_REG, AK8963_XOUT_L)
time.sleep(0.1)

I2C_SLV0_DO=0x63
bus.write_byte_data(address, I2C_SLV0_DO, 0x00)   
time.sleep(0.1)

I2C_SLV0_CTRL=0x27
bus.write_byte_data(address, I2C_SLV0_CTRL, 0x87) #read 6 byte
time.sleep(0.5)
#*****************

#f.write("AK8963 Sens adjustment values \n")
# bus.write_byte_data(address, I2C_SLV0_ADDR, 0x8C)
# time.sleep(0.5)
# ASAX=0x10 #SENS ADJUSTMENT VALUES
# bus.write_byte_data(address, I2C_SLV0_REG, ASAX)
# time.sleep(0.5)
# bus.write_byte_data(address, I2C_SLV0_CTRL, 0x83)
# time.sleep(0.5)
# 
# EXT_SENS_DATA_00 = 0x49
# var1=bus.read_byte_data(address, EXT_SENS_DATA_00)
# time.sleep(0.1)
# f.write("ASA_X : "+hex(var1)+'\n')
# 
# EXT_SENS_DATA_01 = 0x4A
# var1=bus.read_byte_data(address, EXT_SENS_DATA_01)
# time.sleep(0.1)
# f.write("ASA_Y : "+hex(var1)+'\n')
# 
# EXT_SENS_DATA_02 = 0x4B
# var1=bus.read_byte_data(address, EXT_SENS_DATA_02)
# time.sleep(0.1)
# f.write("ASA_Z : "+hex(var1)+'\n')

f.close()



