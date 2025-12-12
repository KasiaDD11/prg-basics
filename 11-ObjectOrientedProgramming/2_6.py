class Phone():
        def __init__(self,marka,kolor):
            self.marka=marka
            self.kolor=kolor
            self.currant_page='home'
            self.on=True
        def change_currant_page(self,nowa):
              self.currant_page=nowa
        def display_page(self):
              print(self.currant_page)
        def turn_on(self):
              if self.on==True:
                    print('Already ON')
              else:
                    self_on=True


def main():
      tel=Phone('Apple','Blue')
      tel.change_currant_page('Insta')
      tel.change_currant_page('Facebook')
      tel.display_page()
      tel.turn_on()

if __name__=='__main__':
      main()