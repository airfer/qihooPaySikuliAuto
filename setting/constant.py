'''
* 本文件用于存放常量信息
* @author wangyukun-xy
* @email wangyukun-xy@360.cn
'''
class qihooConstant:

	TAG="""
	------------------------------------------------------------------------
	* The testting framwork was develped based on sikuli.Now it is used for 
	* qihoo360 pay auto testting.The information of author can be found as 
	* following.
	* @author Airong's home wangyukun
	* @email wangyukun-xy@360.cn
	------------------------------------------------------------------------
	"""
	
	RECHARGE_RESULT="""
	1、The amount of recharge is 11 yuan
	2、The begin.png in the result folder is the init state of the app
	3、The end.png in the result folder is the final state of the app

    result check:
		if difference of cash balance betweent the two picture is 11yuan,the 
		result indicates success,or fail!
	"""
	
	WITHDRAW_RESULT="""
	1、The amount of recharge is 11 yuan
	2、The begin.png in the result folder is the init state of the app
	3、The end.png in the result folder is the final state of the app

    result check:
		if difference of cash balance betweent the two picture is 11yuan,the 
		result indicates success,or fail!
	"""
	
	CHANGE_PASSWORD_RESULT="""
	1、The orignal password is 147258, if the password is changed ,the new password
	   is 147369.
	2、In order to make the following test normal, the new password will be changed
	   to 147258 after the testcase finish.
	"""
	
	RECHARGE_RESULT_PATH=r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\\"
	
	WITHDRAW_RESULT_PATH=r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\\"
	
	CHANGE_PASSWORD_RESULT_PATH=r"E:\Github\qihooPaySikuliAuto\data\ChangePassword\result\\"
