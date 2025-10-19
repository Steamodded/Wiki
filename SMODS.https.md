# API Documentation: `SMODS.https`
The SMODS.https module is a module designed to be compatible with the [lua-https](https://love2d.org/wiki/lua-https) module. The main difference between this and the built in https module is that `SMODS.https` works on more platforms out of the box, compared to Balatro's shipped https modules (which is only availible on Windows by default).
- [Usage](#usage)
- [API Methods](#api-methods)
- [Example Usage](#example-usage)

## Usage

To use this module you must first `require` it, like so:

```lua
local https = require "SMODS.https"
```

## API Methods

- `https.request(url, options) -> code, body, headers`
  - `url`: The URL to request.
  - `options`: Additional optional options for the request.
    - `headers`: Additional headers to add to the request as key-value pairs.
    - `method` (One of `"GET"|"POST"|"HEAD"|"PUT"|"DELETE"|"PATCH"`): HTTP method. If absent, it's either "GET" or "POST" depending on the data field.
    - `data`: Optional additional data to send as application/x-www-form-urlencoded (unless specified otherwise in Content-Type header).
    - Return values:
      - `code`: HTTP status code, or 0 on failure.
      - `body`: The response body on success. Either nil or a description of the error on failure.
      - `headers`: HTTP response headers as key-value pairs, or nil on failure.

- `https.asyncRequest(url, optionsOrCallback, callback)`
  - `url`: The URL to request.
  - `optionsOrCallback`: If callback is nil, this can be set to a function instead of the callback. Otherwise is treated like option (see `http.request`)
  - `callback`: A function to call when the request is done, or nil if the callback is set in `optionsOrCallback`. 
    - `callback(code, body, headers)` - The callback to call. For meanings on the values, see `http.request`'s return values

## Example Usage

```lua
local https = require "SMODS.https"

print(https.request("https://example.com")) -- Sync request

https.asyncRequest("https://example.com", print) -- Async request
```

