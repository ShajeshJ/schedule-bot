"""
Features:
- Command 1: /schedule configure (accessible to admins)
    - configure the day of the week to try to schedule over (Sun -> Sat)
    - configure the start and end times of the schedule
    - configure the channel to post the schedule in
    - configure player threshold (minimum number of players to schedule a game for a day)
    - upon reconfiguration:
        - do nothing and use updated
- Command 2: /email subscribe (accessible to everyone)
    - register an email to be automatically invited to the calendar events
- Command 3: /email unsubscribe (accessible to everyone)
    - unregister an email from the calendar events
- Command 4: /event create (accessible to admins)
    - manually create a new event
- Command 5: /event delete (accessible to admins)
    - delete an already scheduled event

- Background Tasks
    - create a 7-day poll that starts 10 days before the end of the month
    - after poll ends, create calendar invites based on poll results
    - at 9 AM on a scheduled day, post a reminder in the channel about game day with a checkmark reaction
    - (maybe) add discord event as well
    - (maybe) 24 hours after the last person votes, end the poll early
    - (maybe) remind players to vote
"""
