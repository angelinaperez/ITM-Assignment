'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i = from_member
    j = to_member
    
    if i in social_graph[j]["following"] and j in social_graph[i]["following"]: 
        return(print("friends"))
    elif j in social_graph[i]["following"]: 
        return(print("follower"))
    elif i in social_graph[j]["following"]: 
        return(print("followed"))
    else:
        return(print("no relationship"))

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    i = len(board)
    
    horizontal_line = [x for x in board]
    vertical_line = [x for x in zip(*board)]
    left_right = [board[i][i] for i, v in enumerate(board)]
    
    if i == 3:
        right_left = [board[2-i][i] for i, v in enumerate(board)]
    elif i == 4:
        right_left = [board[3-i][i] for i, v in enumerate(board)]
    elif i == 5:
        right_left = [board[4-i][i] for i, v in enumerate(board)]
    else:
        right_left = [board[5-i][i] for i, v in enumerate(board)]
    
    for each_tuple in horizontal_line:
        if all(x == "X" for x in each_tuple):
            return(print("X"))
        elif all(x == "O" for x in each_tuple):
            return(print("O"))
        
    for each_tuple in vertical_line:
        if all(x == "X" for x in each_tuple):
            return(print("X"))
        elif all(x == "O" for x in each_tuple):
            return(print("O"))
                  
    if all([x == "X" for x in left_right]) == True:       #leftright X
        return(print("X"))
    elif all([x == "O" for x in left_right]) == True:     #leftright O                
        return(print("O"))
    elif all([x == "X" for x in right_left]) == True:     #leftright X
        return(print("X"))
    elif all([x == "O" for x in right_left]) == True:     #leftright O                
        return(print("O"))
    else:
        return(print("NO WINNER"))

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    stop1 = list(route_map.keys())
    time_list = [i["travel_time_mins"] for i in route_map.values()]
    
    stop1_list = [i[0] for i in stop1]
    uno = stop1_list.index(first_stop)
    time1 = time_list[uno]

    stop2_list = [i[1] for i in stop1]
    dos = stop2_list.index(second_stop)
    time2 = time_list[dos]
    
    print(dos)
    print(uno)
    
    if (first_stop, second_stop) in stop1:
        finaltime = route_map[first_stop, second_stop]["travel_time_mins"]
    else:
        if first_stop == second_stop:
            finaltime = sum(time_list)
        elif uno < dos:
            time3 = time1 + time2
            dos_uno = dos - uno
            if dos_uno == 1:
                finaltime = time3
            else:
                dosuno_list = []
                dosuno_time = []
                while dos > uno:
                    dos = dos - 1
                    if dos == uno:
                        break
                    dosuno_list.append(dos)
                for eachindex in dosuno_list:
                    dosuno_time.append(time_list[eachindex])
                finaltime = time3 + sum(dosuno_time)  
        elif uno > dos:        
            time3 = time1 + time2
            length = len(route_map)
            unodos_list = []
            unodos_time = []
            dosuno_list = []
            dosuno_time = []
            while dos > 0:        
                dos = dos - 1
                dosuno_list.append(dos)   
            while uno < length:
                uno += 1
                if uno == length:
                    break
                unodos_list.append(uno)
            for eachindex in unodos_list:
                unodos_time.append(time_list[eachindex])
            for eachindex in dosuno_list:
                dosuno_time.append(time_list[eachindex])
            finaltime = time3 + sum(dosuno_time) + sum(unodos_time)    
    
    return str(finaltime) + " minutes"