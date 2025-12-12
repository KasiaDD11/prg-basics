# tv_show.py file
# main program
import Telewizor

def main():
   # object creation
   tele=Telewizor.TV()

   # object usage
   tele.show_status()
   tele.turn_on()
   tele.show_status()
   tele.set_channel(6)
   tele.show_status()
   tele.turn_off()
   tele.show_status()

if __name__ == "__main__":
   main() 