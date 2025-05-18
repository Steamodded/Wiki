# The Balatro Event System

You can make a new event and dispatch it like so

```lua
G.E_MANAGER:add_event(Event({}))
```

Which is an event which does nothing :tada:

However, you probably want to do something in this event. Let's cover some of the properties you can pass to the event handler.


# Properties
These can be passed in a table to the Event function.

trigger - string:
- `"immediate"` (default) - Runs as soon as possible
- `"after"` - Runs after a set amount of time specified in `delay`
- `"before"` - Runs immediately. The event takes at least the amount of time specified in `delay` to finish
- `"condition"` - Waits until the condition is met (namely, when `config.ref_table[config.ref_value] == config.stop_val`). You probably want to use `immediate` instead.
- `"ease"` - Used to interpolate values. Useful for score incrementing or movement. Acts something like `config.ref_table[config.ref_value] = config.func(ease_function(original_value, config.ease_to, config.duration))`

blocking - boolean: Whether or not this event may block other events. Default is true.

blockable - boolean: Whether or not this event may be blocked by other events. Default is true.

func - function: The body of the event. This is where you will perform any actions or custom delays. Once the event starts, this will be run once per frame until it returns true. This can be omitted without consequence.
    Its behavior for each trigger is as follows:
- `immediate` - Called when the event begins
- `after` - Called when the time is over
- `condition` - Behaves exactly like immediate. Providing a function will overwrite the default condition behaviour.
- `ease` - Called each frame with the current interpolated value so you can modify the easing function. The default function returns its argument unmodified.
- `before` - Called when the event begins

delay - number: The time to take, in seconds. Used for after, ease and before. This value is typically affected by the game speed option. Default is 0.

ref_table - table: The table to ease a value in. Required for ease events. Also used for condition events.

ref_value - string: The key in ref_table to ease. Required for ease events. Also used for condition events.

ease_to - number: The value for the ease to end at. Required for ease events.

ease - string: The type of ease to use. Used for ease. Default is "lerp". Can be any of "lerp" (linear ease), "elastic" (wobbly ease in) or "quad" (quadratic ease in).

## Advanced Properties

stop_val - any: The value to wait for in a condition event.

start_timer - boolean: Set to true to start the time component of a before or after event immediately, instead of when the event starts.

no_delete - boolean: Set to true to prevent the event from being deleted by `clear_queue`.

pause_force - boolean: Set to true to force this event to act as though it were created while the game was paused. Events without this will pause when the game is paused.

timer - string: Set this to a key in `G.TIMERS` to use a different timer than the standard one. If `pause_force` was set, this defaults to `'REAL'`, otherwise it defaults to `'TOTAL'`.

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

Now of course, you might be wondering, why wouldn't I just call the function directly? Well, the real power of this is when used in tandem with other events. If you create this event in a calculate() function, you'll notice that it won't run right away, but only after the joker(s) before it are done doing their stuff.

If you remember from earlier, there are blockable and blocking properties on events. This is what allows this to happen. The previous calculations are blocking, and your calculation is blockable, so it will wait until the blocking events are done before running.

This also works for "after" events. For example, if you want to run the function after 5 seconds, you can do this:

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

(This might take less than 5 seconds. This is because the delay is affected by the game speed option)

Note that this event will block for those 5 seconds, so like earlier, other events will wait until after your event is over. In this case, they'll wait for 5 seconds.

Now, let's say you want to wait until a certain condition is met. You can do this by checking your condition, and returning false if it is not met. For example, if you want to wait until the player has 2 hands left, you can do this:

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

Note `blocking = false`. This may be necessary if something blockable happens before what you are waiting for (you can lock up the game if you're not careful).

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

## Queues
So far we have just been adding events to the base queue. However, there are a few other queues for us to use.

When calling `G.E_MANAGER:add_event`, you can pass in a second argument for the queue. This is a string corresponding to the queue type (default is "base"). The queues are as follows:

- base - The default queue. This is where most events should go.
- other - Was once used for displaying a video in the demo. No longer used.

The rest are all mostly for super specific things, but are documented here for completeness.

- unlock - This queue is for when you unlock new stuff. This allows it to keep showing new items when you close the last one.
- tutorial - This is used for the tutorial. Allows it to manage some of it's stuff. Also let's all the tutorial stuff be cleared at once.
- achievement - This is used for unlocking achievements. Allows the ui to show one at a time.

You can also create your own queue:
```lua
G.E_MANAGER.queues.my_cool_queue = {}
```

`add_event` also has a third argument, front. This is a boolean that will put the event at the front of the queue. Using this within an event will cause incorrect behavior.

## Clearing the queue
The event manager has another function:
`G.E_MANAGER:clear_queue(queue, exception)`

Calling it with no options will clear all the queues. If a queue is passed, it will clear that queue. If an exception is passed, it will clear every queue except the one passed. An event can avoid being cleared by setting its `no_delete` property to true.

## Repeating on a timer
Here is an example to run an event every 5 seconds. This does use a bit of hacking to get working, but I figured it might be handy.

```lua
local event
event = Event {
    blockable = false,
    blocking = false,
    pause_force = true,
    no_delete = true,
    trigger = "after",
    delay = 5,
    timer = "UPTIME",
    func = function()
        print("Hi mom!")
        event.start_timer = false
    end
}
G.E_MANAGER:add_event(event)
```

This works by storing a reference to the event, then setting the start_timer property to false. This will cause the event to think it never started the timer, and as such the event restarts after running the event, causing it to repeat every 5 seconds. (Later note: it may take more than 5 seconds depending on how frequently the game updates)

We use `timer = "UPTIME"` here as the default timer (`"REAL"`) is reset when returning to the menu or starting a new game. Without this the event would not fire until the timer catches up to what it was.

This event also sets some properties to make sure it doesn't get blocked or block other events, and it runs even if the game is paused. If you want to make sure you can stop this event, then you could, say, add some check for some variable then return if it's true.

Here's another way to accomplish the same thing:
```lua
local create_event
create_event = function()
    G.E_MANAGER:add_event(Event {
        blockable = false,
        blocking = false,
        pause_force = true,
        no_delete = true,
        trigger = "after",
        delay = 5,
        func = function()
            print("Hi mom!")
            create_event()
            return true
        end
    })
end
create_event()
```

***
*Guide written by WilsontheWolf*
