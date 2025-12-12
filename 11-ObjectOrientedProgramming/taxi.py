class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare
        


def main():
    # your program
    taxi1=TaxiRide(3)
    taxi2=TaxiRide(5)
    rate1=taxi1.rate_per_km
    taxi1.distance=100
    fare1=taxi1.calculate_fare(taxi1.distance)
    print('----RECIPE----')
    print(f'Distance: {taxi1.distance}')
    print(f'Rate per km: {rate1} ')
    print(f'Fare: {fare1}')

    rate2=taxi2.rate_per_km
    taxi2.distance=1564
    fare2=taxi2.calculate_fare(taxi2.distance)
    print('----RECIPE----')
    print(f'Distance: {taxi2.distance}')
    print(f'Rate per km: {rate2} ')
    print(f'Fare: {fare2}')

    
    

if __name__ == "__main__":
    main()
