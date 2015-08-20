#encoding=utf-8
'''
* 本文件为配置文件，配置信息为日志记录信息，以及其他在自动化测试中的
* 可用信息。
* @author wangyukun
* @Email wangyukun-xy@360.cn airfer@126.com
'''
class qihooSetting:
	#一些初始化默认配置
	LOG_FILE=r"E:\Github\qihooPaySikuliAuto\log\\"
	USER_LOG=r"userlog.txt"
	SYSTEM_LOG=r"systemlog.txt"
	
	@staticmethod
	def init(Settings,Debug):
		Settings.UserLog=True
		Settings.UserLogPrefix="user"
		Settings.UserLogTime=True
		Debug.setUserLogFile(qihooSetting.LOG_FILE+qihooSetting.USER_LOG)
		
		#以下是系统日志的相关配置
		Settings.ActionLogs = True
		Settings.InfoLogs = True
		Settings.DebugLogs = False
		Settings.LogTime = False
		Debug.setLogFile(qihooSetting.LOG_FILE+qihooSetting.SYSTEM_LOG)
		
	@staticmethod
	def getLogFile():
		return LOG_FILE
		
	@staticmethod
	def setLogFile(logfile):
		LOG_FILE=logfile
	