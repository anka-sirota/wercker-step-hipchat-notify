import sys
import hipchat

if len(sys.argv) < 7:
    print 'There should be 7 arguments'
    sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
message_from = str(sys.argv[3])
message = str(sys.argv[4])
color = str(sys.argv[5])
notify = (str(sys.argv[6]) in ('true', '1', 'TRUE')) and True or False

hipster = hipchat.HipChat(token=token)
kargs = {
    'room_id': room_id,
    'message_from': message_from,
    'message': message,
    'color': color,
    'notify': notify
}
hipster.message_room(**kargs)
