# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no=1
   def turn_off(self):
      self.is_on=False
   def turn_on(self):
      self.is_on=True
   def show_status (self):
      if self.is_on==True:
        status= 'ON'
        print(f'TV is {status} chanel {self.channel_no}')
      else:
         status="OF"
         print(f'TV is {status}')
   def set_channel(self,new_channel_no):
      self.channel_no=new_channel_no