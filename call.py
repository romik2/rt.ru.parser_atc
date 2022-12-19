import datetime

now = datetime.datetime.now()

datetime = now.strftime("%d-%m-%Y %H:%M:%S")
defiant = ''
caller_number = ''
callee_name = ''
called_number = ''
first_responder = ''
type = ''
status = ''
duration = ''
incoming_line = ''
group_data = ''
link_to_call_recording = ''

def valueValidate(value):
    if (value == None):
        return ''
    else:
        return value

def get_gata_call():
    return (datetime, defiant, caller_number, callee_name, called_number, first_responder, type, status, duration, incoming_line, group_data, link_to_call_recording)

def set_data_call(row):
    global datetime
    global defiant
    global caller_number
    global callee_name
    global called_number
    global first_responder
    global type
    global status
    global duration
    global incoming_line
    global group_data
    global link_to_call_recording
    datetime = valueValidate(row[0]) + " " + valueValidate(row[1])
    defiant = valueValidate(row[2])
    caller_number = valueValidate(row[3])
    callee_name = valueValidate(row[4])
    called_number = valueValidate(row[5])
    first_responder = valueValidate(row[6])
    type = valueValidate(row[7])
    status = valueValidate(row[8])
    duration = valueValidate(row[9])
    incoming_line = valueValidate(row[10])
    group_data = valueValidate(row[11])
    link_to_call_recording = valueValidate(row[12])