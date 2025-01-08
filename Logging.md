# Logging

Steamodded implements 6 levels of logging, each with a different purpose. The levels are as follows:

- `TRACE`: Very detailed information, typically of interest only when diagnosing problems.
- `DEBUG`: Detailed information, typically of interest only when diagnosing problems.
- `INFO`: Confirmation that things are working as expected.
- `WARN`: An indication that something unexpected happened, or indicative of some problem in the near future. The
  software is still working as expected.
- `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
- `FATAL`: A serious error, indicating that the program itself may be unable to continue running.

## Logging usage

All logging functions follow the same pattern, with the first argument being the message, and the second argument being
the logger name. This argument order is consistent across all logging functions. The logger name is optional and will
default to `DefaultLogger` but it is strongly recommended that you use it for clarity purposes.

### Trace

#### Lua

```lua
sendTraceMessage("This is a trace message", "MyTraceLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: TRACE :: MyTraceLogger :: This is a trace message
```

### Debug

#### Lua

```lua
sendDebugMessage("This is a debug message", "MyDebugLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: TRACE :: MyDebugLogger :: This is a debug message
```

### Info

#### Lua

```lua
sendInfoMessage("This is an info message", "MyInfoLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: INFO  :: MyInfoLogger :: This is an info message
```

### Warn

#### Lua

```lua
sendWarnMessage("This is a warn message", "MyWarnLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: WARN  :: MyWarnLogger :: This is a warn message
```

### Error

#### Lua

```lua
sendErrorMessage("This is an error message", "MyErrorLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: ERROR :: MyErrorLogger :: This is an error message
```

### Fatal

#### Lua

```lua
sendFatalMessage("This is a fatal message", "MyFatalLogger")
```

#### Output

```log
2024-04-04 22:58:45 :: FATAL :: MyFatalLogger :: This is a fatal message
```

### Additional notes

A logger name can be any string, but it is recommended to use a descriptive name to make it easier to identify where
the log message is coming from.

An additional function `sendMessageToConsole` is available to send a log message with a custom log level. This function
is not recommended for general use.

You can, with this function, implements your own log levels, but it is not recommended to do so, as the debug console do
not support custom log levels by default. You will have to modify the debug console by yourself to support custom log
levels. If you want to do so, you'll find the function signature in
the [debug.lua](https://github.com/Steamodded/smods/blob/main/src/logging.lua#L39-L49) file, and the log
supported in the console on
the [tk_debug_window.py](https://github.com/Steamodded/smods/blob/main/tk_debug_window.py#L9-L16) file.

Keep in mind that other people may not have the same modifications as you, so it is recommended to use the default log
levels.

## Debug Console

The debug console is a tool that allows you to see the logs in real-time, filter them, and search for specific strings
within the logs. It is a very useful tool for debugging and diagnosing problems.

### Opening the Debug Console

The debug console requires python 3.6+ to be installed on your system. To open the debug console,
execute `tk_debug_window.py` in [the steamodded repo](https://github.com/Steamodded/smods/blob/main/tk_debug_window.py).

The debug console was not tested with python 3.6, but it _should_ work with it. It is recommended to use the latest
python release.

### Using the Debug Console

You need to have the debug console open before you start the game. The console will show all logs in real-time.

### Features

- You can filter logs by logger name.
- You can filter logs by log level (only a single level, or the level selected and above).
- You can search for a specific string within the logs shown.
- You can save the logs to a file using the top left dropdown.
- You can clear the logs all the logs received from the console.

### Shortcuts

- `Ctrl + F`: Focus the search bar.
- `Enter` when focused on the search bar: Go to the next search result.
- `Esc` when focused on the search bar or the logger filter: Focus back into the logs.
- `Shift + Enter` when focused on the search bar: Go to the previous search result.
- `Ctrl + S`: Save all logs to a file.
- `Ctrl + Shift + S`: Save filtered logs to a file.
- `Ctrl + D`: Clear all logs.
- `Ctrl + L`: Focus the logger filter.

## Issues

Please open an issue on the [GitHub repository](https://github.com/Steamodded/smods/issues/new) if you encounter
any problems with the debug console.
