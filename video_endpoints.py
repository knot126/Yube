import files
from template import Template

fake_db_entries = {
	"PROkfP3tpXrQrth_uZ0NQM0u": {
		"title": "Some viedeo :D",
		"date": "2022-06-10T13:10:03+00:00:00",
		"lower": "knot126",
		"name": "Knot",
		"info": "*This is the equal to* the description of a video!!!\n\nHas a lots of stuff!!!\n\nNihil dolor accusamus deserunt. Minima consequatur omnis minima deleniti temporibus. Alias sit repudiandae omnis et inventore soluta.\n\nIpsum doloribus quia neque. Reprehenderit incidunt exercitationem dolor ullam possimus. Perspiciatis est ut repudiandae eveniet. Neque cum qui voluptate non asperiores et dolor. Est et temporibus quo sapiente recusandae culpa officiis.\n\n _Aut facere enim qui. Neque dolor pariatur porro quia in nulla modi nisi. Occaecati animi laborum qui tenetur inventore iste consequatur. Et voluptatem exercitationem dolores. Quia dolores nesciunt voluptatibus ut nulla saepe quos aspernatur. Fuga laborum suscipit quod dolores qui velit._ \n\nIusto eum deserunt deleniti beatae debitis quia similique sunt. Reiciendis ut dicta minus dolorum laborum unde quidem exercitationem. `Itaque accusantium fuga doloribus.` Earum veritatis qui excepturi ut illum similique molestiae. Autem animi eius maxime voluptatem voluptas quae enim. Blanditiis consectetur et dolorem. Quae quis aut officia. Reprehenderit incidunt exercitationem dolor ullam possimus. Perspiciatis est ut repudiandae eveniet. Neque cum qui voluptate non asperiores et dolor. Est et temporibus quo sapiente recusandae culpa officiis.\n\nAut facere enim qui. Neque dolor pariatur porro quia in nulla modi nisi. Occaecati animi laborum qui tenetur inventore iste consequatur. Et voluptatem exercitationem dolores. Quia dolores nesciunt voluptatibus ut nulla saepe quos aspernatur.\n\n\tTesting tabs!",
	},
}

def watch(self, path, params):
	"""
	Handles watching videos
	"""
	
	video = fake_db_entries[params["video"]]
	
	t = Template("video.template")
	t.addVariable("video.title", video["title"])
	t.addVariable("video.date", video["date"])
	t.addFormattedVariable("video.info", video["info"])
	t.addVariable("channel.name", video["name"])
	t.addVariable("channel.lower", '@' + video["lower"])
	content = t.evaluate()
	length = len(content)
	
	# Send the response
	self.send_response(200, "OK")
	self.send_header("Content-Length", str(length))
	self.end_headers()
	self.wfile.write(content)
