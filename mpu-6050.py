import smbus
import math
from time import sleep


class MPU6050:

	DEV_ADDR = 0x68

	ACCEL_XOUT = 0x3b
	ACCEL_YOUT = 0x3d
	ACCEL_ZOUT = 0x3f
	TEMP_OUT = 0x41
	GYRO_XOUT = 0x43
	GYRO_YOUT = 0x45
	GYRO_ZOUT = 0x47
	PWR_MGMT_1 = 0x6b
	PWR_MGMT_2 = 0x6c

	def __init__(self):
		bus = smbus.SMBus(1)
		bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)
#		bus.write_byte_data(DEV_ADDR, 0x1a, 5)


	def read_byte(self, adr):
		return bus.read_byte_data(DEV_ADDR, adr)

	def __read_word(self, adr):
		high = bus.read_byte_data(DEV_ADDR, adr)
		low = bus.read_byte_data(DEV_ADDR, adr+1)
		val = (high << 8) + low
		return val

	def __read_word_sensor(self, adr):
		val = __read_word(adr)
		if (val >= 0x8000):
			return -((65535 -val) + 1)
		else:
			return val


	def get_temp(self):
		temp = __read_word_sensor(TEMP_OUT)
		x = temp / 340 + 36.53
		return x


	def get_gyro_data_lsb(self):
		x = __read_word_sensor(GYRO_XOUT)
		y = __read_word_sensor(GYRO_YOUT)
		z = __read_word_sensor(GYRO_ZOUT)
		return [x, y, z]

	def get_gyro_data_deg(self):
		x,y,z = get_gyro_data_lsb()
		x = x / 131.0
		y = y / 131.0
		z = z / 131.0
		return [x, y, z]


	def get_accel_data_lsb(self):
		x = __read_word_sensor(ACCEL_XOUT)
		y = __read_word_sensor(ACCEL_YOUT)
		z = __read_word_sensor(ACCEL_ZOUT)
		return [x, y, z]

	def get_accel_data_g(self):
		x,y,z = get_accel_data_lsb()
		x = x / 16384.0
		y = y / 16384.0
		z = z / 16384.0
		return [x, y, z]

	def calc_slope_for_accel_1axis(self, x, y, z):
		if x > 1: x = 1
		elif x < -1: x = -1
		slope_x = math.asin(x / 1)

		if y > 1: y = 1
		elif y < -1: y = -1
		slope_y = math.asin(y / 1)

		if z > 1: z = 1
		elif z < -1: z = -1
		slope_z = math.asin(z / 1)
		return [slope_x, slope_y, slope_z]

	def calc_slope_for_accel_2axis_deg(self, x,y,z):
		slope_xy = math.atan(x / y)
		deg_xy = math.degrees(slope_xy)

		if x > 0 and y > 0:
			deg_xy = deg_xy
		if x > 0 and y < 0:
			deg_xy += 180.0
		if x < 0 and y < 0:
			deg_xy -= 180.0
		if x < 0 and y > 0:
			deg_xy = deg_xy
		return deg_xy

	def calc_slope_for_accel_3axis_deg(self, x, y, z):
		theta = math.atan( x / math.sqrt(y*y + z*z))
		psi = math.atan(y / math.sqrt(x*x + z*z))
		phi = math.atan(math.sqrt(x*x + y*y) / z)

		deg_theta = math.degrees(theta)
		deg_psi = math.degrees(psi)
		deg_phi = math.degrees(phi)
		return [deg_theta, deg_psi, deg_phi]


while True:
#	temp = get_temp()
#	print 'temperature[degrees C]:',
#	print '%04.1f' % temp,
#	print '||',
#	gyro_x, gyro_y, gyro_z = get_gyro_data_deg()
#	print'gyro[deg/s]',
#	print 'x: %08.3f' % gyro_x,
#	print 'y: %08.3f' % gyro_y,
#	print 'z: %08.3f' % gyro_z,
#	print '||',
#	accel_x, accel_y, accel_z = get_accel_data_g()
#	print 'accel[g]',
#	print 'x: %06.3f' % accel_x,
#	print 'y: %06.3f' % accel_y,
#	print 'z: %06.3f' % accel_z,
#
#	print
#
#	sleep(1)
	mpu = MPU6050()
	accel_x1,accel_y1,accel_z1 = mpu.get_accel_data_g()
	slope_x1,slope_y1,slope_z1 = mpu.calc_slope_for_accel_1axis(accel_x1,accel_y1, accel_z1)
	slope_x1 = math.degrees(slope_x1)
	slope_y1 = math.degrees(slope_y1)
	slope_z1 = math.degrees(slope_z1)
	print 'katamuki[sita]',
	print 'x: %06.3f' % slope_x1,
	print 'y: %06.3f' % slope_y1,
	print 'z: %06.3f' % slope_z1,
	accel_x2,accel_y2,accel_z2 = mpu.get_accel_data_g()
	slope_xy = mpu.calc_slope_for_accel_2axis_deg(accel_x2, accel_y2, accel_z2)
	print 'katamuki[sita]',
	print 'xy: %06.3f' % slope_xy,
	accel_x3, accel_y3, accel_z3 = mpu.get_accel_data_g()
	theta,psi,phi = mpu.calc_slope_for_accel_3axis_deg(accel_x3, accel_y3, accel_z3)
	print 'sita=%06.3f' % theta,
	print 'psi =%06.3f' % psi,
	print 'phi =%06.3f' % phi,
	print
	
	sleep(0.1)
