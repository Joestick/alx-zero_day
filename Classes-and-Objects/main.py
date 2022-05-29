class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = str(name)
        self.name = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

        print ("The following are the information of the new student")

    def change_name(self, new_name):
        self.name = new_name
        print("name", self.name)
    
    def change_age(Self, new_age):
        Self.age = new_age
        print("peter's age:",Self.age)

    def add_track(self,new_tracks):
        self.tracks.append(new_tracks)
        print("peter's tracks:",self)    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")


