# The Balatro Event System

You can make a new event and dispatch it like so 

```lua
G.E_MANAGER:add_event(Event({}))
```

Which is an event which does nothing :tada:

However, you probably want to do something in this event. Let's cover some of the properties you can pass to the event handler


# Properties
These can be passed in a table to the Event function. 

trigger - string:
- "immediate" (default) - Runs as soon as possible
- "after" - Will run after a set amount of time. Also see delay
- "condition" - Will not finish until the condition is met. For most cases, you probably just want to use immediate with a check (see func). See ref_table, ref_value and stop_val for how to set this.
- "ease" - Used to interpolate values. Useful for score incrementing or movement. Also see ref_table, ref_value and ease_to for how to set this.
- "before" - Will run immediately, but if it doesn't complete before the set amount of time, it will be cancelled. Also see delay

blocking - boolean: Whether or not this event may block other events. Default is true

blockable - boolean: Whether or not this event may be blocked by other events is true

func - function: The function to call for the event. When this is called depends on the trigger type.
    This function takes no arguments. 
    It returns whether it completed. If true, then the event is over, if false, then it will be called again next time the event manager processes events (the next frame).
    It's behavior for each trigger is as follows:
- immediate - Called when events are next processed
- after - Called when the time is over
- condition - Behaves like immediate. Providing a function will overwrite the default condition behaviour. If you want to do stuff conditionally and use a function, then just do your check and return false if the condition is not satisfied.
- ease - Called each frame with the current value of the ease. The function defintion is a bit different here. The first argument is the current value of the ease. The return value is then set to the value stored in the table. The default function just returns the current value.
- "before" - Called immediately. If the event does not complete after the delay, then it is automatically canceled.

delay - number: The time to take, in seconds. Used for after, ease and before. Note this value is effected by the game speed option. Default is 0.

ref_table - table: The table to check for the condition. Used for condition and ease. No default

ref_value - string: The key in ref_table to get the value. Used for condition and ease. No default.

stop_val - any: The value to stop at. Used for condition. No default.

ease_to - number: The value to end at. Used for ease. No default.

ease - string: The type of ease to use. Used for ease. Default is "lerp". Can be any of "lerp", "elastic" or "quad".

# Examples
Great, now you've been info dumped, let's show you some more practical examples.

The below code will run the function `print("Hello, world!")` as soon as the event is processed. Make sure to remember to return true at the end of the function, otherwise it will be called again next frame.

```lua
G.E_MANAGER:add_event(Event({
    func = function() 
        print("Hello, world!")
        return true 
    end
}))
```

Now of course, you might be wondering, why wouldn't I just call the function directly? Well, the real power of this is when used in tandom with other events. If you run this event in the  calculate_joker context, you'll notice that it won't run right away, but only after the joker(s) before it are done doing their stuff. 

If you remember from earlier, there are blockable and blocking properties on events. This is what allows this to happen. The previous calculations are blocking, and your calculation is blockable, so it will wait until the blocking events are done before running.

This also works for after events. For example, if you want to run the function after 5 seconds, you can do this:

```lua
G.E_MANAGER:add_event(Event({
    trigger = "after", 
    delay = 5, 
    func = function() 
        print("Hello, world!") 
        return true 
    end
}))
```

(you may notice this might be less than 5 seconds. This is because the delay is effected by the game speed option)

Also note that this event will block for those 5 seconds, so other events will also wait your 5 seconds, just like the immediate event.

Now, let's say you want to block until a certain condition is met. You can do this by checking your condition, and returning false if it is not met. For example, if you want to wait until the player has 2 hands left, you can do this:

```lua
G.E_MANAGER:add_event(Event({
    func = function() 
        if G.GAME.current_round.hands_left ~= 2 then
            return false
        end
        print("Hello, world!")
        return true
    end,
    blocking = false
}))
```

Note the blocking false I made. This may be nessicary if what you are waiting for is blockable (you can lock up the game if you're not careful).

Now let's get to the last main type. Easing. This is used for interpolating values. For example, if you want to increase the round score by 1000 over 5 seconds, you can do this:

```lua
G.E_MANAGER:add_event(Event({
    trigger = "ease",
    delay = 5,
    ref_table = G.GAME,
    ref_value = "chips",
    ease_to = G.GAME.chips + 1000,
}))
```

and with that, you should have everything you need to use events. However, I'll cover some more stuff just in case you want more.

# Further Reading
So far we have just been adding events to the base queue. However, there are a few other queues for us to use.

## Queues
When calling G.E_MANAGER:add_event, you can pass in a second argument for the queue. This is string corresponding to the queue type (default is "base"). The queues are as follows:

- base - The default queue. This is where most events should go.
- other - Was once used for displaying a video in the demo. Since it's not used, it makes for a prime candidate for putting stuff in, if you want to use blocking but not block the base queue.

The rest are all mostly for super specific things, but are documented here for completeness.

- unlock - This queue is for when you unlock new stuff. This allows it to keep showing new items when you close the last one.
- tutorial - This is used for the tutorial. Allows it to manage some of it's stuff. Also let's all the tutorial stuff be cleared at once.
- achievement - This is used for unlocking achievements. Allows the ui to show one at a time.

add_event also has a third argument, front. This is a boolean that will put the event at the front of the queue. Useful to block stuff already in the queue.

## Clearing the queue
The event manager also has another function you may use.
G.E_MANAGER:clear_queue(queue, exception)

Passing it with no options will clear all the queues. If a queue is passed, it will clear that queue. If an exception is passed, it will not clear all queues, except the one passed. You can avoid being cleared by setting the no_delete property to true.

## Repeating on a timer
Here is an example I made to run an event every 5 seconds. This does use a bit of hacking to get working, but I figured it might be handy.

```lua
local event
event = Event {
    blockable = false,
    blocking = false,
    pause_force = true,
    no_delete = true,
    trigger = "after",
    delay = 5,
    func = function()
        print("Hi mom!")
        event.start_timer = false
    end
}
G.E_MANAGER:add_event(event)
```

This works by storing a reference to the event, then setting the start_timer property to false. This will cause the event to think it never started the timer, and as such restart it after running the event, causing it to repeat every 5 seconds.

This event also set's some properties to make sure it doesn't get block, block other events, and run even if the game is paused. If you want to make sure you can stop this event, then you could add some check for some variable then return if it's true or smth.


## More properites
These are some more event properties you can use, but aren't really that useful in most situations.

start_timer - boolean: If true, then it will use the starting time of the event being created. Otherwise this will start them timer the first time the event is processed. Default is false.

no_delete - boolean: If true, then when clearing the event queue, this event will not be deleted. You probably don't want to use this unless you want to have an event that never stops. Default is false.

force_pause - boolean: If true, then the event will run even if the game is paused. This only has an effect if your command was created when the game wasn't paused. Default is false.

timer - string: The name of the timer to use. Default is "REAL" of created while paused (or with force_pause) otherwise "TOTAL". Can take any of the keys in G.TIMERS.

***
*Guide written by WilsontheWolf*