users = []
# rides = []
requests = []


class User:
    def __init__(self, fname, lname,email,password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def add(self):
        users.append(self)

        for user in users:
            print(self.serialize(user))
    
    def serialize(self, user):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "password": self.password
        }

class Ride:
    rides = []
    #ride_id = 1
    def __init__(self, driver=None, start_loc=None, end_loc=None,departure_time=None, date=None, route=None, cost=None):
        self.driver = driver
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.departure_time = departure_time
        self.date = date
        self.route = route
        self.cost = cost
        #self.id = Ride.ride_id
        self.id =len(Ride.rides)+1
        #Ride.ride_id +=1
        

    def add(self, driver, start_loc, end_loc, departure_time, date, route, cost, id):
        ride = {
            "driver": driver,
            "start_loc": start_loc,
            "end_loc": end_loc,
            "departure_time": departure_time,
            "date": date,
            "route": route,
            "cost": cost,
            "id":id

        }
        Ride.rides.append(ride)
        

    def get_all(self): #get all rides
        return Ride.rides

    def get_one(self, id): #get a single ride
        for ride in Ride.rides:
            if ride['id'] == int(id): 
                
                return ride
        return None



    def delete(self, ride_id):
        ride = self.get_one(ride_id) #Select a ride using an ID
        if ride: #Check if the ride is available
            Ride.rides.remove(ride) #delete it from the list
            return True 
        return False

class Request:
    request_id = 1
    def __init__(self, pickup_loc=None, status = None, ride =None):
        self.pickup_loc = pickup_loc
        self.status = status
        self.ride = ride
        self.id = Request.request_id

        Request.request_id +=1

    def add(self): #add the request
        requests.append(self)

    
    def get_all_requests(self, id ): #Retrieve all requests
        _requests = []
        for request in requests:
            if request.ride.id == id:
                 _requests.append(request.serialize())
        return _requests

    
    def serialize(self):
        return {
            "pickup_loc": self.pickup_loc,
            "status" : self.status, 
            'ride': self.ride.serialize(),
            "id" :self.id

        }

    def get_one_request(self, ride_id, request_id):
        for request in requests:
            if request.id == request_id and request.ride.id == ride_id: 
                return request
        return None

# print (rides)
# print (requests)