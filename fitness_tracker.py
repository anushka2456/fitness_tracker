#Defining a class for exercise
#The __init__ method in Python is a special method used to initialize objects of a class.
#In Python, the def keyword is used to define a function.
class Exercise:
    def_init_(self,name,duration_min,intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity


#Define class for user
        class User:
            def_init_(self,username):
                self.username = username
                self.exercise = []
                self.goals = {}

def log_exercise(self,exercise):
    self.exercises.append(exercise)
#In Python, the append() method is used to add a single element to the end of a list. 

def calculate_calories_burned(self):
    total_calories = 0
    for exercise in self.exercises:
        calories = exercise.duration_min*exercise.intensity
        total_calories = calories
        return total_calories

def set_goal(self,goal_type,target_value):
    self.goals[goal_type] = tartget_value

def track_progress(self):

    total_calories_burned = self.calculate_calories_burned()
    if 'calories' in self goals:
        goal_calories = self.goals['calories']
        progress_percentage = (total_calories_burned/goal_calories)*100
        return progress_percentage
else:
    return None

#Function to log an exercise
def log_exercise(user):
    name = input("Enter exercise name:")
    duration = int(input("Enter duration (minutes):"))
    intensity = int(input("Enter intensity (1-10): "))
    exercise = Exercise(name,duration,intensity)
    user.log_exercise(exercise)
    print("Exercise logged Successfully!")

#Function to set a goal
def set_goal(user):
    goal_type = input("Enter goal type (e.g., calories):")
    target_value = int(input("Enter target value:"))
    user.set_goal(goal_type,target value)
    print("Goal set succesfully!")

#Function to track progress
def track_progress(user):
    progress = user.track_progress()
    if progress is not None:
        print(f"Progress towards goal: {progress:.2f)%")
    else:
        print("No goal set yet.")

#Main function for user interaction
        def main():
            username = input("Enter your username:")
            user = user(username)
while True:
    print("\n---Fitness Tracking System---")
    print("1.Log Exercise")
    print("2. Set Goal")
    print("3.Track Progress")
    print("4.Exit")

    choice = input("Enter your choice (1-4):")
    if choice =="1":
        log_exercise(user)
    elif choice =="2":
        set_goal(user)
    elif choice == "3":
        track_progress(user)
    elif choice == "4":
        print("Existing...")
    break

   else:
       print("Invalid choice. Please enter a nimber between 1 and 4.")

if_name_=="main_":
    main()
       


        
            

    
    
