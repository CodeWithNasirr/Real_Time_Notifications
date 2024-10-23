from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
 

class MyConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_name="task_notifications"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            "message":"Connected To Task Notifications "
        }))



    def task_creations(self,event):
         data=json.loads(event['value'])
         self.send(text_data=json.dumps({
            'Message':"New task created!",
            "data":data
        }))
         
    def task_deadline(self,event):
        data=json.loads(event['value'])
        self.send(text_data=json.dumps({
            "Message":'Task deadline is near!',
            'data':data
        }))
         
    
    def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)
    



    def disconnect(self, code):
        return super().disconnect(code)
    