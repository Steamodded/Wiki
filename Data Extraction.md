# Guide to Extracting Data
This is (hopefully) a simple and easy to understand guide for extracting data from the game. My intention in writing this guide is to present it as the guide that I wish that I had when I was writing my Balatro mod.

## G
`G` is the table that represents the game as a whole. All information is stored in `G`. Some of the information you may require may be stored in `G.GAME`, while some is stored in `G`

#### Some examples include...
- `G.hand` contains the cards that you currently have in your hand
- `G.jokers` contains the jokers you currently have

#### Some other examples include...
- `G.GAME.hands` which stores information regarding the hands you have played so far. This includes the `level` of the hand, the amount of `mult` and `chips` that the hand scores, and how many times this hand has been `played`
- `G.GAME.blind` stores information about the current blind. For example, `G.GAME.blind.chips` stores the amount of chips needed to beat the current blind
- `G.GAME.pseudorandom.seed` stores the current game's seed

## Cards
Almost everything is some kind of card. Cards can be accessed using their specified table, such as `G.hand`. When accessing `G.hand`, you will find that this contains an array of cards. Cards have many properties you may wish to extract, such as:
- `G.hand.cards[x].config.name` is the name of the card, such as "King of Spades"
- `G.hand.cards[x].config.center.key` is the type (or edition) of the card. Normally, this is `c_base`, representing a normal card, however this could be something like `m_mult` for a mult card
- `G.hand.cards[x].seal` gets any kind of seal on the card. I'd reccomend accessing this as `local card_seal = G.hand.cards[x].seal or "NONE"`, to add a specific value for accessing the card seal if none is found
- `G.jokers.cards[x].edition` is a table that holds information about joker editions, for example `G.jokers.cards[x].edition.key` could be `e_foil` for a foil card.

## Experimentation
[Steamodded/Wiki PR #30](https://github.com/Steamodded/Wiki/pull/30) contains additional details about the fields in `G`. While it's not currently accepted, that and my own experiementation helped me find some of the fields that I needed when I was developing a mod.

With that said, here's something you may find useful:
```lua
-- This function explores a table and returns a JSON string representation of it
-- It will not explore any key called "parent" or "children" to avoid useless recursion
local function table_explore(table, current_depth)
    -- Initialize depth if not provided
    if not current_depth then
        current_depth = 0
    end

    -- Check if we are at the maximum depth
    if current_depth > 5 then
        -- If we are, then return an empty array
        log("Maximum recursion depth reached. Stopping exploration.")
        return {}  
    end

    -- Create an empty array to store the result
    local result = {}
    for key, value in pairs(table) do
        -- Check if the key is either "parent" or "children"
        if key ~= "parent" and key ~= "children" then
        
            -- They aren't so is this key's value's type another table?
            if type(value) == "table" then
                
                -- Yes it is, so recursively explore this (adding 1 to depth)
                result[key] = table_explore(value, current_depth+1)
            else
                -- No it isn't, so just add the value
                result[key] = value
            end
        end
    end

    -- Return the result
    return result
end
```

You can call it in the following way, and then I'd reccomend using the built-in JSON serialiser to convert it to a nice and easy to read format.
```lua
local result = table_explore(some_table)
```

Also be aware that the 5-depth limit is for performance. You can change it if you'd like, but beyond 5 levels deep the game may freeze for a while or crash. 

In addition to the above, don't call this function often. It is intended as a developer tool to allow exploration and experimentation, not for general use. You should always access the value directly (`local some_value = G.GAME.some_table.some_value`) if you can

## JSON
I'd reccomend using the included JSON functionality to easily look at data extracted from the game. You can seralize `nil`, `table`, `string`, `number`, and `boolean` data types by default, so implimenting some sort of check to ensure the data you have is of that type is advised.

For example, using this to view data from the `table_explore` function above:
```lua
-- Ensure we have the module loaded. You don't need to do this multiple times
local json = require "json"

-- Explore the table and then convert to JSON
local result = table_explore(some_table)
local json_result = json.encode(result)
```
And then you can do what you need to with it. One idea is [this json viewer](https://jsonviewer.stack.hu/) where you easily view JSON objects in a nesting style

