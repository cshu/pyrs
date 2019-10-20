


def exec_loop(recv_func, send_func, context_obj):
	#last_received_data = None
	while True:
		result = recv_func()
		#print(type(result))
		if not result:
			break
		elif result['is_code']:
			exec(result['data'])#send_func can be called inside the evaluated code
		else:
			last_received_data = result['data']#the data can later be used in the exec

if __name__ == "__main__":
	test_data = [ {'is_code': True, 'data':'send_func(last_received_data+2)'},{'is_code': False, 'data' : 111}]
	def test_recv():
		return test_data.pop() if test_data else None
	def test_send(test_param):
		print(test_param)
	exec_loop(test_recv, test_send, None)
