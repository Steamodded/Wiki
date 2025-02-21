# API Documentation: `SMODS.https`

The SMODS.https module is a module designed to be compatible with the [lua-https](https://love2d.org/wiki/lua-https) module. The main difference between this and the built in https module is that `SMODS.https` works on more platforms out of the box, compared to Balatro's shipped https modules (which is only availible on Windows by default).

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

## Example Usage

```lua
local https = require "SMODS.https"

print(https.request("https://example.com"))
```

