#coding:utf-8
from util.operation_excel import OperationExcel
import data_config
from util.operation_json import OperetionJson
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
	#去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	def get_header_value(self):
		#api.at.top
		header = {
			# 'Accept': '*/*',
			'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMTgxMTk5MCwiZXhwIjoxNTYzMzQ3OTkwLCJuYmYiOjE1MzE4MTE5OTAsImp0aSI6ImFFRmgybk91UkhzbTZLWmIiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.B6SMVdEN0JpzOTZEH87C1MXf5LheHzTalYouY1KrTy8',
			# 'Content-Type': 'application/x-www-form-urlencoded'
		}
		return header
	#是否携带header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		# if header =='yes':
		# 	header=
		# else:
		# 	return None
		return header
	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if not data:
			return None
		return data
	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		if not row:
			return None
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		# if not request_data:
		# 	return None
		# else:
		return request_data
	#获取预期结果
	def get_expcet_data(self,row):
		col = int(data_config.get_expect())
		expect = self.opera_excel.get_cell_value(row,col)
		expect = expect.encode('utf-8')
		# print type(expect)
		if expect == '':
			return None
		return expect
	#写入数据
	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row,col,value)
	#获取caseid
	def get_number_id(self,row):
		col=int(data_config.get_id())
		ID=self.opera_excel.get_cell_value(row,col)
		return ID
if __name__ == '__main__':
	get_data=GetData()
	print get_data.get_expcet_data(1)