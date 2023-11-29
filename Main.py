from Consumer import receive_messages
from Models.CatheterPosition import CatheterPosition


msg_channels_data = []
move_catheter = ('MoveCatheter', 'request')
get_position = ('GetCurrentPosition', 'request')
reset_position = ('ResetPosition', 'request')
position_reply = ('CatheterPosition', 'reply')

msg_channels_data.append(move_catheter)
msg_channels_data.append(get_position)
msg_channels_data.append(reset_position)
msg_channels_data.append(position_reply)

receive_messages(msg_channels_data)
# receive_messages("MoveCatheter", "request")
print('kfir')
