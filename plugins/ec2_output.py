from ansible import inventory

def human_log(self, res, host):
	inventory_manager = inventory.Inventory()
        result = inventory_manager.get_variables(host)
        print result['ec2_tag_Name']
 
class CallbackModule(object):
 
	def on_any(self, *args, **kwargs):
		pass

	def runner_on_ok(self, host, res):
		human_log(self, res, host)
