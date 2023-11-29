from Consumer import receive_messages
from Models.CatheterPosition import CatheterPosition
from Producer import init_connection


msg_channels_data = []
move_catheter = ('MoveCatheter', 'request')
get_position = ('GetCurrentPosition', 'request')
reset_position = ('ResetPosition', 'request')
position_reply = ('CatheterPosition', 'reply')

msg_channels_data.append(move_catheter)
msg_channels_data.append(get_position)
msg_channels_data.append(reset_position)
msg_channels_data.append(position_reply)

channel = init_connection()
receive_messages(msg_channels_data, channel)
# receive_messages("MoveCatheter", "request")
print('kfir')
