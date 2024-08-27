 def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    
    s_h = 1
    # Give a very low reward by default
    reward = 1e-3

    # Give higher reward if the car is closer to center line 
    if (0.5*track_width - distance_from_center) >= 0.05 and all_wheels_on_track:
        reward = 3.0
    elif (0.5*track_width - distance_from_center) >= 0.05 and all_wheels_on_track:
        reward = 2.0
    elif (0.5*track_width - distance_from_center) >= 0.05 and all_wheels_on_track:
        reward = 1.0
    elif (0.5*track_width - distance_from_center) >= 0.05 and all_wheels_on_track:
        reward = 0.75
    elif (0.5*track_width - distance_from_center) >= 0.05 and all_wheels_on_track:
        reward = 0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    if speed < s_h:
        # Penalize if the car goes too slow
        reward = reward + 0.2
    else:
        # High reward if the car stays on track and goes fast
        reward = speed - s_h
        
    if abs(params["steering_angle"]) < 15:
        reward += 1

    # Always return a float value
    return float(reward)
