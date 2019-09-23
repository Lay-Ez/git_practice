import csv
import time
from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

#main body

landmark_string = ''

for letter, place in landmark_choices.items():
    landmark_string += "{} - {}\n".format(letter, place)

stations_under_construction = []

with open('under_construction.csv', 'r') as under_construction:
    csv_reader = csv.reader(under_construction)
    next(csv_reader)
    for line in csv_reader:
        stations_under_construction.extend(line)

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks.\n{}".format(landmark_string))

def skyroute():
    if user_or_worker() == 'u':
        greet()
        new_route()
    else:
        for_workers()
    goodbye()

def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()

def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()

def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            time.sleep(0.5)
            print("Oops that isn't 'o', 'd' or 'b'...\n")
            return set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
    if start_point != end_point:
        return start_point, end_point
    else:
        time.sleep(0.5)
        print("You entered the same place for your start and destination. Let's try again")
        return set_start_and_end(start_point, end_point)

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    if shortest_route:
        time.sleep(0.5)
        shortest_route_string = "\n".join(shortest_route)
        print("\nThe shortest route from {0} to {1} is:\n{2}\n".format(start_point, end_point, shortest_route_string))
    else:
        time.sleep(0.5)
        print("\nUnfortunately, there is currently no path between {0} and {1} due to maintenance".format(start_point, end_point))

    if one_more():
        show_landmarks()
        new_route(start_point, end_point)
    else:
        return

def one_more():
    again = input("Would you like to see another route? Enter y/n: ")
    if again == 'y':
        return True
    elif again == 'n':
        return False
    else:
        time.sleep(0.5)
        print("Sorry, that's not 'y' or 'n'. Let's try again")
        return one_more()

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == 'y':
        print(landmark_string)
    elif see_landmarks == 'n':
        return
    else:
        time.sleep(0.5)
        print("Sorry, this isn't 'y' or 'n'. Let's try again")
        return show_landmarks()

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []

    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro

            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)

                if not possible_route:
                    return None

            route = bfs(metro_system, start_station, end_station)

            if route is not None:
                routes.append(route)

    shortest_route = min(routes, key=len)
    return shortest_route

def goodbye():
    time.sleep(0.5)
    print("\n\n---Thank you for using SkyRoute!---")

def get_active_stations():
    updated_metro = vc_metro

    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():

            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)

            else:
                updated_metro[current_station] = set([])

    return updated_metro

def user_or_worker():
    user = input("Are you a user or worker? Enter 'u' for user, or 'w' for worker\n")
    if user == 'u':
        return 'u'
    elif user == 'w':
        return 'w'
    else:
        print("Sorry, that's not 'u' or 'w', let's try again")
        return user_or_worker()

def for_workers():
    def get_input():
        work_input = input("""\n--Enter 'list' to see the current list of stations under maintenance.
--Enter 'add' to add station to list of stations under maintenance.
--Enter 'rem' to remove the station from the maintenance list.
--Enter 'all' to see list of all stations in metro system with connected stations.
--Enter 'quit' to quit the system.\n""")
        if work_input == 'list':
            return 'list'
        elif work_input == 'add':
            return 'add'
        elif work_input == 'rem':
            return 'rem'
        elif work_input == 'all':
            return 'all'
        elif work_input == 'quit':
            return 'quit'
        else:
            print("Sorry, looks like you entered invalid input. Let's try again\n")
            return get_input()


    option = get_input()

    if option == 'add':
        station_to_add = input('Enter full name of the station\n')
        if station_to_add in vc_metro:
            print("Station {} added to the list of station under construction!\n".format(station_to_add))
            stations_under_construction.append(station_to_add)
        else:
            print("Sorry, there's no such station in the system\n")
        for_workers()

    elif option == 'all':
        for station, neighbor in vc_metro.items():
            print("{} - {}".format(station, neighbor))
        for_workers()

    elif option == 'rem':
        def remove_station():
            station_to_remove = input("Enter the full name of the station to remove\n")
            if station_to_remove in stations_under_construction:
                print("Station {} removed from the list of stations under construction!\n".format(station_to_remove))
                stations_under_construction.remove(station_to_remove)
                for_workers()
            else:
                print("Sorry, looks like you entered something wrong. Let's try again\n")
                remove_station()
        remove_station()

    elif option == 'list':
        print("Here's the list of stations under construction\n")
        print(stations_under_construction)
        for_workers()

    elif option == 'quit':
        with open('under_construction.csv', 'w') as under_construction:
            csv_writer = csv.writer(under_construction)
            csv_writer.writerow(['station'])
            for item in stations_under_construction:
                csv_writer.writerow([item])

        return

skyroute()
