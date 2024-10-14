from events import *

# Cornucopia events with weights
cornucopia_event_pool = [cornucopiaEvent, weaponEquip, weaponKill, meleeKill]
cornucopia_weights = [0.5, 0.25, 0.16, 0.1]  # Weights must add up to 1 or be scaled

# Day events with weights
day_event_pool = [dayEvent, weaponKill, meleeKill, suicide, weaponEquip]
day_weights = [0.45, 0.25, 0.15, 0.05, 0.1]  # Example of varying probabilities

# Night events with weights
night_event_pool = [nightEvent, weaponKill, meleeKill, suicide, weaponEquip]
night_weights = [0.5, 0.2, 0.1, 0.1, 0.1]  # Night events skew towards "nightEvent"

# Endgame day events with weights
endgame_day_event_pool = [dayEvent, weaponKill, meleeKill]
endgame_day_weights = [0.3, 0.4, 0.3]

# Endgame night events with weights
endgame_night_event_pool = [nightEvent, weaponKill, meleeKill]
endgame_night_weights = [0.35, 0.4, 0.25]

def get_event_pool(cycle, tributes, startingTributes):
    # Cornucopia phase
    if cycle == 2:
        return cornucopia_event_pool, cornucopia_weights
    
    # Endgame Day phase (low tribute count)
    elif cycle % 2 == 0 and len(tributes) < len(startingTributes) / 4:
        return endgame_day_event_pool, endgame_day_weights
    
    # Endgame Night phase (low tribute count)
    elif cycle % 2 == 1 and len(tributes) < len(startingTributes) / 4:
        return endgame_night_event_pool, endgame_night_weights
    
    # Regular Day phase
    elif cycle % 2 == 0:
        return day_event_pool, day_weights
    
    # Regular Night phase
    else:
        return night_event_pool, night_weights