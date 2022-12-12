'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
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
    
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        status = "friends"
    elif to_member in social_graph[from_member]['following']:
        status = "follower"
    elif from_member in social_graph[to_member]['following']:
        status = "followed by"
    else:
        status= "no relationship"
    return status


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
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
    new_board=list(board)
    row_sum=[]
    col_sum=[]
    cross=[]
    other_cross=[]
    convert_cross=[]
    total_sum=[]
    
    for y in range (len(new_board)):
        for x in range (len(new_board[y])):
            if new_board[y][x]=='O':
                new_board[y][x]=7
            elif board[y][x]=='X':
                new_board[y][x]=1
            elif board[y][x]=='':
                new_board[y][x]=0

    for x in range (len(new_board)):
        row_sum.append(sum(new_board[x]))   
                
    for x in range (len(new_board)):
        col_sum.append(sum([item[x] for item in new_board]))
    
    for x in range (len(new_board)):
        cross.append(new_board[x][x])
        
    for x in range (len(new_board)):
        other_cross.append([item[len(new_board)-1-x] for item in new_board])
        
    for x in range (len(new_board)):
        convert_cross.append(other_cross[x][x])
                
    total_sum=row_sum+col_sum
    total_sum.append(sum(cross))
    total_sum.append(sum(convert_cross))
    
    if 7*len(new_board) in total_sum:
            winner='O'
    elif 1*len(new_board) in total_sum:
            winner='X'
    else:
            winner='NO WINNER'
            
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
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
    new_keys=list(route_map.keys())
    first_keys= [item[0]for item in new_keys]
    second_keys=[item[1]for item in new_keys]
    new_time=list(route_map.values())
    output=[]
    final=[]
    
    first_position=first_keys.index(first_stop)
    second_position=second_keys.index(second_stop)
        
    for x in range(len(new_time)):
            output=output+list(new_time[x].values())
    
    if first_stop==second_stop:
        return sum(output)
    elif first_position==second_position:
        return output[first_position]
    elif first_position<second_position:
        final=output[first_position:second_position+1]
        return sum(final)
    elif first_position>second_position:
        final=output[first_position:]+output[:second_position+1]
        return sum(final)
