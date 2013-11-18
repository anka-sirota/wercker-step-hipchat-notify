# hipchat-notify

Send a message to a HipChat room... with color!

# What's new

- Add support for color for passed and failed messages (thanks adams-sarah)
- Add support for 'notify' for passed and failed messages

# Options

* `token` (required) Your HipChat token.
* `room-id` (required) The id of the HipChat room.
* `passed-message` (optional) The message which will be shown on a passed build or deploy.
* `failed-message` (optional) The message which will be shown on a failed build or deploy.
* `passed-color` (optional, default: `green`) The color of a passed build/deploy message in HipChat.
* `failed-color` (optional, default: `red`) The color of a failed build/deploy message in HipChat.
* `passed-notify` (optional, default: `false`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `failed-notify` (optional, default: `true`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `from-name` (optional, default: `wercker`) Use this option to override the name that will appear in the room as sender.
* `on` (optional, default: `always`) When should this step send a message. Possible values: `always` and `failed`.

# Example

Add HIPCHAT_TOKEN as deploy target or application environment variable.

```yaml
build:
  after-steps:
    - hipchat-notify:
        token: $HIPCHAT_TOKEN
        room-id: id
        from-name: name
```

# License

The MIT License (MIT)

# Changelog

## 0.1.6

- Add support for color for passed and failed messages (thanks adams-sarah)
- Add support for 'notify' for passed and failed messages

## 0.1.5

*Broken*

## 0.1.4

- Fix example in readme
- Update readme
