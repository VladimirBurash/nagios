import ujson
from tornado import gen
from tornado.httpclient import HTTPRequest
from roboman.bot import BaseBot


class NagiosBot(BaseBot):
    bot_name = 'NagiosBot'
    bot_key = "270374055:AAEd6qibct5phm6B-6KO0J40MB-mMQuetYU"

    async def _on_hook(self, data):
        await self.chech_nagios()
        print("on hook")
        pass

    @gen.coroutine
    def get_state(self):
        req = HTTPRequest(
            'http://10.64.0.2:8080/state',
            method="GET"
        )

        res = yield self.client.fetch(req)
        data = ujson.loads(res.body)
        return data

    async def chech_nagios(self):
        dic = {}
        list_hosts = []
        req = await self.get_state()
        keys_host = req["content"].keys()
        for i in keys_host:
            list_services = []
            list_hosts.append(i)
            keys_services = req["content"][i]["services"].keys()
            for j in keys_services:
                list_services.append(j)
            dic[i] = list_services

        for i in list_hosts:
            for j in dic[i]:
                state = req["content"][i]["services"][j]["current_state"]
                if state == "2" or state == "1":
                    await self.send("Ошибка на сервере "+i+" \nСервис: "+j+"\nТекст ошибки: "+
                              req["content"][i]["services"][j]["plugin_output"])


